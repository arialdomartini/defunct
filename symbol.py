class Symbol(object):
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return 'Symbol: %s' % self.token
