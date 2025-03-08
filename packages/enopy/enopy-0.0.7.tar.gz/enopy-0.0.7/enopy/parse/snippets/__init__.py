from .js import Js
from .py import Py
from .meta import Meta
from .app import App
from .table import Table
from .pop import Pop
from .use import Use
from .tabs import Tabs
from .img import Img


type_to_snippet_impl = {
    'eno.js': Js(),
    'eno.py': Py(),
    'eno.app': App(),
    'eno.meta': Meta(),
    'eno.table': Table(),
    'eno.pop': Pop(),
    'eno.use': Use(),
    'eno.tabs': Tabs(),
    'eno.img': Img(),
}
