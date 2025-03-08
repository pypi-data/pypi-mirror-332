import eno
from .. import markdown

from .mistune_parse import parse as mistune_parse
from .marko_parse import parse as marko_parse


def test_get_markdown_parser():
    assert markdown.get_markdown_parser() == marko_parse

    eno.config(markdown_parser = 'mistune')
    assert markdown.get_markdown_parser() == mistune_parse

    eno.config(markdown_parser = 'invalid')
    assert markdown.get_markdown_parser() == marko_parse


def test_all_cases():
    for parser_name, parse in [
            ('marko', marko_parse),
            ('mistune', mistune_parse),
    ]:
        for testcase in test_cases:
            text = testcase['text']
            exp = testcase['exp']
            got = parse(text)
            if got != exp:
                print(testcase['name'], parser_name)
                print(repr(text))
                print('exp', exp)
                print('got', got)
                assert False


paragraph_subcases = [
    {
        'name': 'paragraph line break',
        'text': 'hello\nworld',
        'exp': [
            {
                'type': 'paragraph',
                'tokens': [
                    {'type': 'text', 'text': 'hello'},
                    {'type': 'br'},
                    {'type': 'text', 'text': 'world'},
                ],
            },
        ],
    },
    {
        'name': 'paragraph line break',
        'text': 'hello\nworld\n',
        'exp': [{
            'type': 'paragraph',
            'tokens': [
                {'type': 'text', 'text': 'hello'},
                {'type': 'br'},
                {'type': 'text', 'text': 'world'},
            ],
        }],
    },
]
test_cases = [
    {
        'name': 'paragraph',
        'text': 'hello world',
        'exp': [{
            'type': 'paragraph',
            'tokens': [
                {'type': 'text', 'text': 'hello world'},
            ],
        }],
    },
    *paragraph_subcases,
    {
        'name': 'blank line separate paragraphs',
        'text': 'hello\n\nworld',
        'exp': [
            {
                'type': 'paragraph',
                'tokens': [
                    {'type': 'text', 'text': 'hello'},
                ],
            },
            {
                'type': 'paragraph',
                'tokens': [
                    {'type': 'text', 'text': 'world'},
                ],
            }
        ],
    },
]
