
def Loop(f):
    while True:
        f()

def Print(result):
    print(result)


def Eval(code):
    return 'evaluated %s' %code

def Read(prompt):
    return raw_input(prompt)


if __name__ == '__main__':
    while True:
        Print(Eval(Read('> ')))
