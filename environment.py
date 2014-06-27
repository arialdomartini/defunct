class Environment(dict):
    def __init__(self, parms=()):
        self.update(parms)
    

    def add_commands(self, commands):
        self.update(commands)


    def find_symbol(self, symbol):
        if symbol.get_value() in self:
            return self[symbol.get_value()]
