import random

def random_number(n):
    return random.randint(1, n)

def is_valid(number):
    if number.isdigit() and 1 <= int(number) <= n:
        return True
    else:
        return False


print("Добро пожаловать в числовую угадайку")
print("Выбирите верхнюю границу диапозона. Диапозон с 1 по n, введите значение n: ", end="")

n = int(input())

flag = True
cnt = 0
r_num = random_number(n)
ask = ""
mystery_number = ""

while flag:
    print(r_num)

    print(f"Введите число от 1 до {n}: ", end="")

    mystery_number = input()

    if not is_valid(mystery_number):
        print(f"А может быть все-таки введем целое число от 1 до {n}?")
        cnt += 1

    else:
        mystery_number = int(mystery_number)
        cnt += 1

        if mystery_number == r_num:
            print(f"Вы угадали за {cnt} попыток, поздравляем!")
            print("Если хотите сыграть ещё, напишите 'Да', иначе напишине 'Нет' или любое другое значение: ", end="")
            ask = input()
            if ask == "Да":
                cnt = 0
                print("Выбирите верхнюю границу диапозона. Диапозон с 1 по n, введите значение n: ", end="")
                n = int(input())
                r_num = random_number(n)
                continue
            else:
                flag = False

        if mystery_number < r_num:
            print("Ваше число меньше загаданного, попробуйте еще разок")

        if mystery_number > r_num:
            print("Ваше число больше загаданного, попробуйте еще разок")


print("Спасибо, что играли в числовую угадайку. Еще увидимся...")