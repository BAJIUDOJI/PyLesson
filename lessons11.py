name = 'Serega'
age = 40

print('My name is ' + name + '. I\'m ' + str(age) + ' years')
print('My name is %(name)s. I\'m %(age)d years' % {'name': name, 'age': age})
print('My name is %s. I\'m %d years!' % (name, age))

# format
print('My name is {0}. I\'m {1} years!'.format(name, age))
print('My name is {name}. I\'m {age} years!'.format(name=name, age=age))
print('My name is {name}. I\'m {age} years!'.format(name='Alex', age=age))


# f-strings
print(f'My name is {name}. I\'m {age} years!')
print(f'5 + 2 = {5 + 2}')
