#NORMAL

# Написать две программы:
# Одна принимает через argparse число N и текст S и в цикле N раз выводит S в консоль
# А вторая программа принимает через input число M
# И указанное кол-во раз спрашивает через input N и S и запускает первую программу через os.system

import os
import sys

m = int(input("Input number M: "))

for i in range (m):
    n,s = input("Введите число и через зяпятую текст: ")
    os.system(task2_norm)


