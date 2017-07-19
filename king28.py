from time import ctime, sleep


def tsfunc(func):
    print('a')
    def wrappedFunc():
        print('{} {} called'.format(ctime(), func.__name__))
        print('c')
        return func()
    print('b')
    return wrappedFunc


@tsfunc
def foo():
    pass


foo()
sleep(1)
for i in range(2):
    sleep(1)
    foo()


def A(a):
    print("I am A")

    def B(b):
        print("a+b=", a + b)
        print("I am B")

    B(2)
    print("Over!!!")
A(3)