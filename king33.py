'''class InstCt(object):
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
'''


class HotelRoomCalc(object):
    def __init__(self, rt, sales=0.085, rm=0.1):
        self.salesTax = sales

        self.roomTax = rm

        self.roomRate = rt

    def calcTotal(self, days=1):
        daily = round((self.roomRate * (1 + self.roomTax + self.salesTax)), 2)
        return round(days) * daily


k = HotelRoomCalc(300)
print(k.calcTotal())
asWkDay = HotelRoomCalc(169, 0.045, 0.02)
print(k.calcTotal(5) + asWkDay.calcTotal())
# print(dir(HotelRoomCalc))
print(getattr(k, "calcTotal")())
print(getattr(k, "calc", "ss"))
