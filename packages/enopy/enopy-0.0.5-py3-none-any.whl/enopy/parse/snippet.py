import yaml
import lark
from lark.visitors import v_args

from .snippets import type_to_snippet_impl


grammar = r'''
start: type args? ("|" attrs)?

type: NAME

args: arg arg*
arg: value_arg | key_value_arg
value_arg: value
key_value_arg: key ":" value

attrs: args

key: NAME
value: number
    | name_value
    | path
    | quoted_string

name_value: NAME
path: PATH
quoted_string: ESCAPED_STRING
number: NUMBER

NAME: /\w(\w|[.-])+/
PATH: /\.\/[^ ]*|\.|\/[^ ]*/

%import common.SIGNED_NUMBER    -> NUMBER
%import common.WS
%import common.ESCAPED_STRING
%ignore WS
'''


@v_args(inline = True)
class Transformer(lark.Transformer):

    def start(self, type, args = None, attrs = None):
        return {
            'type': type,
            'args': args or [],
            'attrs': attrs or [],
        }

    def type(self, token):
        return token.value

    def args(self, *args):
        return list(args)

    def attrs(self, args):
        return args

    arg = lambda _, d: d
    value_arg = lambda _, d: d
    value = lambda _, d: d

    def name_value(self, token):
        return {'type': 'string', 'value': token.value}

    def path(self, path):
        return {'type': 'path', 'value': path.value}

    def quoted_string(self, token):
        return {'type': 'string', 'quoted': '"', 'value': token.value.strip('"')}

    def number(self, token):
        try:
            value = int(token.value)
        except ValueError:
            value = float(token.value)
        return {'type': 'number', 'value': value}


def parse_lang(text):
    return transformer.transform(parser.parse(text))


def parse_snippet(lang, text = None, data = None, context = None):
    snippet = parse_lang(lang)
    context = context or {}
    inline = context.get('inline')
    if inline is None:
        inline = text is None

    snippet['context'] = context
    snippet['text'] = text.strip()
    snippet['inline'] = inline
    snippet['data'] = data

    impl = type_to_snippet_impl.get(snippet['type'])
    if impl:
        if snippet['data'] is None:
            if text and impl.yaml:
                snippet['data'] = yaml.safe_load(text)

        impl.parse(snippet, context)

    snippet['data'] = snippet['data'] or {}

    return snippet


def test():
    for text, expected in [
            ('foo', {'type': 'foo', 'args': [], 'attrs': []}),

            # path
            ('eno.js .', {
                'type': 'eno.js', 'args': [{'type': 'path', 'value': '.'}], 'attrs': [],
            }),
            ('eno.js ./t.js', {
                'type': 'eno.js', 'args': [{'type': 'path', 'value': './t.js'}], 'attrs': []
            }),
    ]:
        res = parse_lang(text)
        if res != expected:
            print('ERROR')
            print(res, '!=', expected)


parser = lark.Lark(grammar)
transformer = Transformer()


if __name__ == '__main__':
    test()
