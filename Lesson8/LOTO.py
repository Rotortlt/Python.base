# 1 Создаем карты ЛОТО
# 2 механизм игры
import random
import pprint




def line(bank_loto_card):
    line = []
    for i in range(9):

        if i == 0:
            line.append(bank_loto_card[random.randint(0, 8)])
        if i == 9:
            line.append(bank_loto_card[random.randint((9 + ((i - 1) * 10)), (9 + (i * 10)))])
        if 0 < i < 9:
            line.append(bank_loto_card[random.randint((9 + ((i - 1) * 10)), (8 + (i * 10)))])

    it_for_zero_num = 0

    while it_for_zero_num < 4:

        item_line = random.randint(0, 8)

        if line[item_line] != 0:
            line[item_line] = 0
            it_for_zero_num += 1
        else:
            continue

    return line

def get_origin_line_in_card(line_compare: list, line_compare_1: list, line_compare_2: list):

    i = 0
    while i < 9:
        if line_compare[i] == 0:
            i += 1
            continue
        if line_compare[i] in line_compare_1 and line_compare[i] != 90 or line_compare[i] in line_compare_2 and line_compare[i] != 90:
            line_compare[i] += 1
            i += 1
            continue
        if line_compare[i] in line_compare_1 and line_compare[i] == 90 or line_compare[i] in line_compare_2 and line_compare[i] == 90:
            line_compare[i] -= 1
            i += 1
            continue
        i += 1
    return line_compare

def card(bank_loto_card):

    line_1 = line(bank_loto_card)
    line_2 = line(bank_loto_card)
    line_3 = line(bank_loto_card)

    line_2 = get_origin_line_in_card(line_2, line_1, line_3)
    line_3 = get_origin_line_in_card(line_3, line_2, line_1)


    card = [line_1, line_2, line_3]

    return card


def move_bank(bank_loto_move):

    random_pos_num = random.randint(0, len(bank_loto_move))

    move_bank = bank_loto_move[random_pos_num]

    bank_loto_move.pop(random_pos_num)

    return move_bank


def move_game(card_player, card_PC, bank_loto):
    j = 0
    bank_loto_move = bank_loto.copy()

    while j < 89:
        move_bank1 = move_bank(bank_loto_move)
        count_zero_in_card_player = 0
        count_zero_in_card_PC = 0

        for a in range(3):
            for b in range(9):
                if card_player[a][b] == 0:
                    count_zero_in_card_player += 1
        if count_zero_in_card_player == 27:
            print("Player1 you WIN!!!!")
            exit(0)

        for g in range(3):
            for h in range(9):
                if card_PC[g][h] == 0:
                    count_zero_in_card_PC += 1
        if count_zero_in_card_PC == 27:
            print("PC WIN!!!!")
            exit(0)

        print("Player1 - your Loto card is: ")
        pprint.pprint(card_player)

        print("Loto card PC is: ")
        pprint.pprint(card_PC)

        print(f"Выпал ,бочонок: {move_bank1}")

        if move_bank1 in card_PC[0] or move_bank1 in card_PC[1] or move_bank1 in card_PC[2]:
            for d in range(3):
                for e in range(9):
                    if move_bank1 == card_PC[d][e]:
                        card_PC[d][e] = 0
                        break

        move_player = input(" Зачеркнуть цифру, y/n? ")

        if move_player == ("n"):
            if move_bank1 in card_player[0] or move_bank1 in card_player[1] or move_bank1 in card_player[2]:
                print("You wrong, this number exist in your card")
                exit(0)
            else:
                j += 1
                continue

        if move_player == ("y"):
            count_number = 0
            for r in range(3):
                for t in range(9):
                    if move_bank1 == card_player[r][t]:
                        card_player[r][t] = 0
                        j += 1

                        continue
                    count_number += 1
            if count_number == 27:
                print("You wrong!!! This number don't exist in this card")
                exit(0)


def start_game(bank_loto):

    bank_loto_card = bank_loto.copy()
    card_player = card(bank_loto_card)
    card_PC = card(bank_loto_card)
    move_game(card_player, card_PC, bank_loto)


bank_loto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
             20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
             37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48, 48, 49, 50, 51, 52, 53,
             54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
             71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87,
             88, 89, 90]

start_game(bank_loto)






