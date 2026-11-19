def normalize_whitespace(text: str) -> str:
    """Nahradí skupiny bílých znaků jednou mezerou."""
    return " ".join(text.split())
def count_words(text: str) -> int:
    """Vrátí počet slov oddělených bílými znaky."""
    return len(text.split())

def tokenize(text: str) -> list[str]:
    """Rozdělí text na malá slova bez okrajové interpunkce."""
    words = []

    for word in text.lower().split():
        word = word.strip(".,!?;:")

        if word:
            words.append(word)

    return words

def word_frequencies(text: str) -> dict[str, int]:
    """Vrátí četnosti slov bez ohledu na velikost písmen."""
    frequencies = {}

    for word in tokenize(text):
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies


def most_common_words(text: str, limit: int = 5) -> list[tuple[str, int]]:
    """Vrátí nejčastější slova a jejich počty."""
    frequencies = word_frequencies(text)

    sorted_words = sorted(
        frequencies.items(),
        key=lambda item: (-item[1], item[0])
    )

    return sorted_words[:limit]