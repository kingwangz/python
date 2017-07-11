f = lambda x, y: x * y
print(f(5, 4))


def v(a, *b):
    print(type(b))
    for n in b:
        a += n
        print(a)
    return a


v(1, 2, 3, 4, 5)

n = 1
ls = [9]


def func(a, b):
    global n
    n = b
    #ls = []
    ls.append(b)
    print(n, ls)
    return a * b


s = func("knock", 2)
print(s, n, ls)
from datetime import datetime

t = datetime.now()
print(t)
h = datetime.utcnow()
print(h)
k = datetime(2017, 10, 2, 7, 8, 9, 828782)
t = k.isoformat()
y = k.isoweekday()
o = k.strftime("%Y,%B%S")
print(k)
print(t)
print(y)
print(o)
