# Задание-1
# Есть два игрока и 25 монет.
# Каждый может брать от 1 до 3 монет.
# Проигрывает тот кто забрал последнюю.
#
# Написать программу для этой игры

class Coin_game:

    def __init__(self, player_1: str, player_2: str):

        self.player_1 = player_1
        self.player_2 = player_2
        self.coin = 25

    def game(self):

        while self.coin > 0:

            self.player = self.player_1

            try:
                self.move_player = int(input(self.player + " выберете количество монет от 1 до 3: "))

            except ValueError:
                print("Вы ввели не корректные данные, попробуйте еще раз")
                continue

            if self.move_player != 1 and self.move_player != 2 and self.move_player != 3:

                print(self.player + " - Вы не верно ввели количество монет, нужно выбрать от 1 до 3. Попробуйте еще раз")
                continue

            if self.move_player > self.coin:
                print(self.player + " - Вы ввели количество монет большее чем осталось")
                continue

            self.coin -= self.move_player

            if self.coin == 0:
                print(self.player + " - Вы проиграли!!!")
                exit(0)

            self.player_1, self.player_2 = self.player_2, self.player_1

            print(self.coin)

print('Игра монетка.')
print("Игроки у вас есть 25 монет. Каждый может брать от 1 до 3 монет. Проигрывает тот кто забрал последнюю.")

player_1 = input("Введите имя 1 игрока: ")
player_2 = input("Введите имя 2 игрока: ")

game1 = Coin_game(player_1, player_2)
game1.game()





