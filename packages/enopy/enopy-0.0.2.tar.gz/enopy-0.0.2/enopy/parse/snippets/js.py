from eno.apps import apps
from .base import Impl


apps_prefix = 'src/apps/enojs'


class Js(Impl):

    loaded = False

    def parse(self, snippet, context):
        if not self.loaded:
            from fme.apps.auto_gen_eno_apps import key_to_comp
            apps.update({
                **apps,
                **key_to_comp,
            })
            self.loaded = True

        args = snippet['args']
        if args and args[0]['type'] == 'path':
            parse_include(snippet, context)
        else:
            parse_inline(snippet, context)


def parse_include(snippet, context):
    path = context['path']
    dire = path.parent
    name = path.stem

    keys = [str(apps_prefix / (dire / p).relative_to('/')) for p in [
        snippet['args'] and snippet['args'][0]['value'], # eno.js ./foo.js
        f'{name}.js', # bar.eno => bar.js
        'main.js',
        'index.js',
    ]]
    print(keys)
    keys = [d for d in keys if apps.get(d)]
    key = keys[0] # TODO: set snippet error and render accordingly
    entry = snippet['args'] and len(snippet['args']) > 1 and snippet['args'][1]['value']
    snippet['entry'] = entry or 'default'
    snippet['dir'] = str('/' / dire)
    snippet['name'] = name
    snippet['key'] = key
    snippet['include'] = True # frontend depend on this attr


def parse_inline(snippet, context):
    snippet['result'] = {}
