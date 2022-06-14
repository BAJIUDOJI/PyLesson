# x = 10
# print(x, id(x))
# x = 20
# print(x, id(x))

# s = 'hello'
# s += ' world'
# print(s, id(s))

# l = [1, 2, 3]
# print(l, id(l))
# l.append(l)
# print(l, id(l))


l1 = [1, 2, 3]
l2 = l1
print(l1, id(l1))
print(l2, id(l2))