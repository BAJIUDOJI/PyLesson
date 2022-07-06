# s = 'Hello worid'
# if ' ' in s:
#     s = s.upper()
# else:
#     s = s.lower()
#
#
# print(s)


# def set_register(s):
#     if ' ' in s:
#         return s.upper()
#     else:
#         return s.lower()
#
#
# print(set_register('Hello_World'))
# print(set_register('Hello World'))


# def get_sum(a, b, c, d):
#     return a + b * c / d
#
#
# print(get_sum(2, 6, 8, 3))


# def get_sum(*args):
#     return sum(args)
#
#
# print(get_sum(1, 5, 10))


# def func(**kwargs):
#     print(kwargs)
#
#
# func(a=1, b=5, c=20)


def f(a, x, *args, **kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)


f(1, 2, 3, 4, b='test', c='hi')
