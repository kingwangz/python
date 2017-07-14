def displayNumType(num):
    print(num, "is", )
    if type(num) == type(0):
        print('an integer')
    elif type(num) == type(0.0):
        print('a float')
    elif type(num) == type(0 + 0j):
        print('a complex number')
    else:
        print('not a number at all!!')


k = "kingking"
print(k[-1:4:-2])
foo1 = 4.2
foo2 = 1.1 + 3.1
print(foo1 is foo2)
print(id(foo1))
print(id(foo2))
foo1 = 2
foo2 = 1 + 1
print(foo1 is foo2)
print(id(foo1))
print(id(foo2))
print(repr(foo1))
del foo1
print(0.1 / 0.2)
print(0.1)
