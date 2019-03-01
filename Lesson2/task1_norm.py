import math

random_list_1 = [1, 144, 25, 69, 81, 34, 5646, 65, 12, -45, 12, 62]
random_list_2 = []

for number in random_list_1:

    if number > 0 and int(math.sqrt(number)) == math.sqrt(number):
        random_list_2.append(int(math.sqrt(number)))

print(random_list_2)