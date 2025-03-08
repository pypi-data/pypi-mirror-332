from .base import Impl


class Img(Impl):

    def parse(self, snippet, context):
        args = snippet['args']
        snippet['src'] = args[0]['value']
        if len(args) > 1:
            side = args[1]['value']
            if isinstance(side, str) and side[0] in 'hx':
                snippet['height'] = int(side[1:])
            else:
                try:
                    snippet['width'] = int(side)
                except ValueError:
                    snippet['show'] = side
