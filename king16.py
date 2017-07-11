from math import sqrt


def get():
    nums = []
    inum = input("pleas enter the num")
    while inum != "":
        nums.append(eval(inum))
        inum = input("pleas enter the num")
    return nums


def mean(numi):
    s = 0.0
    for num in numi:
        s = s + num
    return s / len(numi)


def dev(numi, mean):
    sdev = 0.0
    for num in numi:
        sdev = sdev + (num - mean) ** 2
    return sqrt(sdev / (len(numi) - 1))


def med(numi):
    sorted(numi)
    size = len(numi)
    if size % 2 == 0:
        med = (numi[size // 2-1] + numi[size//2]) / 2
    else:
        med = numi[size // 2]
    return med


n = get()
m = mean(n)
print("p:{},f:{:.2},z:{}.".format(m, dev(n, m), med(n)))
