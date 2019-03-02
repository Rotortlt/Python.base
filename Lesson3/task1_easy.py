
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

import random

ran_number = random.random() * 100
count_mark = int(input("Введите до какого количества знаков округляем число полсе запятой: "))

print(ran_number)


def round_number(number, count_mark):

    integer_num = int(number * 10 ** count_mark )
    fraction_residue = ((number * 10 ** count_mark ) - integer_num)

    if fraction_residue > 5:
        fraction_residue = int(fraction_residue + 1)

    else:
        fraction_residue = int(fraction_residue)


    num = (integer_num + fraction_residue) / 10 ** count_mark

    return  num


print(f"Округленная число: {round_number(ran_number, count_mark)}")