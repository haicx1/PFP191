import datetime


def date_val(date):
    date_format = '%d-%m-%Y'
    try:
        dateObject = datetime.datetime.strptime(date, date_format)
        print('valid')
    except:
        print('not valid')


def char_code(a, b):
    num1 = ord(a)
    num2 = ord(b)
    if num1 > num2:
        num1, num2 = num2, num1
    for i in reversed(range(num1, num2 + 1)):
        hx = ''.join(hex(i)[2:])
        print(f'{chr(i)}:{i},{hx}h')


def menu():
    print('MENU')
    print('1.Valid Date')
    print('2. print ACSII characters.')
    while True:
        try:
            choice = int(input('Enter choice:'))
            if choice == 1 or choice == 2:
                break
            else:
                print('Enter your choice again.')
        except:
            print('Invalid input')
    if choice == 1:
        n = input('Enter date(dd-mm-yyyy):')
        date_val(n)
    if choice == 2:
        while True:
            char = input()
            if len(char) != 2:
                print('Must input 2 characters.')
                continue
            else:
                break
        chrs = list(char)
        char_code(chrs[0], chrs[1])


menu()
