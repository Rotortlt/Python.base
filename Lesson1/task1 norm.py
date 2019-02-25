import random
randomNumber = int(random.random() * 1000000)
maxNumber = 0
print(randomNumber)

while randomNumber > 0:
    randomIntegerNumber = int(randomNumber // 10)
    randomNumber = round((randomNumber / 10), 1)
    randomNumberI = int(round((randomNumber * 10),1)) - (randomIntegerNumber * 10)
    randomNumber = randomIntegerNumber
    if randomNumberI > maxNumber:
        maxNumber = randomNumberI

print(maxNumber)






