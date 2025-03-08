from pathlib import Path

from .env import env
from .router import app as router


def config(
        root: str = None,
        markdown_parser: str = None,
):
    if root:
        env.root = Path(root)

    if markdown_parser:
        env.markdown_parser = markdown_parser


def get_router(root: str = None):
    if root:
        config(root = root)
    if not env.root:
        raise RuntimeError(f'eno root not set, cannot get router')
    return router
