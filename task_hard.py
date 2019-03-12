#HARD

# Написать программу для распаковки файлов в корневую из всех папок с расширениями (код взять с урока) и папки удалить

import os

BASE_PATH = r"E:\Users\User\Downloads"
# Определить какие у меня в папке расширения у файлов
ext = set()
for i in os.listdir(BASE_PATH):
    if os.path.isfile(os.path.join(BASE_PATH, i)):
        print(os.path.splitext(i))
        ext.add(os.path.splitext(i)[1]) # добавить в множество расширение текущего файла

# print(ext)
# Создаем папки
for e in ext:
    if not os.path.exists(os.path.join(BASE_PATH, e)):
        os.mkdir(os.path.join(BASE_PATH, e))

# Переносим файлы в соответствующие каталоги
for i in os.listdir(BASE_PATH):
    if os.path.isfile(os.path.join(BASE_PATH, i)):
        os.rename(os.path.join(BASE_PATH, i),
                  os.path.join(BASE_PATH, os.path.splitext(i)[1], i))





for c in ext:
   for j in os.listdir(os.path.join(BASE_PATH, c)):
       if os.path.isfile(os.path.join(BASE_PATH, c, j)):
            os.rename(os.path.join(BASE_PATH, c, j), os.path.join(BASE_PATH, j))