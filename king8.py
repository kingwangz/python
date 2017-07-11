import time

s = 50
print("\n" + "kaishi".center(s // 2, '-'))
t = time.clock()
for i in range(s + 1):
    a = '*' * i
    b = '.' * (s - i)
    c = (i / s) * 100
    t -= time.clock()
    print("\r{:^3.0f}%[{}->{}]{:.2f}".format(c, a, b, -t), end="")
    time.sleep(0.3)
print("\n" + "jieshu".center(s // 2, '-'))
