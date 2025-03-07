from .database import bible_data
from .citations import parse_multiple_citations
from .reader import read_citations, read_book

def read_bible(book_name, citation=None):
    book = read_book(bible_data, book_name)
    if not citation:
        return { book_name: book }

    return {
        book_name: read_citations(
            book,
            parse_multiple_citations(citation)
        )
    }
