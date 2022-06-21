# Множество

# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s2 = set('hello')
# s3 = {i for i in range(1, 11)}
# s4 = set()
#
# print(s4, type(s4))
# ----------------------------------------

# nums = [1, 2, 3, 3, 1, 2, 4, 5]
# nums2 = set(nums)
# nums2 = list(set(nums))
# print(nums2)
# -----------------------------------------

# a = set('abracadabra')
# b = set('calcium')
#
# c = a - b  # вычитание - убираем из а все буквы, которые есть в b
# d = a | b  # объединение - буквы или в а или в b
# e = a & b  # пересечение - буквы и в а и в b
# f = a ^ b  # множество из элементов - буквы в а или b, но не в обоих
#
# print(a, b, c, d, e, f, sep='\n')
# -------------------------------------------

# set.copy() - возвращает копию множества
# set.add(elem) - добавляет элемент в множество
# set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует
# set.discard(elem) - удаляет элемент если он находится в множестве
# set.pop() - возвращает и удаляет первый элемент из множества. т.к. множества не упорядочены, нельзя точно сказать,
#             какой элемент будет первым
# set.clear() - очистка множества


s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s2 = s.copy()#
# print(s, id(s))
# print(s2, id(s2))

# s.add('melon')
# print(s)

# s.remove('apple')
# print(s)

# if 'pear' in s:
#     print('OK')


# s.pop()
# print(s)

# s.clear()
# print(s)


# frozenset

a = frozenset('hello')
print(a)

for i in s:
    print(i)