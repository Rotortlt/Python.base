import random
randomNumber = int(random.random() * 1000000)
print(randomNumber)

while randomNumber > 0:
    randomIntegerNumber = int(randomNumber // 10)
    randomNumber = float(randomNumber / 10)
    randomNumberI = int((randomNumber * 10) - (randomIntegerNumber * 10))
    randomNumber = randomIntegerNumber

    print(randomNumberI)






