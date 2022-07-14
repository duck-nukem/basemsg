_L337_LETTER_REPLACEMENTS = {
    'i': '1',
    'o': '0',
    'e': '3',
    'a': '4',
}


def get_l337_char(char: str) -> str:
    if char not in _L337_LETTER_REPLACEMENTS.keys():
        return char

    return _L337_LETTER_REPLACEMENTS[char]


def leetify(english_str: str) -> str:
    return "".join([get_l337_char(c) for c in english_str])
