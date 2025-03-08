from .base import Impl


class Py(Impl):

    def parse(self, snippet, context):
        args = snippet['args']
        if len(args) > 0:
            py_path = args[0]['value']
            if py_path == '.':
                py_path = context['path'].stem + '.py'
            snippet['path'] = context['path'].parent / py_path
