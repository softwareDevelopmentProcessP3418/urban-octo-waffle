from sys import argv, stderr
from readchar import readchar


class State:
    array = [0]
    ptr = 0

    def reset(self):
        self.array = [0]
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

    def print_char(self):
        print(chr(self.array[self.ptr]), end="")

    def get_char(self):
        self.array[self.ptr] = ord(readchar())


def get_action(char):
    switcher = {
        '>': State.move_ptr_right,
        '<': State.move_ptr_left,
        '+': State.increment_current_cell,
        '-': State.decrement_current_cell,
        '.': State.print_char,
        ',': State.get_char,
        '[': None,
        ']': None,
        '!': State.reset
    }
    action = switcher.get(char, None)
    if action is None:
        raise SyntaxError("Symbol '{}' is not part of Brainfuck language".format(char))
    return action


def main():
    filename = argv[1]
    state = State()
    try:
        with open(filename) as f:
            for line in f:
                for c in line:
                    get_action(c)(state)
    except SyntaxError as e:
        print(e.msg, file=stderr)
    except FileNotFoundError as e:
        print("{}: {}".format(e.strerror, e.filename), file=stderr)


if __name__ == '__main__':
    main()
