
fruits_list = ["яблоко","банан","апельсин","мандарин","киви","манго"]
length_fruits_list = len(fruits_list)
for i in range (len(fruits_list)):
    print(i + 1, '{:>20}'.format(fruits_list[i]))
