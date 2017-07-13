class FooClass(object):
    """my very first class: FooClass"""
    version = 0.1

    def __init__(self, nm='John Doe'):
        """constructor"""
        self.name = nm

    def showname(self):
        """display instance attribute and class name"""
        print('Your name is', self.name)
        print('My name is', self.__class__.__name__)

    def showver(self):
        """display class(static) attribute"""
        print(self.version)

    def addMe2Me(self, x):
        return x + x
foo1 = FooClass()
foo1.showver()
