def read_book(bible, book):
    return bible[book]

def read_verses(chapter, verses):
    response = []
    for verse in verses:
        if isinstance(verse, tuple):
            start, end = verse
            response.append({
                i: chapter[i]
                for i in range(start, end + 1)
            })
        else:
            response.append({ verse: chapter[verse] })
    return response

def read_citation(book, citation):
    if isinstance(citation['chapters'], tuple):
        start, end = citation['chapters']
        return {
            i: book[i]
            for i in range(start, end + 1)
        }
    else:
        chapter = book[citation['chapters']]
        return {
            citation['chapters']: (
                read_verses(chapter, citation['verses'])
                if 'verses' in citation
                else chapter
            )
        }

def read_citations(book, citations):
    return [read_citation(book, citation) for citation in citations]
