class Book:
    def __init__(self, name, author, publisher, year, price):
        self._name = name
        self._author = author
        self._publisher = publisher
        self._year = year
        self._price = price

    @property
    def Ten_sach(self):
        return self._name

    @Ten_sach.setter
    def Ten_sach(self, value):
        self._name = value

    @property
    def Ten_tac_gia(self):
        return self._author

    @Ten_tac_gia.setter
    def Ten_tac_gia(self, value):
        self._author = value

    @property
    def Nha_xuat_ban(self):
        return self._publisher

    @Nha_xuat_ban.setter
    def Nha_xuat_ban(self, value):
        self._publisher = value

    @property
    def Nam_XB(self):
        return self._year

    @Nam_XB.setter
    def Nam_XB(self, value):
        self._year = value

    @property
    def Gia_ban(self):
        return self._price

    @Gia_ban.setter
    def Gia_ban(self, value):
        self._price = value

    def display(self):
        print(self.Ten_sach)
        print(self.Ten_tac_gia)
        print(self.Nha_xuat_ban)
        print(self.Nam_XB)
        print(self.Gia_ban)
        print('\n')
