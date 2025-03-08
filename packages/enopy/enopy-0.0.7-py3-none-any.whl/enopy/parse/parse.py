import re
from collections import defaultdict
from pathlib import Path, PurePosixPath

from fans.logger import get_logger

from enopy.convert import to_snippet
from .markdown import parse_markdown
from .snippet import parse_snippet
from .snippets.mindmap import parse_mindmap
from .cmds import eno_cmds


logger = get_logger(__name__)


def parse_eno(text: str, path: str = None) -> dict:
    """
    Params:
        text - text content in eno format
        path - OPTIONAL eno path, e.g. /todo/main.eno (used for cross reference)

    Returns:
        dict: {
            'tokens' - eno tokens
            'refToTokens'
            'tagToTokenGroups'
        } parsed eno
    """
    if path:
        path = PurePosixPath(path)

    context = {
        'path': path,
        'post_process': [],
    }

    tokens = parse_markdown(text)
    tokens = trans_tokens(tokens, context)
    tokens = layouted(tokens)

    eno = {
        'tokens': tokens,
        'refToTokens': {},
        'tagToTokenGroups': {},
    }

    execute_cmds(tokens, context)

    if 'post_process' in context:
        # template etc
        for post_process, data in context['post_process']:
            post_process(eno, data)
    del context['post_process']

    return eno


def parse_path(path: str):
    with Path(f'/no{path}').open() as f:
        text = f.read()
    return parse_eno(text)


def trans_tokens(tokens, context):
    return [trans_token(token, context, toplevel = True) for token in tokens]


def trans_token(token, context, toplevel = False):
    trans = trans_mapping.get(token['type'])
    if trans:
        token = trans(token, context = context, toplevel = toplevel)
    if 'tokens' in token:
        token['tokens'] = [trans_token(d, context) for d in token['tokens']]
    return token


def layouted(tokens: list):
    """
    Params:
        tokens - List of block level tokens
    """
    stack = [{'type': 'eno-layout', 'depth': 0, 'tokens': []}]

    top_layout = None
    for token in tokens:
        layout = get_layout(token)
        if layout:
            if 'top' in layout['dots']:
                layout['top'] = True
                top_layout = layout
            # higher level layout encountered, finalize previous ones
            while layout['depth'] <= stack[-1]['depth']:
                top = stack.pop()
                stack[-1]['tokens'].append(top)
            # begin layout (if not ending mark)
            if not layout['end']:
                stack.append(layout)
        else:
            layout_tokens = stack[-1]['tokens']
            if not layout_tokens:
                token['block_start'] = True
            layout_tokens.append(token)

    # finalize all layout into single one
    while len(stack) > 1:
        top = stack.pop()
        stack[-1]['tokens'].append(top)

    if stack and top_layout:
        stack[0]['tokens'].insert(0, {'show': True, **top_layout})

    return stack


layout_heading_regex = re.compile(r'(?P<title>.*)\{(?P<conf>.*)\}')


def get_layout(token):
    if token['type'] == 'heading':
        text = token['tokens'][0]['text']
        matc = layout_heading_regex.match(text)
        if matc:
            token['type'] = 'eno-layout'
            conf = matc.group('conf')
            end = False
            name = None
            dots = []
            if ':' in conf:
                name, claz = conf.split(':')
                if name.endswith('.end'):
                    name = name.split('.')[0]
                    end = True
            elif conf.startswith('.'):
                parts = conf.split()
                dots = [d[1:] for d in parts if d.startswith('.')]
                other_parts = [d for d in parts if not d.startswith('.')]
                claz = ' '.join(other_parts)
            else:
                claz = conf

            tokens = []
            title = matc.group('title').strip()
            if title:
                tokens.append({
                    'type': 'heading',
                    'depth': token['depth'],
                    'text': title,
                    'tokens': parse_markdown(title)[0]['tokens'],
                })
            return {
                'type': 'eno-layout',
                'name': name,
                'depth': token['depth'],
                'end': end,
                'claz': claz,
                'dots': dots,
                'tokens': tokens,
            }


