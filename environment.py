from pprint import pprint

class Environment(dict):
    def __init__(self, parameters=(), arguments=(), outer=None):
        self.update(zip(parameters, arguments))
        self.outer = outer


    def add_commands(self, commands):
        self.update(commands)


    def find_symbol(self, symbol):
        
        pprint("Looking for symbol: '%s' with value '%s' in env: %s"
               % (symbol, symbol.get_value(), self))
        if symbol.get_value() in self:
            return self[symbol.get_value()]
        else:
            pprint("Not found. Asking outer env...")
            return self.outer.find_symbol(symbol)
