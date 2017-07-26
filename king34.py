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


A.static_foo()
A.class_foo()