
def cazino(a, b):
    import time
    print('Подождите...')
    time.sleep(2)
    import random
    choice = random.randint(1,31)
    if choice == a:
        print(f'Загаданное число: {choice}')
        print(f'+{b}$')
        print('Вы выиграли!')
        return b * 2
    else:
        print(f'Загаданное число: {choice}')
        print(f'-{b}$')
        print('Вы проиграли!')
        return 0