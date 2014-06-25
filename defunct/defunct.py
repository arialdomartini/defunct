def tokenize(source):
    return source.replace('(',' ( ').replace(')',' ) ').split()

