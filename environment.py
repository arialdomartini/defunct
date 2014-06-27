class Environment(dict):
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.update(parms)
        self.outer = outer


    

    def add_commands(self, commands):
        self.update(commands)
        


    def find_symbol(self, symbol):
        from pprint import pprint
        pprint('Looking for symbol: %s in env: %s' %(symbol.get_value(), self))
        if symbol.get_value() in self:
            return self[symbol.get_value()]
        else:
            return self.outer.find_symbol(symbol)
