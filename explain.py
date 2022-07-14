from rich.prompt import Prompt
from rich import print

from base_64 import SIX_BIT_MAPPING
from strings import to_chunks


def explain_base64(input_string: str):
    binary_data = ''.join([bin(ord(char)) for char in input_string]).replace('b', '')
    char_bytes = to_chunks(binary_data, chunk_size=8)
    base64_six_bit_array = to_chunks(binary_data, chunk_size=6)

    original_lines = ''
    original_str = ''
    base64_lines = ''
    base64_str = ''
    bytes = ''

    for i, six_bits in enumerate(base64_six_bit_array):
        try:
            char_byte = char_bytes[i]
        except IndexError:
            char_byte = six_bits + '??'

        base64_char = SIX_BIT_MAPPING[six_bits]
        base64_str += f'   [bold]{base64_char}[/bold]  '
        base64_lines += '┌────┐'

        if '??' not in char_byte:
            char_from_byte = chr(int(char_byte, 2))
            bytes += f'[bold white]{char_byte[:-2]}[/bold white][cyan]{char_byte[-2:]}[/cyan]'
            original_lines += '[cyan]└──────┘[/cyan]'
            original_str += f'    [cyan]{char_from_byte}[/cyan]   '
        else:
            base64_str += f' [bold]pad.[/bold] '
            base64_lines += '┌────┐'
            bytes += f'[bold white]{six_bits}[/bold white]'

    print(base64_str)
    print(base64_lines)
    print(bytes)
    print(original_lines)
    print(original_str)


if __name__ == '__main__':
    input_base64_string = Prompt.ask('Enter a string to convert to base64')

    explain_base64(input_base64_string)
