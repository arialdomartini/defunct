def Read(prompt):
    return parse(raw_input(prompt))


def parse(source_code):
    return parse_ats(to_ats(source_code))


def parse_ats(ats):
    return ats

def to_ats(source_code):
    return tokenize(source_code)


def tokenize(source_code):
    replacements = (
        ( '(',  ' ( '), 
        ( ')' , ' ) ')
    )
    expanded_code = reduce(lambda a, kv: a.replace(*kv), replacements, source_code)
    return expanded_code.split()


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
