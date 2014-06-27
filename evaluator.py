from pprint import pprint
from symbol import Symbol

def Eval(item, env):
    if isinstance(item, Symbol):
        return value_of_symbol(item, env)
    elif isinstance(item, list):
        return eval_list(item, env)
    else:
        return item


def eval_list(items, env):
        exps = [Eval(item, env) for item in items]
        proc = exps.pop(0)
        return proc(*exps)


def value_of_symbol(symbol, env):
    return env.find_symbol(symbol)
