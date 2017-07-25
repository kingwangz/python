class MyData:
    pass


mathObj = MyData()

mathObj.x = 2
mathObj.y = 3
print(mathObj.x + mathObj.y)
print(mathObj.x * mathObj.y)


class MyDataWithMethod(object):
    def printFoo(self):
        print('You invoked printFoo()!')


myObj = MyDataWithMethod()
myObj.printFoo()


class addrBookEntry(object):
    def __init__(self, nm, ph):
        self.phone = ph
        self.name = nm
        print('Created instance for:', self.name)
        print('Created instance for:', self.phone)

    def updatePhone(self, newph):
        self.phone = newph
        print('Updated phone for:', self.phone)


john = addrBookEntry('John Doe', '408-555-1212')
john.updatePhone('2')
print(john.phone)


class emplAddrBookEntry(addrBookEntry):
    def __init__(self, nm, ph, id, em):
        addrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print('Updated e-mail address for:', self.name)


john = emplAddrBookEntry('John Doe', '408-555-121', 42, 'john@spam.doe')
print(dir(emplAddrBookEntry))
print(emplAddrBookEntry.__dict__)
print(emplAddrBookEntry.__bases__)
print(emplAddrBookEntry.__class__)
print(emplAddrBookEntry.__doc__)
print(emplAddrBookEntry.__name__)
print(emplAddrBookEntry.__module__)
print(type(emplAddrBookEntry))
print(type(0))
