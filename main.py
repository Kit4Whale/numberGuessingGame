import random

def random_number():
    return random.randint(1, 100)

def is_valid(number):
    if number.isdigit() and 1 <= int(number) <= 100:
        return True
    else:
        return False

flag = True

cnt = 0

print("Добро пожаловать в числовую угадайку")

while flag:
    print(random_number())

    print("Введите число от 1 до 100: ", end="")

    mystery_number = input()

    if not is_valid(mystery_number):
        print("А может быть все-таки введем целое число от 1 до 100?")

    if is_valid(mystery_number):
        mystery_number = int(mystery_number)
        cnt += 1

        if mystery_number == random_number():
            print("Вы угадали, поздравляем!")
            flag = False

        if mystery_number < random_number():
            print("Ваше число меньше загаданного, попробуйте еще разок")

        if mystery_number > random_number():
            print("Ваше число больше загаданного, попробуйте еще разок")

print(f"Вы угадали за {cnt} попыток")
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")