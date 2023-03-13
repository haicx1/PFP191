import math


def test1():
    commands = input().split(',')
    print(*commands,sep='\n')
    print('FINISH')

def test2():
    x = 0
    y = 0
    commands = input().split(',')
    for command in commands:
        com = command.split()
        if com[0] == 'UP':
            y = y + float(com[1])
        elif com[0] == 'DOWN':
            y = y - float(com[1])
        elif com[0] == 'LEFT':
            x = x - float(com[1])
        elif com[0] == 'RIGHT':
            x = x + float(com[1])
    z = math.sqrt(x**2 + y**2)
    print(z)
    print('FINISH')

def menu():
    print('1. Test f1')
    print('2. Test f2')
    choice = int(input('Your selection (1 -> 2):'))
    if choice == 1:
        test1()
    elif choice == 2:
        test2()
menu()