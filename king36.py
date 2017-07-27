class Time60(object):
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    def __str__(self):
        return '{}:{}'.format(self.hr, self.min)

    def __add__(self, other):
        return self.__class__(self.hr + other.hr, self.min + other.min)

    __repr__ = __str__

    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self


mon = Time60(10, 30)
tue = Time60(11, 15)
print(mon, tue)
print(mon + tue)
mon += tue
print(mon)
