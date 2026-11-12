import pytest


@pytest.mark.for3_3
@pytest.mark.parametrize(
    "word, expected_length",
    [("QA", 2), ("Python", 6), ("", 0), ("Автоматизация", 13)],
    ids=["short_word", "average_word", "empty_string", "long_word"],
)
def test_word(word, expected_length):
    assert len(word) == expected_length
