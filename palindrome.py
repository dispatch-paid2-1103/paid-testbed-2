def is_palindrome(text: str) -> bool:
    """Return True if ``text`` reads the same forwards and backwards.

    Case, spaces and punctuation are ignored; only letters and digits are
    compared. An empty string (or one with no letters or digits) is a
    palindrome.
    """
    cleaned = [c.lower() for c in text if c.isalnum()]
    return cleaned == cleaned[::-1]
