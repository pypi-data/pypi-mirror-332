import re

import yaml
from fans.logger import get_logger

from eno import colors
from eno.parse.utils import get_text


logger = get_logger(__name__)


def parse_mindmap(token):
    if token['type'] != 'list_item':
        return {'text': get_text(token), 'children': []}
    meta = {}
    attrs = parse_text(get_text(token['tokens'][0]))
    children = []
    for item in token['tokens']:
        match item['type']:
            case 'code':
                meta = yaml.safe_load(get_text(item))
            case 'list':
                children = item['items']
    meta = {
        **attrs.get('meta', {}),
        **meta,
    }
    root = {
        **attrs,
        'children': [parse_mindmap(d) for d in children],
        'meta': meta,
    }
    root['meta']['more'] = bool(meta.get('content') and len(meta['content']))
    return root


content_regex = re.compile(r'(?P<prefix>\[.+\])?[^\[]+(?P<suffix>\[.+\])?')
rating_regex = re.compile(r'm\d')


def parse_text(text):
    ret = {
        'content': None,
    }
    if text.startswith('[') or text.endswith(']'):
        matc = content_regex.match(text)
        prefix = matc and matc.group('prefix') or ''
        suffix = matc and matc.group('suffix') or ''
        ret['content'] = text[len(prefix):(-len(suffix) or len(text))]
        ret['prefix'] = parse_inline(prefix)
        ret['postfix'] = parse_inline(suffix)
        ret['meta'] = {
            'content': [
                *(ret['postfix'].get('refs') or []),
                *(ret['postfix'].get('refTags') or []),
            ],
        }
    else:
        ret['content'] = text
    return ret


def parse_inline(text):
    if not text:
        return {}
    parts = text[1:-1].split()
    ret = {}
    refs = []
    ref_tags = []
    for part in parts:
        if rating_regex.match(part):
            ret['rating'] = parse_rating(part)
        elif part.startswith('ref-tag-'):
            ref_tags.append({'ref-tag': part[len('ref-tag-'):]})
        elif part.startswith('ref-'):
            refs.append({'ref': part[len('ref-'):]})
        elif part.startswith('`'):
            pass
        else:
            logger.info(f'unknown mindmap item inline {text} {part}')
    if refs:
        ret['refs'] = refs
    if ref_tags:
        ret['refTags'] = ref_tags
    return ret


def parse_rating(part):
    ret = {}
    match part:
        case 'm5':
            ret['stars'] = '✸'
            ret['color'] = colors.fg.red
        case 'm4':
            ret['stars'] = '★'
            ret['color'] = colors.fg.green
        case 'm3':
            ret['stars'] = '✭'
            ret['color'] = colors.fg.blue
            ret['scale'] = 0.9
        case 'm2':
            ret['stars'] = '✧'
            ret['color'] = colors.fg.lightblue
            ret['scale'] = 0.8
        case 'm1':
            ret['stars'] = '✧'
            ret['color'] = colors.fg.gray
            ret['scale'] = 0.6
    return ret


if __name__ == '__main__':
    m = content_regex.match('[m5] 球状闪电 林云')
    print(m)
