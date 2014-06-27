class Symbol(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'Symbol: %s' % self.value

    def get_value(self):
        return self.value
