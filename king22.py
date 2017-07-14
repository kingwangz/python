import os

ls = os.linesep
while True:
    fname = input()
    if os.path.exists(fname):
        print("ERROR: '%s' already exists".format(fname))
    else:
        break
all = []
print("\nEnter lines ('.' by itself to quit).\n")
while True:
    entry = input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)
fobj = open(fname, 'w')
fobj.writelines(['%s%s'.format(x, ls) for x in all])
fobj.close()
print('DONE!')
fobj = open(fname, 'r')
fobj.read()
print(fobj)
