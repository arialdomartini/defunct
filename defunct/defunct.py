import sure

def tokenize(source):
    return source.replace('(',' ( ').replace(')',' ) ').split()

