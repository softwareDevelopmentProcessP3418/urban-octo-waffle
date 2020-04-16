from sys import argv


def handle(char):
    print(char)


def main():
    filename = argv[1]
    with open(filename) as f:
        for line in f:
            for c in line:
                handle(c)


if __name__ == '__main__':
    main()
