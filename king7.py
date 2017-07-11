'''s="python"
y="holle"
print("{0:*>30}".format(s))
print("{0:*<30}".format(y))
print("y\n")
print(s)'''
import time

s = 10
print("_______kaishi_______")
for i in range(s + 1):
    a, b = '**' * i, '..' * (s - i)
    c = (i / s) * 100
    print("%{:^3.0f}[{}->{}]".format(c, a, b))
    time.sleep(0.1)
print("______jieshu_______")
