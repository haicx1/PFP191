import random

num = int(input('Enter number to guess:'))
range = int(input('Enter a range for guessed number:'))
while True:
    guess = random.randint(1,range)
    if guess == num :
        print(f'Is {guess} too hight(h), too low(l), or correct(c): c')
        print(f'Welldone! The computer guessed your number {num} correctly!')
        print('Finish')
        break
    elif guess > num:
        print(f'Is {guess} too hight(h), too low(l), or correct(c): h')
        continue
    else:
        print(f'Is {guess} too hight(h), too low(l), or correct(c): l')
        continue


