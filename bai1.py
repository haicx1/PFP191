import random


def dice_throw():
    i = 0
    while True:
        try:
            total = int(input('Total sought:'))
            if total in range(2, 13):
                break
            else:
                continue
        except:
            print('invalid input')

    while True:
        i += 1
        dice1 = random.randint(1, 7)
        dice2 = random.randint(1, 7)
        total_1 = dice1 + dice2
        if total_1 == total:
            print('Result of throw', i, ':', total_1)
            print(f'You got your total in {i} throws!')
            break
        else:
            print('Result of throw', i, ':', total_1)
            pass


dice_throw()