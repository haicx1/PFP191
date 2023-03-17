class Employee:
    def __init__(self, code, name, salary, allowance):
        self._code = code
        self._name = name
        self._salary = salary
        self._allowance = allowance

    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, value):
        self._code = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        self._salary = value

    @property
    def allowance(self):
        return self._allowance

    @allowance.setter
    def allowance(self, value):
        self._allowance = value


    def display(self):
        print(self.code)
        print(self.name)
        print(self.salary)
        print(self.allowance)