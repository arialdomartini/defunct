from parser import parse

def Read(prompt):
    return parse(raw_input(prompt))



def Eval(code):
    return code


from pprint import pprint
def Print(result):
    pprint(result)


def Loop(f):
    while True:
        f()


if __name__ == '__main__':
    Loop(lambda: Print(Eval(Read('> '))))
