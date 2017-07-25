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
        print('Updated phone# for:', self.name)


addrBookEntry('John ', '408-555-1212')
addrBookEntry('Jane ', '650-555-1212')
