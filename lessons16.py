l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
names = ['Иванов', 'Петров', 'Сидоров']


# print(l[4][0])
# print(l[0:3])
l.append('new')
l.extend([5, 7])
l2 = ['hi', 19]
l += l2
l.insert(1, 'two')
l.remove('two')
el = l.pop()
l3 = ['Hello', 'world', 'Petrov', 'Magnum', 'Harley', 'Mars']
l3.sort(reverse=True)
print(l, l.count('world'), l3, sep='\n')
