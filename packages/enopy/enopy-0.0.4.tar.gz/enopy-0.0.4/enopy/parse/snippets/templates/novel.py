import re
import itertools

from enopy.parse.utils import get_text
from .base import Base


class Novel(Base):
    """
    Novel content should have:
        - heading (title)
        - paragraphs (content)
        - heading (end of content)

    Available commands:

        # group sections
        {beg-sec <sec_name>}
        {end-sec <sec_name>}

        # group paragraphs
        {beg-par <sec_name>}
        {end-par <sec_name>}
    """

    def process(self, eno, data):
        template = data['template']
        paragraphs = []
        sections = []
        groups = {}
        parags = {} # paragraph groups
        stat = {}
        novel = {
            'heading': '',
            'sections': sections,
            'version': template.get('version') or 'v1.0',
        }

        cur = eno['tokens'][0]

        # descend into blocks
        parent = cur
        while True:
            if cur.get('block_start'):
                cur = parent
                break
            elif 'tokens' in cur:
                parent = cur
                cur = cur['tokens'][0]

        # find heading
        pres = []
        heading = None
        for i, token in enumerate(cur['tokens']):
            if token['type'] == 'heading':
                heading = get_text(token).strip('《').strip('》')
                break
            else:
                pres.append(token)

        if not heading:
            return

        novel['heading'] = heading
        novel['pres'] = pres

        # find paragraphs
        for token in cur['tokens'][i + 1:]:
            match token['type']:
                case 'paragraph':
                    text = get_text(token)
                    matc = section_regex.match(text)
                    type = token['tokens'][0]['type']
                    if matc and type not in ['em', 'strong']:
                        order = matc.group('order')
                        title = matc.group('title')
                        meta = matc.group('meta')
                        sections.append({
                            'order': int(order, 10),
                            'order_str': order,
                            'title': title,
                            'meta': meta,
                            'paragraphs': [],
                        })
                    else:
                        if type == 'em':
                            style = {'fontStyle': 'italic'}
                        elif type == 'strong':
                            style = {'fontWeight': 'bold'}
                        else:
                            style = {}
                        para = {
                            'text': text,
                            'nchars': len(text),
                            'style': style,
                        }
                        paragraphs.append(para)
                        if sections:
                            sections[-1]['paragraphs'].append(para)
                case 'eno-cmd':
                    for cmd in token['cmds']:
                        match cmd['type']:
                            case 'beg-sec':
                                name = cmd['args'][0]
                                groups[name] = {
                                    'type': 'section_group',
                                    'subtype': 'linear',
                                    'name': name,
                                    'sections': [{'index': len(sections)}],
                                }
                            case 'end-sec':
                                name = cmd['args'][0]
                                group = groups[name]
                                _sections = group['sections']
                                beg = _sections[0]['index']
                                end = len(sections)
                                _sections[:] = [{'index': i} for i in range(beg, end)]
                            case 'beg-par':
                                names = cmd['args']
                                for name in names:
                                    if name not in parags:
                                        parags[name] = {
                                            'type': 'paragraph_groups',
                                            'name': name,
                                            'slices': [],
                                        }
                                    parags[name]['slices'].append({'beg': len(paragraphs)})
                            case 'end-par':
                                names = cmd['args']
                                for name in names:
                                    parags[name]['slices'][-1]['end'] = len(paragraphs)
                case 'heading':
                    break

        # single section novel
        if not sections:
            sections.append({
                'order': None,
                'title': None,
                'meta': None,
                'paragraphs': paragraphs,
            })

        # stat sections
        for section in sections:
            section['nchars'] = sum(p['nchars'] for p in section['paragraphs'])
        stat_text(sections)

        # stat novel
        novel['nchars'] = sum(d['nchars'] for d in sections)

        # finalize sections
        for section in sections:
            section['perc'] = section['nchars'] / novel['nchars']

        # finalize groups
        tree_by_name(groups)
        novel['groups'] = groups = list(groups.values())
        for group in groups:
            stat_group(group, sections)

        # finalize paragraph groups
        for parag in list(parags.values()):
            slices = parag['slices']
            if 'end' not in slices[-1]:
                slices[-1]['end'] = len(paragraphs)
            for slic in slices:
                beg, end = slic['beg'], slic['end']
                paras = paragraphs[beg:end]
                slic['nchars'] = sum(d['nchars'] for d in paras)
            parag['nchars'] = sum(d['nchars'] for d in slices)
        tree_by_name(parags)
        for parag in parags.values():
            stat_parag(parag)
        novel['parags'] = list(parags.values())

        # finalize eno
        eno['template'] = {
            'type': 'novel',
            'data': novel,
        }
        eno['meta'] = data


def stat_text(sections):
    paragraphs = itertools.chain(*[section['paragraphs'] for section in sections])
    stmts = []
    parts = []
    for para in paragraphs:
        text = para['text']
        for stmt in re.split('[。？！]', text):
            if stmt.strip():
                stmts.append(stmt)
                for part in re.split('[，]', stmt):
                    parts.append(part)
                    #print(part)
                #print(repr(stmt))
    stmt_counts = [len(d) for d in stmts]
    part_counts = [len(d) for d in parts]
    for name, arr in [('句子', stmt_counts), ('短语', part_counts)]:
        avg = sum(arr) / len(arr)
        ma = max(arr)
        mi = min(arr)
        #print(f'{name} avg={avg:.2f} max={ma} min={mi}')


def trans_name(name):
    return builtin_name_mapping.get(name) or name


def tree_by_name(nodes):
    for node in list(nodes.values()):
        del nodes[node['name']]
        node['name'] = trans_name(node['name'])
        nodes[node['name']] = node

        name = node['name']
        if '.' in name:
            parts = name.split('.')
            del nodes[name]
            name = node['name'] = parts[-1]
            cur = node
            for part in reversed(parts[:-1]):
                if part not in nodes:
                    nodes[part] = {'name': part, 'children': []}
                nodes[part]['children'].append(cur)
                cur = nodes[part]


def stat_parag(parag):
    if 'children' in parag:
        for child in parag['children']:
            stat_parag(child)
        parag['nchars'] = sum(d['nchars'] for d in parag['children'])
        for child in parag['children']:
            child['perc'] = child['nchars'] / parag['nchars']

        if parag['name'] in ('人物',):
            parag['children'] = sorted(
                parag['children'],
                key = lambda d: d['nchars'],
                reverse = True,
            )


def stat_group(group, sections):
    if 'children' in group:
        for child in group['children']:
            stat_group(child, sections)
        group['nchars'] = sum(d['nchars'] for d in group['children'])
        for child in group['children']:
            child['perc'] = child['nchars'] / group['nchars']
    else:
        group['nchars'] = sum(sections[d['index']]['nchars'] for d in group['sections'])


section_regex = re.compile(r'^(?P<order>\d+)(( (?P<title>[^{]+))?( (?P<meta>\{[^{]+\}))?)?$')
builtin_name_mapping = {
    '.intro':       '起承转合.启',
    '.follow':      '起承转合.承',
    '.trans':       '起承转合.转',
    '.concl':       '起承转合.合',
    '.conclu':      '起承转合.合',
}

novel = Novel()
