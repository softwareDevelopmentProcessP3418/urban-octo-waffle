from sys import argv
from enum import Enum

l = [0] * 30000
ptr = 0    

class BrainfuckSymbols(Enum):
    GREATER_THAN = '>'
    LESS_THAN = '<'
    PLUS = '+'
    MINUS = '-'
    DOT = '.'
    COMMA = ','
    OPEN_BRACKET = '['
    CLOSE_BRACKET = ']'

    @staticmethod
    def get_token(char):
        switcher = {
            BrainfuckSymbols.GREATER_THAN.value: BrainfuckSymbols.GREATER_THAN,
            BrainfuckSymbols.LESS_THAN.value: BrainfuckSymbols.LESS_THAN,
            BrainfuckSymbols.PLUS.value: BrainfuckSymbols.PLUS,
            BrainfuckSymbols.MINUS.value: BrainfuckSymbols.MINUS,
            BrainfuckSymbols.DOT.value: BrainfuckSymbols.DOT,
            BrainfuckSymbols.COMMA.value: BrainfuckSymbols.COMMA,
            BrainfuckSymbols.OPEN_BRACKET.value: BrainfuckSymbols.OPEN_BRACKET,
            BrainfuckSymbols.CLOSE_BRACKET.value: BrainfuckSymbols.CLOSE_BRACKET
        }
        token = switcher.get(char, None)
        if token is None:
            raise IOError('Error: Symbol \'' + char + '\' is not the part of a Brainfuck language')
        return token

def move_ptr_right():
    global ptr
    ptr += 1

def move_ptr_left():
    global ptr
    ptr -= 1

def main():
    filename = argv[1]
    tokenized_symbols = []
    with open(filename) as f:
        for line in f:
            for c in line:
                token = BrainfuckSymbols.get_token(c)
                tokenized_symbols.append(token) 

if __name__ == '__main__':
    main()
