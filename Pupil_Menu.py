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
    def name(self, name):
        self._name = name

    @property
    def mark_e(self):
        return self.mark_e

    @mark_e.setter
    def mark_e(self, mark_e):
        self._mark_e = mark_e

    @property
    def mark_m(self):
        return self._mark_m

    @mark_m.setter
    def mark_m(self, mark_m):
        self._mark_m = mark_m

    @property
    def mark_p(self):
        return self.mark_p

    @mark_p.setter
    def mark_p(self, mark_p):
        self._mark_p = mark_p

    @property
    def mark_chem(self):
        return self._mark_chem

    @mark_chem.setter
    def mark_chem(self, mark_chem):
        self._mark_chem = mark_chem

    @property
    def mark_cs(self):
        return self._mark_cs

    @mark_cs.setter
    def mark_cs(self, mark_cs):
        self._mark_cs = mark_cs

    def display(self):
        print('Roll number:', self._id)
        print('Name:', self._name)
        print('English:', self._mark_e)
        print('Maths:', self._mark_m)
        print('Physics:', self._mark_p)
        print('Chemistry:', self._mark_chem)
        print('CS:', self._mark_cs)


stuList = list()
search = False


def createStudent(arr):
    student = Student()
    arr.append(student)
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

def mod_student(roll_number):
    name = stuList[roll_number][1]
    e = stuList[roll_number][2]
    m = stuList[roll_number][3]
    p = stuList[roll_number][4]
    chem = stuList[roll_number][5]
    cs = stuList[roll_number][6]
    print('Name:',name)
    choice = input('Wants to edit(y/n)?')
    if choice == 'y' or choice == 'Y':
        name = input('Enter the name:')
    elif choice == 'n' or choice == 'N':
        print('Eng:',e)
        choice = input('Wants to edit(y/n)?')
        if choice == 'y' or choice == 'Y':
            e = input('English marks:')
        elif choice == 'n' or choice == 'N':
            return 0

def mod_student1(student = Student()):
    print('Name:', student.name)







while True:
    printMenu()
    try:
        choice = int(input('Enter choice(1-6):'))
    except:
        continue
    if choice not in range(1, 7):
        continue
    elif choice == 1:
        createStudent(stuList)
        while True:
            choice_1 = input('Wants to enter more record (y/n):')
            if choice_1 == 'y' or choice_1 == 'Y':
                createStudent(stuList)
                continue
            elif choice_1 == 'n' or choice_1 == 'N':
                break
        continue
    elif choice == 2:
        for student in stuList:
            student.display()
        choice2 = input('Do you want to continue the program ?(y/n)')
        if choice2 == 'y' or 'Y':
            continue
        elif choice2 == 'n' or 'N':
            print('Exit program')
            break
    elif choice == 3:
        roll = int(input('Enter rollno you want to search:'))
        for student in stuList:
            if student.id() == roll:
                print('PUPIL DETAIL..')
                student.display()
                search = True
                break
        if search == False:
            print('No result')
        printMenu1()
        while True:
            try:
                choice1 = int(input('Enter choice(1-3):'))
            except:
                print('Invalid input')
            if choice > 3:
                continue
            else:
                break
        if choice1 == 3:
            print('EXIT PROGRAM')
            break
        if choice1 == 1:
            continue
    elif choice == 4:
        print('MODIFY RECORD')
        roll_4 = int(input('Enter roll number:'))
        for student in stuList:
            if student._id == roll_4:
                modify_stu = student
                break
        print('Name:', student.name)
        print()
