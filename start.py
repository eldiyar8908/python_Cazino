
from logic import cazino
My_money = 1000
start = input()
while start == 'start':
    user = input('Вы хотите играть?: ')
    if user == 'нет':
        break
    elif user == 'да':
        number = int(input('Введите число от 1 до 30: '))
        stav = int(input('Ваша ставка: '))
        My_money -= stav
        My_money = My_money + cazino(number, stav)
        print(f'Баланс: {My_money}$')
    else:
        print('Введите коректно!!!')