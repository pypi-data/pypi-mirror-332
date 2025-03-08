import json

import peewee

from ..base import Base

from .db import Entry, Alias


class MathSearch(Base):

    def process(self, eno, meta):
        return
        super().process(eno, meta)
        eno['endpoint'] = '/q/math-search'

        Entry.delete().execute()
        Alias.delete().execute()

        entries = []
        for block in self.iter_blocks(eno):
            if block['type'] == 'heading':
                cmd = block['text'].split(' ', 1)[0]
                entries.append({
                    'cmd': cmd,
                    'heading': block,
                    'blocks': [],
                })
            elif entries:
                entries[-1]['blocks'].append(block)

        for entry in entries:
            processor = cmd_to_processor.get(entry['cmd'])
            if processor:
                processor.process(entry)

        entries = filter(lambda d: d.get('type'), entries)
        for entry in entries:
            #print(entry['data'])
            data = entry['data']
            try:
                content = json.dumps(entry['blocks'], ensure_ascii = False)
            except :
                # TODO: handle `eno.img`
                print(entry['blocks'])
                raise
            Entry.insert(
                name = data['name'],
                type = data['type'],
                content = content,
            ).execute()


class Processor:

    type = None

    def process(self, entry):
        self.entry = entry
        entry['type'] = self.type
        data = self.make()
        if data:
            data['type'] = self.type
            data['typename'] = self.typename
            entry['data'] = data

    def make(self):
        entry = self.entry
        ret = {}
        ret.update(make_names(entry['heading']['text']))
        return ret


class Def(Processor):

    type = 'definition'
    typename = '定义'


class The(Processor):

    type = 'theorem'
    typename = '定理'


class For(Processor):

    type = 'formula'
    typename = '公式'


def make_names(s):
    s = s.split(' ', 1)[1].strip()
    parts = [d.strip() for d in s.split('-')]
    cn_names_str = parts[0]
    en_names_str = parts[1] if len(parts) > 1 else ''
    cn_names = split_names(cn_names_str)
    return {
        'name': cn_names[0],
        'cn_names': cn_names,
        'en_names': split_names(en_names_str),
    }


def split_names(s):
    return [d.strip() for d in s.split('/')]


cmd_to_processor = {
    'def': Def(),
    'the': The(),
    'for': For(),
}


math_search = MathSearch()
