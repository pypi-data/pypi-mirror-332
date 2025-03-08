from .base import base_impl
from .novel import novel
#from .math_search import math_search


type_to_template_impl = {
    'novel': novel,
    'novella': novel,
    #'math-search': math_search,
}
