from pprint import pprint
from symbol import Symbol


def Eval(item, env):
    pprint("Evaluating %s" % item)
    if isinstance(item, Symbol):
        return value_of_symbol(item, env)
    elif isinstance(item, list):
        return eval_list(item, env)
    else:
        return item


def eval_list(items, env):
    pprint("Evaluating the list: %s" % items)
    first_element = items[0]
    pprint("First element is: %s" % first_element)
    if is_a_lambda(first_element):
        pprint("It's a lambda: %s" % items)
        (_, vars, exp) = items
        return lambda *args: Eval(exp, Env(vars, args, env))
    elif is_a_binding_definition(first_element):
        (_, binding_name, expression) = items
        env[binding_name] = Eval(expression, env)
    else:
        exps = [Eval(item, env) for item in items]
        proc = exps.pop(0)
        return proc(*exps)


def value_of_symbol(symbol, env):
    return env.find_symbol(symbol)


def is_a_lambda(element):
    return is_the_builtin_symbol(element, 'lambda')


def is_a_binding_definition(element):
    return is_the_builtin_symbol(element, 'define')


def is_the_builtin_symbol(element, symbol):
    return isinstance(element, Symbol) and element.get_value() == symbol
