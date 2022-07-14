import sys
from time import sleep

from rich import print
from rich.prompt import Prompt

from base_64 import SIX_BIT_VALUES_BY_CHAR
from config import read_config
from strings import to_chunks, make_permutations, is_printable

_CONFIG = read_config()


def debug(*args, **kwargs):
    if _CONFIG.getboolean('main', 'debug'):
        print(*args, **kwargs)


def make_message(message: str) -> None:
    if len(message) % 4 != 0:
        print(f'Message length ({len(message)}) must be divisible by 4 without remainder')
        for message_part in to_chunks(message, chunk_size=4, add_padding=False):
            if len(message_part) != 4:
                print(f'[red]{message_part} <-- [/red]')
            else:
                print(f'[green]{message_part}[/green]')
        sys.exit(1)

    base64_blocks = to_chunks(message, chunk_size=4)
    debug(base64_blocks)
    complete_ascii_readable = ''
    complete_resolved_string = ''

    for block in base64_blocks:
        case_permutations = make_permutations(block)
        for index, permutation in enumerate(case_permutations):

            if _CONFIG.getboolean('main', 'anim8'):
                sleep(0.05)

            print(f'[green]{complete_resolved_string}[/green][yellow]{permutation}[/yellow]', end='\r')
            debug(permutation)
            ascii_block = ''
            chunk_ascii_readable = ''

            debug('\neach letter as if they were 4x6 bits in base64')
            for letter in permutation:
                ascii_block += SIX_BIT_VALUES_BY_CHAR[letter]
                debug(letter, SIX_BIT_VALUES_BY_CHAR[letter])

            debug('\nchars derived from binary as if it were 3x8 bits')
            for chunk in to_chunks(ascii_block, chunk_size=8):
                ascii_value = chr(int(chunk, 2))
                chunk_ascii_readable += ascii_value
                debug(ascii_value, chunk, 'printable:', is_printable(ascii_value))

            if is_printable(chunk_ascii_readable):
                debug(ascii_block, chunk_ascii_readable)
                complete_ascii_readable += chunk_ascii_readable
                complete_resolved_string += permutation
                break
            elif index == len(case_permutations) - 1:
                print(
                    f'[white on red]{block} does not have a valid permutation to be used :< '
                    f'Failed to convert {message}[/white on red]'
                )
                sys.exit(1)
    print(f'[green]{complete_resolved_string}[/green]')
    print(f'[bold]{complete_ascii_readable}[/bold]')


if __name__ == '__main__':
    message = Prompt.ask('State thy bidding')

    make_message(message)
