'''def foo():
    print("\ncalling foo()...")
    bar = 200
    print("in foo(), bar is", bar)


bar = 100

print("in __main__, bar is", bar)
foo()
'''


def foo():
    print('\ncalling foo()...')
    aString = 'bar'
    anInt = 42
    print("foo()'s globals:", globals().keys())
    print("foo()'s locals:", locals().keys())


print("__main__'s globals:", globals().keys())
print("__main__'s locals:", locals().keys())
foo()
