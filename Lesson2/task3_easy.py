random_list_1 = [1, 34, 5646, 65, 12, 45, 12, 62]
random_list_2 = []

for i in range (len(random_list_1)):
    if random_list_1[i] % 2 == 0:
        random_list_2.append(random_list_1[i] // 4)
    else:
        random_list_2.append(random_list_1[i] * 2)

print(random_list_2)