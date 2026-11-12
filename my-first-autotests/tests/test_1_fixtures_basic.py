def test_book_not_in_library(library):
    assert "Война и мир" not in library


def test_symbol_in_new_book(new_book):
    assert "о" in new_book
