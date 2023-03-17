from employee import Employee
employee_list = list()

def add_employee():
    while True:
        name = input('Enter employee name:')
        code = input('Enter employee code:')
        if len(name) > 20:
            continue
        if len(code) > 20:
            continue
        else:
            break
    while True:
        try:
            salary = float(input('Enter salary:'))
            allowance = float(input('Enter allowance:'))
            break
        except:
            print('error')
    employee_list.append(Employee(code, name, salary, allowance))
    print('add success')

def search_employee():
    search_name = input('Enter name to search:')
    names = [x for x in employee_list if x.name == search_name]
    if not names:
        print('Name not found')
    else:
        for name in names:
            name.display()

def remove_employee():
    search_name = input('Enter name to remove:')
    names = [x for x in employee_list if x.code == search_name]
    if not names:
        print('Code not found')
    else:
        for name in names:
            employee_list.remove(name)
        print('Remove success')

def print_list():
    employee_list.sort(key=lambda x:x.salary + x.allowance,reverse=True)
    for employee in employee_list:
        employee.display()

while True:
    print('1-Adding a new employee')
    print('2-Find data by name')
    print('3-remove employee by code')
    print('4-print the list base on money')
    print('5-Quit')
    try:
        choice = int(input('Enter choice(1 -> 5):'))
    except:
        print('sai cu phap')
    if choice not in range(1, 6):
        print('nhap tu 1 -> 6')
        continue
    elif choice == 1:
        add_employee()
        continue
    elif choice == 2:
        search_employee()
        continue
    elif choice == 3:
        remove_employee()
        continue
    elif choice == 4:
        print_list()
        continue
    elif choice == 5:
        print('Exit')
        break