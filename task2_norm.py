#NORMAL

# Написать две программы:
# Одна принимает через argparse число N и текст S и в цикле N раз выводит S в консоль
# А вторая программа принимает через input число M
# И указанное кол-во раз спрашивает через input N и S и запускает первую программу через os.system

import os
import sys

import argparse

parser = argparse.ArgumentParser(description='Выводим текст S - N раз')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='Введите целое число от 1 до 100')

for i in range (n):
    print(s)


