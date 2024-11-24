# This script converts entered characters into ASCII code
# It parses ASCII styled chars from txt files and 
# creates a char dict to convert and print the inputted text.
# Can set the style of the ascii output.
# Can write the output to file.
# Can set a color of the text.

import argparse
import re
from typing import Optional
from collections.abc import Iterable

COLORS_DICT = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[0m',
}

# create a dict of char: ascii
def create_dict(ascii_raw: str, int_repr: Iterable, color: Optional[str] = None):
    ascii_dict = {}
    start_index = 0
    for i in int_repr:
        end_index = start_index + 9
        letter = [line.rstrip('\n') for line in ascii_raw[start_index + 1:end_index]]
        ascii_dict[chr(i)] = letter
        start_index = end_index
    if color:
        for color in COLORS_DICT:
            ascii_dict[color] = [COLORS_DICT[color]] * 8
    return ascii_dict

def convert_char_to_ascii(word: str, ascii_dict: dict, color: Optional[str] = None):
    ascii_text_list = [ascii_dict[letter] for letter in word]
    return ascii_text_list

def apply_color(word: str, color: Optional[str], letters=None):
    color_code = COLORS_DICT.get(color, COLORS_DICT["reset"])
    reset_code = COLORS_DICT["reset"]

    if letters:
        # Apply color only to the specified letters
        pattern = f"[{re.escape(letters)}]"
        return re.sub(pattern, lambda m: f"{color_code}{m.group(0)}{reset_code}", word)
    else:
        # Apply color to the entire text
        return f"{color_code}{word}{reset_code}"

def parse_color_flag(flag):
    match = re.match(r"--color=([^ ]+)(?: (.+))?", flag)
    if match:
        color = match.group(1)
        letters_to_color = match.group(2)
        if color in COLORS_DICT:
            return color, letters_to_color
    return None, None

def join_chars(ascii_text_list):
    ascii_text = '\n'.join([''.join(lines) for lines in zip(*ascii_text_list)])
    return ascii_text

def main():

    # create and parse arguments
    parser = argparse.ArgumentParser(
        description="Process a message with a specified ASCII style."
    )
    parser.add_argument(
        "input_text", 
        type=str, 
        help="The input text to be processed."
    )
    parser.add_argument(
        "style", 
        type=str, 
        nargs="?",
        default='standard',
        choices=["standard", "shadow", "thinkertoy"],
        help="The style to apply to the input text."
    )
    parser.add_argument(
        "--output",
        type=str,
        help="File name to write."
    )
    parser.add_argument(
        "--color",
        type=str,
        nargs="+",
        help='Apply color to the text.'
    )
    args = parser.parse_args()    

    # handle newlines
    input_text_list = args.input_text.split('\\n')

    # read style file
    with open(f'{args.style}.txt', 'r') as f:
        ascii_raw = f.readlines()

    # convert string to ascii
    ascii_dict = create_dict(ascii_raw=ascii_raw, int_repr=range(32, 128), color=args.color)
    result_list = []
    for word in input_text_list:
        ascii_text_list = convert_char_to_ascii(word=word, ascii_dict=ascii_dict, color=args.color)
        ascii_text = join_chars(ascii_text_list)
        print(ascii_text)
        result_list.append(ascii_text)

    if args.output:
        # write to the file
        with open(args.output, 'w') as file:
            file.write('\n'.join(result_list))

if __name__ == '__main__':
    main()