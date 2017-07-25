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


class EmplAddrBookEntry(addrBookEntry):
    def __init__(self, nm, ph, id, em):
        addrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print('Updated e-mail address for:', self.name)


john = EmplAddrBookEntry('John Doe', '408-555-121', 42, 'john@spam.doe')
