def ball_throw():
    i = 0
    j = 0
    while True:
        try:
            total = int(input('Total sought:'))
            if total in range(2, 21):
                break
            else:
                continue
        except:
            print('invalid input')

    while True:
        i += 1
        j += 1
        k = j + 1
        dice1 = random.randint(1, 11)
        dice2 = random.randint(1, 11)
        total_1 = dice1 + dice2
        if total_1 == total:
            print(f'Result of picks {j} and {k}:{dice1} + {dice2}')
            print(f'You got your total in {k} picks!')
            break
        else:
            print(f'Result of picks {j} and {k}:{dice1} + {dice2}')
            pass


ball_throw()