def trans_code(token, context, **_):
    lang = token['lang']
    text = token['text']
    stripped_text = text.strip()
    if stripped_text.startswith('$$') or stripped_text.endswith('$$'):
        return {
            'type': 'block-math',
            'text': stripped_text.strip('$$'),
        }
    elif lang and lang.startswith('eno.'):
        return {
            **token,
            'snippet': parse_snippet(
                lang = lang,
                text = token['text'],
                data = token.get('data'),
                context = context,
            ),
            'lang': lang,
            'type': 'eno-snippet-v2',
        }
    else:
        return token


def trans_list(token, toplevel, **_):
    if toplevel and token['bullet'] == '*':
        root = parse_mindmap(token['items'][0])
        root['scale'] = 2.0
        for child in root['children']:
            child['scale'] = 1.2
        return {
            'type': 'eno-mindmap',
            'root': root,
        }
    else:
        return token


def trans_codespan(token, context, **_):
    text = token['text']
    if text.startswith('eno.'):
        token['type'] = 'inline-eno-snippet'
        token['snippet'] = parse_snippet(token['text'], '', None, context)
    elif text.endswith('\\'):
        # inline math `\sin{\theta}\`
        token['type'] = 'inline-math'
        token['text'] = '$' + token['text'][:-1] + '$'
    elif text.startswith('$') and text.endswith('$'):
        token['type'] = 'inline-math'
    elif text.startswith('$$') and text.endswith('$$'):
        token['type'] = 'inline-display-math'
    elif text.startswith('((') and text.endswith('))'):
        token['type'] = 'inline-common-lisp'
    elif text.startswith('${') and text.endswith('}'):
        token['type'] = 'inline-js'
    return token


def trans_paragraph(token, **_):
    tokens = token['tokens']
    if len(tokens) == 1:
        tok = tokens[0]
        if (
            tok['type'] == 'codespan' and
            tok.get('text').startswith('eno.')
        ):
            token['type'] = 'eno-div'
        elif (
            tok['type'] == 'text' and
            tok.get('text').startswith('{') and
            tok.get('text').endswith('}')
        ):
            token['type'] = 'eno-cmd'
            token['cmds'] = []
            for text in tokens[0]['text'].split('{'):
                if text:
                    parts = text.strip()[:-1].split()
                    token['cmds'].append({
                        'type': parts[0],
                        'args': parts[1:]
                    })
            del token['tokens']
    elif len(tokens) > 1:
        tok = tokens[0]
        if (
            tok['type'] == 'text' and
            datetime_regex.match(tok.get('text'))
        ):
            token['datetime'] = tok['text']
            token['tokens'] = token['tokens'][1:]
    return token


def execute_cmds(tokens, context):
    for i_token, token in enumerate(tokens):
        if token.get('tokens'):
            execute_cmds(token['tokens'], context)
        else:
            match token['type']:
                case 'eno-cmd':
                    for cmd in token['cmds']:
                        args = cmd['args']
                        handler = eno_cmds.get(cmd['type'])
                        if handler:
                            handler.on_cmd(args, context)
                case 'inline-eno-snippet':
                    snippet = token['snippet']
                    for cmd in eno_cmds.values():
                        cmd.on_snippet(snippet, context)
                case _:
                    for cmd in eno_cmds.values():
                        ret = cmd.on_token(token, context)
                        #if ret and ret is not token:
                        #    tokens[i_token] = {
                        #        'type': 'eno-snippet-v2',
                        #        'snippet': to_snippet(ret)[0],
                        #    }


trans_mapping = {
    'code': trans_code,
    'list': trans_list,
    'paragraph': trans_paragraph,
    'codespan': trans_codespan,
}
datetime_regex = re.compile(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d')
