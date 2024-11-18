import random

def random_number():
    return random.randint(1, 100)

print("Добро пожаловать в числовую угадайку")

def is_valid(number):
    if number.isdigit() and 1 <= int(number) <= 100:
        return True
    else:
        return False

print(is_valid(input()))
