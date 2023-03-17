from drink import Drink
drink_list = list()
def add_drink():
    while True:
        name = input('Enter name:')
        if len(name) > 20:
            print( 'name must have below 21 chars')
            continue
        else:
            break
    while True:
        make = input('Enter make:')
        if len(make) > 20:
            print( 'make must have below 21 chars')
            continue
        else:
            break
    while True:
        try:
            volume = int(input('Enter volume:'))
            break
        except:
            print( 'error')
    while True:
        try:
            price = int(input('Enter price:'))
            break
        except:
            print( 'error')
    while True:
        try:
            duration = int(input('Enter duration:'))
            break
        except:
            print('error')
    drink_list.append(name, make, volume, price, duration)
    print('add success')

def print_drink():
    make = input('Enter make:')
    list_dr = [x for x in drink_list if x.make == make]
    if not list_dr:
        print('make not found')
    else:
        for drink in list_dr:
            drink.display()

def print_drink_1():
    v1 = int(input('Enter v1'))
    v2 = int(input('Enter v2'))
    list_dr = [x for x in drink_list if x.volume in range(v1,v2+1)]
    if not list_dr:
        print('make not found')
    else:
        for drink in list_dr:
            drink.display()

def print_drink_2():
    drink_list.sort(key=lambda x:x.volume)
    drink_list.sort(key=lambda x:x.price)
    for drink in drink_list:
        drink.display()

while True:
    print('1-Adding a new drink')
    print('2-Printing out items with make')
    print('3-print between v1 v2')
    print('4-print by volume then price')
    print('5-Quit')
    try:
        choice = int(input('Enter choice(1 -> 5):'))
    except:
        print('sai cu phap')
    if choice not in range(1, 6):
        print('nhap tu 1 -> 6')
        continue
    elif choice == 1:
        add_drink()
        continue
    elif choice == 2:
        print_drink()
        continue
    elif choice == 3:
        print_drink_1()
        continue
    elif choice == 4:
        print_drink_2()
        continue
    elif choice == 5:
        print('Exit')
        break