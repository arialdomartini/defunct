def Read(prompt):
    return raw_input(prompt)


def Eval(code):
    return 'evaluated %s' %code


def Print(result):
    print(result)


def Loop(f):
    while True:
        f()


if __name__ == '__main__':
    Loop(lambda: Print(Eval(Read('> '))))
