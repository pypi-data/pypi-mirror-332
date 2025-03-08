import html
import functools

from marko.ext.gfm import gfm


def parse(text):
    doc = gfm.parse(text)

    tokens = []
    for block in doc.children:
        block_type = block.get_type()

        if block_type not in maker_mapping:
            raise RuntimeError(f'unsupported {block}')

        token = maker_mapping[block.get_type()](block)
        if token:
            tokens.append(token)

    return tokens


def make_token(elem):
    try:
        return maker_mapping[elem.get_type()](elem)
    except KeyError:
        raise RuntimeError(f'{elem}')
    except:
        print('elem', elem)
        exit()


def make_tokens(elem):
    tokens = [make_token(d) for d in elem.children]
    return [d for d in tokens if d]


def make_paragraph(elem):
    tokens = make_tokens(elem)
    return {
        'type': 'paragraph',
        'tokens': tokens,
    }


def make_quote(elem):
    tokens = make_tokens(elem)
    return {
        'type': 'blockquote',
        'text': get_text(tokens),
        'tokens': tokens,
    }


def make_blankline(block):
    return None


def make_code(elem, style = None):
    return {
        'type': 'code',
        'text': get_text(make_tokens(elem)),
        'lang': f'{elem.lang} {elem.extra}'.strip(),
        'codeBlockStyle': style,
    }


def make_list(elem):
    tokens = make_tokens(elem)
    return {
        'type': 'list',
        'ordered': elem.ordered,
        'bullet': elem.bullet,
        'start': elem.start if elem.start != 1 else '',
        'loose': not elem.tight,
        'items': tokens,
        'tokens': tokens,
        #'d': elem,
    }


def make_list_item(elem):
    #print(dir(elem))
    return {
        'type': 'list_item',
        'task': False, # TODO
        'loose': not elem._tight,
        'tokens': make_tokens(elem),
    }


def make_heading(elem):
    tokens = make_tokens(elem)
    raw = get_text(tokens)
    return {
        'type': 'heading',
        'depth': elem.level,
        'text': raw,
        'tokens': tokens,
    }


def make_text(elem):
    return {
        'type': 'text',
        'text': elem.children,
    }


def make_codespan(elem):
    return {
        'type': 'codespan',
        'text': elem.children,
    }


def make_linebreak(elem):
    #print(elem, elem.soft)
    return {
        'type': 'br',
    }


def make_link(elem):
    tokens = make_tokens(elem)
    href = elem.dest
    text = get_text(tokens) or elem.title or href
    return {
        'type': 'link',
        'text': text, # TODO: renderer should use tokens instead
        'href': href,
        'title': elem.title,
        'tokens': tokens,
    }


def make_hr(elem):
    return {
        'type': 'hr',
    }


def make_image(elem):
    try:
        text = elem.children[0].children
    except:
        text = ''
    return {
        'type': 'image',
        'href': elem.dest,
        'title': elem.title,
        'text': elem.title or text or '',
    }


def make_table(elem):
    tokens = make_tokens(elem)
    header = tokens[0]
    return {
        'type': 'table',
        'header': [d['tokens'] for d in header['tokens']],
        'rows': [[d['tokens'] for d in row['tokens']] for row in tokens[1:]],
        'align': [None] * len(header['tokens']),
        'tokens': tokens,
    }


def make_table_row(elem):
    return {
        'type': 'table_row',
        'tokens': make_tokens(elem),
    }


def make_table_cell(elem):
    return {
        'type': 'table_cell',
        'tokens': make_tokens(elem),
    }


def make_strong(elem):
    tokens = make_tokens(elem)
    return {
        'type': 'strong',
        'text': get_text(tokens),
        'tokens': tokens,
    }


def make_link_ref_def(elem):
    return None
    return {
        'type': 'link_ref_def',
    }


def make_del(elem):
    return {
        'type': 'del',
        'tokens': make_tokens(elem),
    }


def make_emphasis(elem):
    tokens = make_tokens(elem)
    return {
        'type': 'em',
        'text': get_text(tokens),
        'tokens': tokens,
    }


def make_literal(elem):
    return {
        'type': 'escape',
        'text': elem.children,
    }


def make_inline_html(elem):
    return {
        'type': 'html',
    }


maker_mapping = {
    'Paragraph': make_paragraph,
    'Quote': make_quote,
    'CodeBlock': functools.partial(make_code, style = 'indented'),
    'FencedCode': functools.partial(make_code, style = 'fenced'),
    'List': make_list,
    'ListItem': make_list_item,
    'Heading': make_heading,
    'RawText': make_text,
    'CodeSpan': make_codespan,

    'BlankLine': make_blankline,
    'LineBreak': make_linebreak,

    'Url': make_link,
    'ThematicBreak': make_hr,
    'Image': make_image,
    'Table': make_table,
    'Link': make_link,
    'StrongEmphasis': make_strong,
    'TableRow': make_table_row,
    'TableCell': make_table_cell,
    'LinkRefDef': make_link_ref_def,
    'Strikethrough': make_del,
    'Emphasis': make_emphasis,
    'Literal': make_literal,
    'InlineHTML': make_inline_html,
}


def get_text(tokens):
    parts = []
    for token in tokens:
        match token:
            case {'text': text}:
                parts.append(text)
            case {'type': 'br'}:
                parts.append('\n')
            case {'tokens': sub_tokens}:
                parts.append(get_text(sub_tokens))
    return ''.join(parts)
