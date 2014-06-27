from pprint import pprint
from symbol import Symbol

def Eval(item, env):
    pprint('Evaluating: %s' %item)
    pprint('Environment is: %s' %env)
    if isinstance(item, Symbol):
        print("%s is a Symbol" %item)
        return value_of_symbol(item, env)
    elif isinstance(item, list):
        print('%s is a list' %item)
        return eval_list(item, list)
    else:
        print('%s is a literal' %item)
        return item

def eval_list(item, env):
    print("Evaluating a list")


def value_of_symbol(symbol, env):
    return env.find_symbol(symbol)
