from sys import argv


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


def get_action(char):
    switcher = {
        '>': State.move_ptr_right,
        '<': State.move_ptr_left,
        '+': State.increment_current_cell,
        '-': State.decrement_current_cell,
        '.': None,
        ',': None,
        '[': None,
        ']': None,
        '!': State.reset
    }
    action = switcher.get(char, None)
    if action is None:
        raise IOError('Symbol \'' + char + '\' is not the part of a Brainfuck language')
    return action


def main():
    filename = argv[1]
    with open(filename) as f:
        for line in f:
            for c in line:
                pass


if __name__ == '__main__':
    main()
