tem=input("shuru")
while tem[-1]not in ['N','n']:
 if tem[-1]in['F','f']:
    C=(eval(tem[0:-1])-32)/1.8
    print("zhuanhuan{:.2f}C".format(C))
 elif tem[-1]in['C','c']:
    F=1.8*eval(tem[0:-1])+32
    print("zhuanhuan{:.2f}F".format(F))
 else:
    print("error")
 tem=input("shu ru")