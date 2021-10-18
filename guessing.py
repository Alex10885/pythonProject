from random import *


def is_valid(n):
    return n.isdigit() and (0 < int(n) < 101)


def continue_game():  # Предложение продолжить игру
    ans = input('Хотите продолжить ("д"/"н")?\n')
    while True:
        if ans not in ('y', 'д', 'n', 'н'):
            ans = input('Вроде, взрослый человек, а на простой вопрос ответить не может...\nПродолжим ("д"/"н")?\n')
        elif ans in ('n', 'н'):
            print('До новых встреч!!!')
            return False
        else:
            return True


def generator():
    num = randint(1, 100)
    return num


shot = 1
print('Игра "Угадайка чисел"')
print()
print('Добро пожаловать в числовую угадайку')
chislo = generator()
while True:

    n = input('Угадай какое число от 1 до 100 у меня на уме! \n')
    if is_valid(n):
        num = int(n)
        print(chislo)
        if num < chislo:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            shot += 1
        elif num > chislo:
            print("Ваше число больше загаданного, попробуйте еще разок")
            shot += 1
        elif num == chislo:
            print("Вы угадали, поздравляем!")
            print("Количество попыток: ", shot)
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            if continue_game():
                shot = 1
                chislo = generator()
                continue
            else:
                break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
