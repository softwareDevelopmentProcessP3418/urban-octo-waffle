from sys import argv
from enum import Enum


class State:
    array = [0]
    ptr = 0

    def reset(self):
        self.array = [0]*3000
        self.ptr = 0

    def move_ptr_right(self):
        if (self.ptr == (len(self.array) - 1)):
            self.array.append(0)        
        self.ptr += 1

    def move_ptr_left(self):
        if (self.ptr == 0):
            self.array.insert(0, 0)
            return
        self.ptr -= 1

    def increment_current_cell(self):
        self.array[self.ptr] += 1

    def decrement_current_cell(self):
        self.array[self.ptr] -= 1


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
