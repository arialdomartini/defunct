from pprint import pprint
from parser import parse
from evaluator import Eval


def Read(prompt):
    return parse(raw_input(prompt))


def Print(result):
    pprint(result)


def Loop(f):
    while True:
        f()


if __name__ == '__main__':
    try:
        Loop(lambda: Print(Eval(Read('> '))))
    except EOFError:
        print('Done.')
