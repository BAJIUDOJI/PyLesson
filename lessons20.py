# t1 = (1, 2, 3)
# t1 = tuple((1, 2, 3))
# test = 1, 2, 3


t1 = tuple('hello')
t2 = tuple(' world')
t3 = t1 + t2
print(len(t3))

if 'l' in t3:
    print(t3.index('l'))
else:
    print('NO')
