def get_text(token):
    match token['type']:
        case 'text':
            return token['text']
        case 'br':
            return '\n'
    if 'text' in token:
        return token['text']
    if 'tokens' in token:
        return ''.join([get_text(d) for d in token['tokens']])
    return ''

