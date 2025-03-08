import json

from fme.query.handlers.base import Handler

from .db import Entry


class QueryHandler(Handler):

    key = 'math-search'

    def init(self):
        pass

    def handle(self, req, **_):
        match req.get('type'):
            case 'stat':
                return self.stat()
            case 'samples':
                return self.samples()

    def stat(self):
        return {
            'n_defs': Entry.select().where(Entry.type == 'definition').count(),
            'n_thes': Entry.select().where(Entry.type == 'theorem').count(),
        }

    def samples(self):
        return [{
            'name': d.name,
            'content': json.loads(d.content),
        } for d in Entry.select().order_by(-Entry.id)]
