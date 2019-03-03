# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
import random

ticket = int(random.randint(100000, 999999))

def fun_happy_ticket(ticket):
    ticket_str = list(str(ticket))

    if int(ticket_str[0]) + int(ticket_str[1]) + int(ticket_str[2]) == int(ticket_str[3]) + int(ticket_str[4]) + int(
            ticket_str[5]):
        ticket1 = ('Happy')
    else:
        ticket1 = ('Not happy')
    return  ticket1

print(f"Your ticket №{ticket} is - {fun_happy_ticket(ticket)}")