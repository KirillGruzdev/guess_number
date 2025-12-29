from random import randint

the_number = randint(1, 100)
user_number = 0
while True:
    user_number = int(input())
    if user_number == the_number:
        break
    elif user_number > the_number:
        print('Ваше число больше того, что загадано')
    else:
        print('Ваше число меньше того, что загадано')
print('Отличная интуиция! Вы угадали число :)')
    