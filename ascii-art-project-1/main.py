# This script converts entered characters into ASCII code
# It parses ASCII styled chars from txt files and 
# creates a char dict to convert and print the inputted text.

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

def convert_to_ascii(input_text, ascii_dict):
    ascii_text_list = [ascii_dict[letter] for letter in input_text]
    return ascii_text_list

def join_chars(ascii_text_list):
    print
    for lines in zip(ascii_text_list):
        print(lines)
    ascii_text = [''.join(lines) for lines in zip(ascii_text_list)]
    return ascii_text

def main():
    # read ascii file
    with open('standard.txt', 'r') as f:
        ascii_raw = f.readlines()
    
    ascii_dict = create_dict(ascii_raw)
    ascii_text_list = convert_to_ascii('abc def xyz !~^', ascii_dict)
    join_chars(ascii_text_list)

if __name__ == '__main__':
    main()