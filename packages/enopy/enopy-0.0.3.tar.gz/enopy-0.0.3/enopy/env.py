import traceback
from pathlib import PurePosixPath

import yaml


class Env:

    def __init__(self):
        self.root = None
        self.default_markdown_parser = 'marko'
        self.markdown_parser = self.default_markdown_parser

        self._conf = None

    def ensure_conf(self):
        return self.conf

    @property
    def conf(self):
        if self._conf is None:
            path = self.root / 'conf.yaml'
            if path.exists():
                try:
                    with path.open() as f:
                        self._conf = yaml.safe_load(f)
                except:
                    logger.warning(traceback.format_exc())
                    self._conf = {}

            aliases = {}
            for alias in self._conf.get('alias', []):
                try:
                    if isinstance(alias, str):
                        src, dst = [d.strip() for d in alias.split('>')]
                    elif isinstance(alias, dict):
                        src, dst = alias['from'], alias['to']
                    else:
                        src, dst = None, None

                    assert src.startswith('/') and dst.startswith('/')

                    src = PurePosixPath(src).relative_to('/')
                    dst = PurePosixPath(dst).relative_to('/')
                    aliases[src] = dst
                except:
                    logger.warning(traceback.format_exc())
            self.aliases = aliases

        return self._conf


env = Env()
