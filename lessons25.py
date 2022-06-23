i = 75

user = 0
cnt = 0

while True:
    user = int(input('Введите чмсло от 1 до 100: '))
    cnt += 1
    if user == i:
        print(f'Ты угадал число с {cnt} попыток')
        print('Спасибо за игру')
    elif user > i:
        print('Мое число меньше')
    else:
        print('Мое число больше')
