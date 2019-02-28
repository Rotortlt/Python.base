list_1 = [1, 2, 3, 34, 65, 76, 978, 66679, 2]
list_2 = [2, 3, 54, 1]

for item in list_1:
    if item in list_2:
        list_1.remove(item)

print (list_1)







