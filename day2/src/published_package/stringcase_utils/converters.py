def to_snake_case(text):
    return ''.join(['_' + i.lower() if i.isupper() else i for i in text]).lstrip('_')

def to_camel_case(text):
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
