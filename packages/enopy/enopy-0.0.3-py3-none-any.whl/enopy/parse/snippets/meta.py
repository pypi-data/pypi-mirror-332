from fans.logger import get_logger

from .base import Impl
from .templates import type_to_template_impl, base_impl


logger = get_logger(__name__)


class Meta(Impl):

    yaml = True

    def parse(self, snippet, context):
        data = snippet['data']
        template = data.get('template')
        if template:
            template_impl = type_to_template_impl.get(template.get('type'))
            if template_impl:
                context['post_process'].append(
                    (template_impl.process, data)
                )
            else:
                context['post_process'].append(
                    (base_impl.process, data)
                )
                logger.warn(f'Unknown eno meta template: {template.get("type")}')
