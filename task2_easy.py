# Задача-2:
# Напишите скрипт, который выводит в консоль список файлов и папок в указанной директории.

import os

def list_dir(path):
    return os.listdir(path)

path_user = input("Укажите путь папки для просмотра ее содержания : ")

print(list_dir(path_user))