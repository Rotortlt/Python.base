#EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# Учесть проверку на то что папка не пуста и на то, что такая папка уже существует

import os

name_dir = [('dir_' + str(i + 1)) for i in range (9)]

def make_dir (name_dir):
    dir_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' - такая директория уже есть')

def del_dir(name_dir):
    dir_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.rmdir(name_dir)
    except:
        print(name_dir + ' - эта директория не пустая')


for i in name_dir:
    make_dir(i)


print(name_dir)

N = input("Для удаления директорий нажмите D : ")

if N == ("D"):
    for i in name_dir:
        del_dir(i)


