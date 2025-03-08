import json

import yaml

from eno.apps import conf as name_to_conf
from .base import Impl


class App(Impl):

    def parse(self, snippet, context):
        name = snippet['args'][0]['value']
        conf = name_to_conf.get(name)
        if not conf or not conf.get('raw'):
            snippet['data'] = parse_data(snippet.get('text') or '')
            # TODO: remove
            if name == 'timeline':
                data = snippet['data']
                convert_date(data)


def parse_data(text):
    if text.startswith('{'):
        return json.loads(text)
    else:
        return yaml.safe_load(text)

# TODO: remove
import datetime
def convert_date(root):
    for key, value in root.items():
        if isinstance(value, datetime.date):
            root[key] = datetime.datetime.combine(value, datetime.datetime.min.time()).isoformat() + '.000Z'
        elif isinstance(value, list):
            value = [convert_date(c) for c in value]
        elif isinstance(value, dict):
            for k, v in value.items():
                value[k] = convert_date(v)
