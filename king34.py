class TestStaticMethod:
    @staticmethod
    def foo():
        print('calling static method foo()')


class TestClassMethod:
    @classmethod
    def foo(cls):
        print('calling class method foo()')
        print('foo() is part of class:', cls.__name__)


class A(object):
    bar = 1

    def foo(self):
        print('foo')

    @staticmethod
    def static_foo():
        print('static_foo')
        print(A.bar)

    @classmethod
    def class_foo(cls):
        print('class_foo')
        print(cls.bar)
        cls().foo()


class P(object):
    def __init__(self):
        print("calling P's constructor")


class C(P):
    def __init__(self):
        super(C, self).__init__()
        print("calling C's constructor")

c = C()
A.static_foo()
A.class_foo()
TestStaticMethod.foo()
TestClassMethod.foo()
