from .base import Impl


class Use(Impl):

    def parse(self, snippet, context):
        snippet['path'] = snippet['args'][0]['value']
