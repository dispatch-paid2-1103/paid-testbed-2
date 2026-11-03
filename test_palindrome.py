import pytest

from palindrome import is_palindrome


@pytest.mark.parametrize(
    "text",
    [
        "",
        "a",
        "racecar",
        "Racecar",
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "   ",
        "!!!",
        "12321",
    ],
)
def test_palindromes(text):
    assert is_palindrome(text) is True


@pytest.mark.parametrize(
    "text",
    [
        "hello",
        "12345",
        "ab",
    ],
)
def test_non_palindromes(text):
    assert is_palindrome(text) is False
