'''import datetime

print(datetime.datetime.now())
text = open("3.1.txt", "r")
for line in text.readline():
    print(line)
text.close()'''
l = 'tang'
z = 'song'
j = 'yuan'
fo = open("2.1.txt", "a+")
fo.writelines(l)
fo.seek(0)
for line in fo:
    print("{}".format(line))
fo.close()
