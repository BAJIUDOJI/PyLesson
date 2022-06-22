# Словари dictionary


# d = {}
# product1 = {'title': 'Sony',
#             'price': 100}
# product2 = dict(title='iphone', price=400)
# users = [
#     ['bob@gmail.com', 'Bob'],
#     ['katy@gmail.com', 'Katy'],
#     ['john@gmail.com', 'John'],
# ]
# d_users = dict(users)
#
# print(users)
# print(d_users)
#
# print(d)
# print(product1)
# print(product2)


# product3 = dict.fromkeys(['price1]', 'price2', 'price3', ], 50)
# print(product3)


# product3nums = {i: i + 1 for i in range(1, 11)}
# print(nums)


product1 = {'title': 'Sony', 'price': 100}
product2 = dict(title='iphone', price=400)

# print(product1['title'])
# print(product1.get('title'))

# for key in product1:
#     print(product1[key])
#     print(f'{key}: {product1[key]}')
#
# for key, value in product1.items():
#     print(key, value)


products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iphone', 'price': 110},
    {'title': 'Samsung', 'price': 90}
]
print(products)

for product in products:
    print(product['title'], product['price'])
