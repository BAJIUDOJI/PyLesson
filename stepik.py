# ----less 2.4----

# s = 'abcdefghijk'


# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])


# s = 'aTGcc'
# p = 'cc'
#
# print(s.find('A'))


# s = 'agTtcAGtc'
# print(s.upper().count('gt'.upper()))


# s = input()
# a = s.upper()
# k = a.count('C')
# k2 = a.count('G')
# k3 = int(k) + int(k2)
# k4 = a.count('')
# result = (k3 / (k4 - 1)) * 100
# print(result)


# s = str(input())
# l = len(s) - 1
# c = 1
# t = ''
# if len(s) == 1:
#     t = t + s + str(c)
# else:
#     for i in range(0, l):
#         if s[i] == s[i + 1]:
#             c += 1
#         elif s[i] != s[i + 1]:
#             t = t + s[i] + str(c)
#             c = 1
#     for j in range(l, l + 1):
#         if s[-1] == s[-2]:
#             t = t + s[j] + str(c)
#         elif s[-1] != s[-2]:
#             t = t + s[j] + str(c)
#             c = 1
# print(t)


# ----less 2.5----


# students = ['Ivan', 'Masha', 'Sasha']
# students.reverse()
# ordered_students = sorted(students)
# if 'Ivan' in students:
#     print('OK')
#
# if 'Ann' not in students:
#     print('Ann is out')
# students += ['Olga']
# students.remove('Olga')
# del students[0]
# print(students)

# teachers = ['Oleg', 'Alex']
# res = students + teachers
# print(res[4])


# a = [1, 'A', 2]
# b = a
# a[0] = 42
# print('Значение а: ' + str(a))
# print('Значение b: ' + str(b))
# b[2] = 30
# print('Значение b: ' + str(b))
# print('Значение а: ' + str(a))


# a = [1, 2, 3]
# b = a
# print(b)
# a[1] = 10
# print(b)
# b[0] = 20
# print(a)
# a = [5,6]
# print(b)


# a = str(input()).split()  # split() - благодаря сплит - это теперь список, он состоит из
#                           # строк, разделенных пробелами а не из чисел
# for i in range(len(a)):  # Получаем список из чисел
#     a[i] = int(a[i])
# print(sum(a))


# list1 = [int(i) for i in input().split()]
#
# if len(list1) == 1:
#     print(list1[0])
#
# elif len(list1) == 2:
#     print(list1[1] * 2, list1[0] * 2)
#
# else:
#     for i in range(len(list1)):
#         if i < len(list1) - 1:
#             print(list1[i - 1] + list1[i + 1], end=" ")
#         else:
#             print(list1[0] + list1[i - 1])


# s = [int(i) for i in input().split()]
# t = []
# s.sort()
# l = len(s) - 1
# k = 100000
# if len(s) != 1:
#     for i in range(0, l):
#         if s[i] == s[i + 1] and s[i] != k:
#             t.append(s[i])
#             k = s[i]
#     for j in range(l, l + 1):
#         if s[-1] == s[-2] and s[j] != k:
#             t.append(s[j])
# n = len(t)
# for g in range(0, n):
#     print(t[g], end=' ')


# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(a[1][0])

# ----less 2.6----


# a = [int(i) for i in input().split()]
# m = a[0]
# for x in a:
#     if m > x:
#         m = x
# print(m)


# n, m, k = (int(i) for i in input().split())
# a = [[0 for j in range(m)]for i in range(n)]
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = - 1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()


# a1 = int(input())
# s = a1
# s2 = 0 + abs(a1 ** 2)
# while s != 0:
#     a1 = int(input())
#     s = s + a1
#     s2 = s2 + abs(a1) ** 2
#     if s == 0:
#         break
# print(s2)


# n = int(input())
# lis = []
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         lis.append(i)
# print(*lis[:n])


# s = [int(i) for i in input().split()]
# n = int(input())
# t = []
# l = len(s) - 1
# if n in s:
#     for i in range(0, l + 1):
#         if s[i] == n:
#             t.append(i)
#     g = len(t) - 1
#     for j in range(0, g + 1):
#         print(t[j], end=' ')
# else:
#     print('Отсутствует')


# m = []
# while True:
#     n = input().split()
#     if n[0] == 'end':
#         break
#     else:
#         m.append(n)
# for i in range(len(m)):
#     x = ''
#     for j in range(len(m[i])):
#         a = int(m[i - 1][j])
#         if i == len(m) - 1:
#             b = int(m[0][j])
#         else:
#             b = int(m[i + 1][j])
#         c = int(m[i][j - 1])
#         if j == len(m[i]) - 1:
#             d = int(m[i][0])
#         else:
#             d = int(m[i][j + 1])
#         s = a + b + c + d
#         x += str(s) + ' '
#     print(x.rstrip())


# a = int(input())
# nul = [[0] * a for i in range(a)]
# x, y = 0, 0
# for i in range(1, a ** 2 + 1):
#     nul[x][y] = i
#     if x <= y + 1 and x + y < a - 1:
#         y += 1
#     elif x < y:
#         x += 1
#     elif x + y >= a:
#         y -= 1
#     elif x >= y:
#         x -= 1
# for i in range(a):
#     print(*nul[i])


x = {'name': 'John', 'age': 36}
print(type(x))
