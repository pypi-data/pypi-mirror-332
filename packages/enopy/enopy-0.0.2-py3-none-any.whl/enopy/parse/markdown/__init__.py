"""
Parse markdown text as a list of block tokens.

Each block token might have sub inline tokens.

Block tokens:

    {
        'type': 'paragraph',
    }

    {
        'type': 'code',
    }

Inline tokens:

    {
        'type':  'text',
    }

    ...
"""
from fans.logger import get_logger

from eno.env import env


logger = get_logger(__name__)


def parse_markdown(text):
    parse = get_markdown_parser()
    return parse(text)


def get_markdown_parser():
    match env.markdown_parser:
        case 'mistune':
            from .mistune_parse import parse as mistune_parse
            return mistune_parse
        case 'marko':
            from .marko_parse import parse as marko_parse
            return marko_parse
        case _:
            logger.warning(
                f'unknown markdown parser "{env.markdown_parser}", '
                f'using {env.default_markdown_parser}')
            from .marko_parse import parse as marko_parse
            return marko_parse
