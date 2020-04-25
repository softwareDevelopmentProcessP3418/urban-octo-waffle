from sys import argv
from enum import Enum


class State:
    array = [0] * 30000
    ptr = 0

    def reset(self):
        self.array = [0] * 30000
        self.ptr = 0

    def move_ptr_right(self):
        self.ptr += 1

    def move_ptr_left(self):
        self.ptr -= 1


class BrainfuckSymbols(Enum):
    GREATER_THAN = '>'
    LESS_THAN = '<'
    PLUS = '+'
    MINUS = '-'
    DOT = '.'
    COMMA = ','
    OPEN_BRACKET = '['
    CLOSE_BRACKET = ']'
    EXCLAMATION_MARK = '!'

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
            BrainfuckSymbols.CLOSE_BRACKET.value: BrainfuckSymbols.CLOSE_BRACKET,
            BrainfuckSymbols.EXCLAMATION_MARK.value: BrainfuckSymbols.EXCLAMATION_MARK
        }
        token = switcher.get(char, None)
        if token is None:
            raise IOError('Error: Symbol \'' + char + '\' is not the part of a Brainfuck language')
        return token


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
