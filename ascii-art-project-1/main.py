# This script converts entered characters into ASCII code
# It parses ASCII styled chars from txt files and 
# creates a char dict to convert and print the inputted text.
# Can set the style of the ascii output.
# Can write the output to file.

import argparse


# create a dict of char: ascii
def create_dict(ascii_raw):
    ascii_dict = {}
    start_index = 0
    for i in range(32, 128):
        end_index = start_index + 9
        letter = [line.rstrip('\n') for line in ascii_raw[start_index + 1:end_index]]
        ascii_dict[chr(i)] = letter
        start_index = end_index
    return ascii_dict

def convert_char_to_ascii(word: str, ascii_dict: dict):
    ascii_text_list = (ascii_dict[letter] for letter in word)
    return ascii_text_list

def join_chars(ascii_text_list):
    ascii_text = '\n'.join([''.join(lines) for lines in zip(*ascii_text_list)])
    return ascii_text

def main(input_text, style, output):

    # handle newlines
    input_text_list = input_text.split('\\n')

    # read style file
    with open(f'{style}.txt', 'r') as f:
        ascii_raw = f.readlines()

    # convert string to ascii
    ascii_dict = create_dict(ascii_raw)
    result_list = []
    for word in input_text_list:
        ascii_text_list = convert_char_to_ascii(word, ascii_dict)
        ascii_text = join_chars(ascii_text_list)
        print(ascii_text)
        result_list.append(ascii_text)

    if output:
        # write to the file
        with open(output, 'w') as file:
            file.write('\n'.join(result_list))


if __name__ == '__main__':
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
    
    args = parser.parse_args()    
    main(args.input_text, args.style, args.output)