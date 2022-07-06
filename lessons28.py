# def get_sum(a, b):
#     """
#     Возвращает сумму аргументов а и b.
#
#     :param a: Первый операнд
#     :type a: int
#     :param b: Второй операнд
#     :type b: int
#     :return: Return type int
#     """
#     return a + b
#
#
# print(get_sum(1, 2))


# a = 5  # global
#
#
# def f():
#     a = 10  # local
#     a += 1
#     print(a)
#
#
# f()


l = [1, 2, 3]


def f(l):
    return [i * 2 for i in l]


print(f(l))


def f2(l):
    def get_mult(x):
        return list(map())

    return [get_mult(i) for i in l]


print(f2(l))
