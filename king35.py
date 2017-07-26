class P1(object):
    print('called P1-foo()')


class P2(object):
    print('called P2-foo()')

    def bar(self):
        print('called P2-bar()')


class C1(P1, P2):
    pass


class C2(P1, P2):
    print('called C2-bar()')


class GC(C1, C2):
    pass


P2.bar(1)
