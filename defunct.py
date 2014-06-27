def foo():
    print('the rest')

def loop(f):
    while True:
        f()

if __name__ == '__main__':
    loop(foo)
