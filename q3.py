import itertools


class Employee:
    id_obj = itertools.count(1)

    def __init__(self, name, salary, age):
        self.id = next(Employee.id_obj)
        self.name = name
        self.salary = salary
        self.age = age


    def display(self):
        print(f'Employees {self.id}')
        print(self.name)
        print(self.salary)
        print(self.age)

    def getAge(self):
        return self.age

    def getSalary(self):
        return self.salary

def inputlistemployee():
    list_employ = list()
    n = int(input('Enter the number of employees:'))
    for i in range(1, n + 1):
        print('Enter employee',i)
        employee = Employee(input(), float(input()), int(input()))
        list_employ.append(employee)
    return list_employ

def sort_age():
    employees = inputlistemployee()
    ages = list()
    for employee in employees:
        ages.append(employee.age)
    ages.sort(reverse=True)
    for age in ages:
        for employee in employees:
            if employee.age == age:
                employee.display()
    print('FINISH')

def sort_salary():
    employees = inputlistemployee()
    salaries = list()
    for employee in employees :
        if employee.age >= 18:
            salaries.append(employee.salary)
    salaries.sort(reverse=True)
    for salary in salaries:
        for employee in employees:
            if employee.salary == salary:
                employee.display()
    print('FINISH')
def menu():
    print('1. Test f1')
    print('2. Test f2')
    print('3. Test f3')
    choice = int(input('Your Selection (1 -> 3):'))
    if choice == 1:
        list_employ = inputlistemployee()
        for employ in list_employ:
            employ.display()
    elif choice == 2:
        sort_age()
    elif choice == 3:
        sort_salary()

menu()







