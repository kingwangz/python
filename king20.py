def nume(k):
    while k == 0:
        print("(a)Student account number")
        print("(b)Teacher account number")
        print("(c)Exit")
        a = input()
        h = 0
        while a == 'a' and k == 0:
            num = input("Enter your ID number:\nreturn\n")
            if num[0:2].isalpha() == True and num[2:6].isnumeric() == True and len(num) == 6:
                k = 1
                h = 1
                print("Through")
            elif num == 'return':
                h = 1
                break
            else:
                print("Illegal input")
        while a == 'b' and k == 0:
            num = input("Enter your ID number:\nreturn\n")
            if num == 'king99':
                k = 1
                h = 1
                print("Through")
            elif num == 'return':
                h = 1
                break
            else:
                print("Illegal input")
        if a == 'c' and k == 0:
            exit(0)
        if h == 0:
            print("Illegal input")
    global r
    r = num
    return k


def math():
    from datetime import datetime
    g = 0
    o = []
    print("The test starts!")
    l = datetime.now()
    for i in range(10):
        import random
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        c = random.randint(1, 4)
        if c == 1:
            while a * b > 100:
                a = random.randint(0, 100)
                b = random.randint(0, 100)
            d = '*'
            f = a * b
        if c == 2:
            while a < b or b == 0 or a % b != 0:
                a = random.randint(0, 100)
                b = random.randint(0, 100)
            d = '/'
            f = a / b
        if c == 3:
            while a + b > 100:
                a = random.randint(0, 100)
                b = random.randint(0, 100)
            d = '+'
            f = a + b
        if c == 4:
            while a < b:
                a = random.randint(0, 100)
                b = random.randint(0, 100)
            d = '-'
            f = a - b
        print(a, d, b)
        h = 0
        while h == 0:
            try:
                e = input()
                n = int(e)
            except NameError:
                print("Please enter an integer")
            except SyntaxError:
                print("Please enter an integer")
            except ValueError:
                print("Please enter an integer")
            else:
                h = 1
        if n == f:
            g += 10
            print('Correct')
        else:
            print("Error")
            print("Correct answer：{}".format(f))
        o.append(a)
        o.append(d)
        o.append(b)
        o.append(f)
        o.append(n)
    print("{:-^18}".format("Transcripts"))
    for i in range(0, 50, 5):
        print("{:3}{}{:<3} {:<4} {:<3}".format(o[i], o[i + 1], o[i + 2], o[i + 3], o[i + 4]))
    print("---------------------")
    m = datetime.now()
    print("Your grades：{}".format(g))
    print("Your time:{}".format(m - l))
    print("Current time:{}".format(m))
    wen = open("king.txt", "a+")
    wen.write("{:<15}".format(r))
    wen.write("{:<10}".format(g))
    wen.write("{}\n".format(m - l))
    wen.close()


def look():
    h = list(r)
    print("IDnumber     Results         Time ")
    ken = open("king.txt", "r", encoding='utf-8')
    wen = ken.readlines()
    for line in wen:
        s = list(line)
        if s[0:6] == h:
            print(line)
    ken.close()


def look1():
    print("IDnumber     Results         Time ")
    ken = open("king.txt", "r", encoding='utf-8').read()
    print(ken)


a = nume(0)
while a == 1:
    if r == 'king99':
        print("(a)Query results")
        print("(b)Switch account")
        print("(c)Exit")
        b = input()
        if b == "a":
            look1()
        elif b == "b":
            nume(0)
        elif b == "c":
            a = 0
        else:
            print("Illegal")
    else:
        print("(a)Enter the test")
        print("(b)Query results")
        print("(c)Switch account")
        print("(d)Exit")
        b = input()
        if b == "a":
            math()
        elif b == "b":
            look()
        elif b == "c":
            nume(0)
        elif b == "d":
            a = 0
        else:
            print("Illegal")
