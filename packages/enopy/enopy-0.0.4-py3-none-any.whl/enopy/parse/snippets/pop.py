from .base import Impl


class Pop(Impl):

    def parse(self, snippet, context):
        snippet['conf'] = make_conf(snippet, {
            'args': snippet['inline'] and [
                {'type': 'alt', 'choices': [
                    {'name': 'content', 'pred': lambda d: d['type'] == 'string'},
                    {'name': 'path', 'pred': lambda d: d['type'] == 'path'},
                ]},
                {'name': 'title'},
            ] or [
                {'type': 'alt', 'choices': [
                    {'name': 'title', 'pred': lambda d: d['type'] == 'string'},
                    {'name': 'path', 'pred': lambda d: d['type'] == 'path'},
                ]},
                {'name': 'title'},
            ],
            'attrs': {
                'trigger': {'type': 'enum', 'values': ['click', 'hover']},
                'anchor': {'type': 'enum', 'values': ['button', 'link']},
                'container': {'type': 'enum', 'values': ['popover', 'drawer', 'collapse']},
                'size': {'type': 'enum', 'values': ['middle', 'small', 'large']},
                'active': {'type': 'enum', 'values': ['inactive', 'active']},
                'placement': {'type': 'enum', 'values': ['right', 'left', 'bottom', 'top']},
                'wrapper': {'type': 'enum', 'values': snippet['inline'] and ['span', 'div'] or ['div', 'span']},
            },
        })


def make_conf(eno, spec):
    conf = {}
    arg_idx = 0
    for field in spec['args'] or []:
        if arg_idx == len(eno['args']):
            break
        arg = eno['args'][arg_idx]
        match field.get('type'):
            case 'alt':
                choice = next((d for d in field['choices'] if 'pred' not in d or d['pred'](arg)), None)
                if choice:
                    conf[choice['name'] or field['name']] = arg['value']
                    arg_idx += 1
            case _:
                if 'pred' not in field or field['pred'](arg):
                    conf[field['name']] = arg['value']
                    arg_idx += 1

    for name, field in spec['attrs'].items():
        match field['type']:
            case 'enum':
                values = set(field['values'])
                conf[name] = field['values'][0]
                for token in eno['attrs']:
                    if token['value'] in values:
                        conf[name] = token['value']
                        break

    return conf
