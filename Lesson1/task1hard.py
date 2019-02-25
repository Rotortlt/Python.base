number = int(input("Введите число: "))
count = 0
i = 0
while count < 3:
    i = i + 1
    if number % i == 0:
        count = count + 1
    if count > 2:
        print("Вы ввели число ", number, " оно сложное")
        break
    if i == number:
        print("Вы ввели число ", number, " оно простое")
        break








