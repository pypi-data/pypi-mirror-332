def parse_possible_range(text):
    if '-' in text:
        return tuple(int(i) for i in text.split('-'))
    else:
        return int(text)

def parse_verses(text):
    return [parse_possible_range(t) for t in text.split(',')]

def parse_citation(citation):
    components = citation.split(':')
    if len(components) == 1:
        return {"chapters": parse_possible_range(components[0])}
    else:
        return {
            "chapters": int(components[0]),
            "verses": parse_verses(components[1])
        }

def parse_multiple_citations(citation):
    return [parse_citation(book) for book in citation.split(';')]
