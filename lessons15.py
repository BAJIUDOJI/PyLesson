print('Таблица умножения')

for i in range(1, 10):
    for j in range(2, 10):
        print(f'{j}*{i}={j * i}\t', end=' ')
    print('')
else:
    print('Well Done')