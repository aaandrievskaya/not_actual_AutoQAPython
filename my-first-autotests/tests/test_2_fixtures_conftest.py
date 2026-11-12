def test_library_is_not_empty(library):
    assert len(library) == 3


def test_add_book(library, new_book):
    library.append(new_book)
    assert "Золушка" in library


def test_library_size(library):
    assert len(library) == 4
