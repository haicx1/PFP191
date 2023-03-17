from collections import OrderedDict
student_name = OrderDict()
def print_menu():
    print('1-Add a student')
    print('2-Remove a student')
    print('3-Search a student')
    print('4-Print the list in ascending order')
    print('5-Quit')

def add_student():
    name = input('Enter student name:').split()
    new_name = ''.join(name).upper()
    student_name[name] = new_name
    print(student_name)

def remove_student():
    name = input('Enter student name want to remove:')
    if name in student_name:
        student_name.remove(name)
        print('remove sucess')
    else:
        print('Name not found')

def search_student():
    name = input('Enter student name want to search:')
    if name in student_name.keys():
        print(name,':',student_name[name] )
    else:
        print('Name not found')

def print_list():
    for key,value in student_name.items():
        print(f'{key}: {value}')

while True:
    print_menu()
    try:
        choice = int(input('Enter choice(1 -> 5):'))
    except:
        print('sai cu phap')
    if len(student_name.keys()) > 100:
        break
    if choice not in range(1,6):
        print('nhap tu 1 -> 6')
        continue
    elif choice == 1:
        add_student()
        continue
    elif choice == 2:
        remove_student()
        continue
    elif choice == 3:
        search_student()
        continue
    elif choice == 4:
        print_list()
        continue
    elif choice == 5:
        print('Exit')
        break