from pprint import pprint
from symbol import Symbol

def Eval(x, env):
    pprint('Evaluating: %s' %x)
    if isinstance(x, Symbol):
        print("%s is a Symbol" %x)
    elif isinstance(x, list):
        print('%s is a list' %x)
    else:
        print('%s is a literal' %x)
