import re
import sys

bad_newline_regex = r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n\s'
illegal_chars = '<' # detects tags


def open_srt():
    try:
        with open(filename, 'r', encoding="utf8") as f:
            f_contents = f.read()
            return f_contents
    except FileNotFoundError:
        print('\nFile not valid or does not exist, please try again...')
        main()

def find_wrong_newline():
    global filename
    filename = input('\nInsert full file name or "exit": ')
    if filename == 'exit':
        sys.exit('\nterminated by user')
    pattern = re.compile(bad_newline_regex)
    matches = pattern.findall(open_srt())
    print('________________________________________________\n')
    print(filename)
    print(f'\nNumber of newline errors: {len(matches)}\n')
    for item in matches:
        print(item)

def contains_illegal_chars():
    if illegal_chars in open_srt():
        print(f'contains: {illegal_chars}')
    else:
        print(f'does not contain: {illegal_chars}')
        print('________________________________________________')

def main():
    while True:
        find_wrong_newline()
        contains_illegal_chars()

if __name__ == '__main__':
    main()
