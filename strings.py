import string
from itertools import product
from typing import List, Set

from l337 import leetify


def to_chunks(input_str: str, chunk_size: int, add_padding=True) -> List[str]:
    chunks = []

    for i in range(0, len(input_str), chunk_size):
        chunk = input_str[i:i + chunk_size]

        if len(chunk) < chunk_size and add_padding:
            padding = (chunk_size - len(chunk)) * '0'
            chunk += padding

        chunks.append(chunk)

    return chunks


def make_permutations(of_string: str) -> Set[str]:
    cases = zip(*[of_string, of_string.swapcase(), leetify(of_string)])
    case_permutations = ["".join(permutation) for permutation in product(*cases)]

    return set(case_permutations)


def is_printable(input_str: str) -> bool:
    printable_chars = string.digits + string.ascii_letters + string.punctuation
    return all(letter in printable_chars for letter in input_str)
