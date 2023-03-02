import math

def bank_deposit():
    while True:
        try:
            d = float(input('Enter Deposit money:'))
            r = float(input('Enter Yearly rate:'))
            n = int(input('Enter number of year:'))
            if d > 0 and r > 0 and r < 1 :
                break
        except:
            print('Invalid input')
    amount = math.pow(d*(1+r), n)
    print(f'Amount at the {n}(th)year:{amount}')

def quadratic_e(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return ()
    elif delta == 0:
        x = (-b + math.sqrt(delta)) / (2 * a)
        return x,
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2

def menu():
    print('MENU')
    print('1.Quadratic equation')
    print('2.Bank deposit problem.')
    while True:
        try:
            choice = int(input('Enter choice:'))
            if choice == 1:
                a, b, c = float(input()), float(input()), float(input())
                result = quadratic_e(a, b, c)
                print(result)
                continue
            elif choice == 2:
                bank_deposit()
                continue
            elif choice == 3:
                print('Exit Program')
                break
            else:
                print('Enter your choice again.')
        except:
            print('Invalid input')

menu()
