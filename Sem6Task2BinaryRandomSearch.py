#Создайте модуль с функцией внутри.
#Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
#Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
#Функция выводит подсказки «больше» и «меньше».
#Если число угадано, возвращается истина, а если попытки исчерпаны — ложь.

from random import randint
def binary_random_search(minimum: int, maximum: int, count: int) -> bool:
    num = randint(minimum, maximum + 1)
    search_num = None
    while search_num != num:
        search_num = int(input("Угадайте число: "))
        print([["Загаданное число меньше", "Загаданное число больше"][search_num < num], "Угадали!"][search_num == num])
        count -= 1
        if count == 0:
            print("Попытки закончились")
            return False
    return True