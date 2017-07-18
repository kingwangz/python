'''k = ['a', 'b', 'c']
k.append('s')
print(k)
k.remove('s')
print(k)
k.pop(0)
print(k)
l = [1, 2, 3]
print(l + k)
k = ['a', 'b', 'k', 'c']
k.sort()
print(k)'''
person = ['name', [100.00]]
hubby = person[:]
wifey = person
print(person)
# wifey = list(person)
hubby[0] = 'joe'
wifey[0] = 'jane'
print(hubby, wifey)
hubby[1][0] = 50.00
print(hubby, wifey)
person = ['name', 100.00]
hubby = person[:]
wifey = person
print(person)
# wifey = list(person)
hubby[0] = 'joe'
wifey[0] = 'jane'
print(hubby, wifey)
hubby[1] = 50.00
print(hubby, wifey)
person = ['name', ['savings', 100.00]]
hubby = person[:]
wifey = person
print(person)
# wifey = list(person)
hubby[0] = 'joe'
wifey[0] = 'jane'
print(hubby, wifey)
hubby[1][1] = 50.00
print(hubby, wifey)
person = ['name', ['savings', 100.00]]
hubby = person[:]
import copy
wifey = copy.deepcopy(person)
print(person)
# wifey = list(person)
hubby[0] = 'joe'
wifey[0] = 'jane'
print(hubby, wifey)
hubby[1][1] = 50.00
print(hubby, wifey)