import pytest


@pytest.fixture(scope="session")
def library():
    print("\nSETUP module fixture-1")
    data_books = ["Преступление и наказание", "Отцы и дети", "Гордость и предубеждение"]
    yield data_books
    print("\nTEARDOWN module fixture-1")


@pytest.fixture(scope="session")
def new_book():
    print("\nSETUP module fixture-2")
    book = "Золушка"
    yield book
    print("\nTEARDOWN module fixture-2")
