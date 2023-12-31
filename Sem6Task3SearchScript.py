#Улучшаем задачу 2.
#Добавьте возможность запуска функции «угадайки» из модуля в командной строке терминала.
#Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
#Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from sys import argv
from random import randint

def binary_search(count: int, minimum=0, maximum=100) -> bool:
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

if __name__ == '__main__':
    binary_search(*[int(i) for i in argv[1:]])