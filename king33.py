class InstCt(object):
    count = 0

    def __init__(self):
        InstCt.count += 1

    def __del__(self):
        InstCt.count -= 1

    def howMany(self):
        return InstCt.count


a = InstCt()
print(a.howMany())
b = InstCt()

print(b.howMany())

print(a.howMany())

del b

print(a.howMany())

del a

print(InstCt.count)
