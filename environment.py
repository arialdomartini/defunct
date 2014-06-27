class Environment(dict):
    def __init__(self, parms=()):
        self.update(parms)
    

    def add_commands(self, commands):
        self.update(commands)
