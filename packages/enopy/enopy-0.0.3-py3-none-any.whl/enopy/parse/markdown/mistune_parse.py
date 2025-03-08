import mistune


markdown = mistune.create_markdown(renderer = 'ast', hard_wrap = True)


def parse(text):
    blocks = markdown(text)
    return [make_token(block) for block in blocks]


def make_token(token):
    children = token.get('children')
    if children:
        tokens = [make_token(d) for d in children]
    else:
        tokens = None

    match token['type']:
        case 'paragraph':
            return {
                'type': 'paragraph',
                'tokens': tokens,
            }
        case 'linebreak':
            return {
                'type': 'br',
            }
        case _:
            return token
