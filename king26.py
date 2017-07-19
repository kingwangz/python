fdict = dict((['x', 1], ['y', 2]))
print(fdict)
ddict = {}.fromkeys(('x', 'y'), (-1, -2))
print(ddict)
print(ddict.keys())
print('y' in ddict.keys())
print(hash('x'))
s = set('cheeseshop')
print(s)
t = frozenset('bookshop')
print(t)
myTuple = (123, 'xyz', 0, 45.67)
legends = {('Poe', 'author'): (1809, 1849, 1976), ('Gaudi', 'architect'): (1852, 1906, 1987),
           ('Freud', 'psychoanalyst'): (1856, 1939, 1990)}
i = iter(legends)
for k in list(legends):
    print(next(i))
print(legends)