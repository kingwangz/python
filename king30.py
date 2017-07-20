from time import ctime


def tsfunc(func):
    def wrappedFunc():
        print('{} {} called'.format(ctime(), func.__name__))
        return func()

    return wrappedFunc


@tsfunc
def foo():
    pass


def foo():
    global m
    m = 3


def bar():
    global n
    n = 4


def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]

    return incr()


foo()
bar()
print(m + n)
s = map((lambda x: x + 2), [0, 1, 2, 3, 4, 5])
print(s)
b = lambda *z: z
print(b(88))
print(counter(3))
