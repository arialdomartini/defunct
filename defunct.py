from pprint import pprint
from parser import parse
from environment import Environment
import lisp
from evaluator import Eval


def Read(prompt):
    return parse(raw_input(prompt))


def Print(result):
    pprint(result)


def Loop(f):
    while True:
        f()


if __name__ == '__main__':
    env = Environment(lisp.builtin_commands)

    try:
        Loop(lambda: Print(Eval(Read('> '), env)))
    except EOFError:
        print('Done.')
