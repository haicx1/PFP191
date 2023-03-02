import itertools


class Student:
    stuCount = 0
    id_obj = itertools.count()

    def __init__(self):
        self._id = next(Student.id_obj)
        self._name = input('Enter student name:')
        self._mark_e = int(input('Enter English mark:'))
        self._mark_m = int(input('Enter Math mark:'))
        self._mark_p = int(input('Enter Physic mark:'))
        self._mark_chem = int(input('Enter Chemistry mark:'))
        self._mark_cs = int(input('Enter Computer Science mark:'))

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def mark_e(self):
        return self._mark_e

    @mark_e.setter
    def mark_e(self, value):
        self._mark_e = value

    @property
    def mark_m(self):
        return self._mark_m

    @mark_m.setter
    def mark_m(self, value):
        self._mark_m = value

    @property
    def mark_p(self):
        return self._mark_p

    @mark_p.setter
    def mark_p(self, value):
        self._mark_p = value

    @property
    def mark_chem(self):
        return self._mark_chem

    @mark_chem.setter
    def mark_chem(self, value):
        self._mark_chem = value

    @property
    def mark_cs(self):
        return self._mark_cs

    @mark_cs.setter
    def mark_cs(self, value):
        self._mark_cs = value

    def display(self):
        print('Roll number:', self._id)
        print('Name:', self._name)
        print('English:', self._mark_e)
        print('Maths:', self._mark_m)
        print('Physics:', self._mark_p)
        print('Chemistry:', self._mark_chem)
        print('CS:', self._mark_cs)


stuList = list()


def create_student(arr):
    student1 = Student()
    arr.append(student1)
    while True:
        choice_1 = input('Wants to enter more record (y/n):')
        if choice_1 == 'y' or choice_1 == 'Y':
            create_student(stuList)
            break
        elif choice_1 == 'n' or choice_1 == 'N':
            break
    return arr


def printMenu():
    print('ADMIN MENU')
    print('1. CREATE PUPIL RECORD')
    print('2. DISPLAY ALL PUPIL RECORDS')
    print('3. SEARCH PUPIL RECORD')
    print('4.MODIFY PUPIL RECORD')
    print('5. DELETE PUPIL RECORD')
    print('6. BACK TO MAIN MENU')


def printMenu1():
    print('MAIN MENU')
    print('1. REPORT MENU')
    print('2. ADMIN MENU')
    print('3. EXIT')


def mod_student1(student):
    print('Name:', student.name)
    choice = input('Wants to edit(y/n)?')
    if choice == 'y' or choice == 'Y':
        student.name = input('Enter the name:')
    print('English marks:', student.mark_e)
    choice_e = input('Wants to edit(y/n)?')
    if choice_e == 'y' or choice_e == 'Y':
        student.mark_e = int(input('Enter mark:'))
    print('Math marks:', student.mark_m)
    choice_m = input('Wants to edit(y/n)?')
    if choice_m == 'y' or choice_m == 'Y':
        student.mark_m = int(input('Enter mark:'))
    print('Physics marks:', student.mark_p)
    choice_p = input('Wants to edit(y/n)?')
    if choice_p == 'y' or choice_p == 'Y':
        student.mark_p = int(input('Enter mark:'))
    print('Chemistry marks:', student.mark_chem)
    choice_ch = input('Wants to edit(y/n)?')
    if choice_ch == 'y' or choice_ch == 'Y':
        student.mark_ch = int(input('Enter mark:'))
    print('CS marks:', student.mark_cs)
    choice_cs = input('Wants to edit(y/n)?')
    if choice_cs == 'y' or choice_cs == 'Y':
        student.mark_cs = int(input('Enter mark:'))
    student.display()


def search_student(rollnumber):
    search = False
    for student in stuList:
        if student.id == rollnumber:
            print('PUPIL DETAIL..')
            student.display()
            return student
            break
        if not search:
            print('No result')

def del_student(rollnumber):
    delete = False
    for student in stuList:
        if student.id == rollnumber:
            stuList.remove(student)
            delete = True
        print('record found and deleted')
        break
    if not delete:
        print('rollnumber not found')



def main_menu():
    printMenu1()
    while True:
        try:
            choice_main = int(input('Enter choice(1-3):'))
        except:
            print('invalid input')
        if choice_main == 1:
            report_menu()
        elif choice_main == 2:
            return True
            break
        elif choice_main == 3:
            return False
            break


def report_menu():
    print('REPORT MENU')
    print('1. CLASS RESULT')
    print('2. PUPIL REPORT CARD')
    print('3. BACK TO MAIN MENU')
    while True:
        try:
            choice_report = int(input('Enter choice(1-4):'))
        except:
            print('error')
        if choice_report == 1:
            print('Rollno   Name      English  Maths  Physics  Chemistry  CS')
            for student in stuList:
                print(student.id,student.name,student.mark_e,student.mark_m,student.mark_p,student.mark_chem,student.mark_cs)
            continue
        if choice_report == 2:
            roll = int(input('Enter the rollno you want to search:'))
            search_student(roll)
            continue
        if choice_report == 3:
            break
            main_menu()


while True:
    printMenu()
    try:
        choice = int(input('Enter choice(1-6):'))
    except:
        continue
    if choice not in range(1, 7):
        continue
    elif choice == 1:
        create_student(stuList)
        continue
    elif choice == 2:
        for student in stuList:
            student.display()
        continue
    elif choice == 3:
        roll = int(input('Enter rollno you want to search:'))
        search_student(roll)
        main_menu()
    elif choice == 4:
        print('MODIFY RECORD')
        roll_4 = int(input('Enter roll number:'))
        mod_student1(stuList[roll_4])
        stuList[roll_4].display()
        continue
    elif choice == 5:
        print('DELETE RECORD')
        del_number = int(input('Enter roll number'))
        del_student(del_number)
        continue
    elif choice == 6:
        isRunning = True
        print('Back to main menu')
        isRunning = main_menu()
        if isRunning:
            continue
        else:
            print('EXITING')
            break

