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
        d = '-'''''