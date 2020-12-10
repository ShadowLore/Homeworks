from random import randint


def play():
    random_int = randint(0, 100)

    while True:
        user_guess = int(input("Запишите целое число в диапазоне от 0 до 100?"))
        if user_guess == random_int:
            print("Вы угадали число ({random_int}). Поздравляю!")
            break
        if user_guess < random_int:
            print("Ваше число меньше секретного.")
            continue
        if user_guess > random_int:
            print("Выше число больше секретного.")
            continue

if __name__ == '__main__':
    play()
