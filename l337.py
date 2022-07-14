_L337_LETTER_REPLACEMENTS = {
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
    's': '5',
    't': '7',
}


def get_l337_char(char: str) -> str:
    if char.lower() not in _L337_LETTER_REPLACEMENTS.keys():
        return char

    return _L337_LETTER_REPLACEMENTS[char.lower()]


def leetify(english_str: str) -> str:
    return "".join([get_l337_char(c) for c in english_str])
