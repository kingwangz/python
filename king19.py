import jieba
word='djkkkkks'
cou={}
for words in word:
    cou[words]=cou.get(words,0) + 1
    print(words)
print(cou.items())
items = list(cou.items())
print(items)
txt = open("2.1.txt", "r").read()
txt = txt.lower()
for ch in '唐诗':
        txt = txt.replace(ch, " ")
print(txt)
k= txt.split()
print(k)
l=['f','d','d']
print(l[2])
for i in range(4):
    if i==2:
        print(i)
        continue
    else:
        print(i)
    print(i)
print(i)
print(i)
'''
import random
for i in range(10):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(1, 4)
    if c == 1:
        while a * b > 100:
            a = random.randint(0, 100)
            b = random.randint(0, 100)
        d = '*'
    if c == 2:
        while a < b or b == 0 or a % b != 0:
            a = random.randint(0, 100)
            b = random.randint(0, 100)
        d = '/'
    if c == 3:
        while a + b > 100:
            a = random.randint(0, 100)
            b = random.randint(0, 100)
        d = '+'
    if c == 4:
        while a < b:
            a = random.randint(0, 100)
            b = random.randint(0, 100)
        d = '-'
    print(a,d,b)
from datetime import datetime
n=datetime.now()
l=datetime.now()
print(l-n)
o=[]
for i in range(10):
    e = eval(input())
    h=0
    o.append(e)
    o.append(h)
print(o)
j=0
for i in range(10):
    j=j+5
print(j)

r="ss2222"
h=list(r)
print(h)
wen = open("king.txt", "r+", encoding='utf-8').readlines()
for line in wen:
    s=list(line)
   # print(s[0:6])
    if  s[0:6]==h:
       print (line)
       while h == 0:
           try:
               e = input()
               n = eval(e)
           except NameError:
               print("Please enter an integer")
           except SyntaxError:
               print("Please enter an integer")
           else:
               h = 1
           finally:
               if e == 'b' or e == 'a' or e == 'c' or e == 'd' or e == 'f' or e == 'l' or e == 'n':
                   print("Please enter an integer")
                   h = 0
               if e == 'g' or e == 'h' or e == 'e' or e == 'i' or e == 'j' or e == 'm' or e == 'o':
                   print("Please enter an integer")
                   h = 0'''
