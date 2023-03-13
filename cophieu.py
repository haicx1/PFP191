import itertools
from msilib.schema import Property


class Cophieu:
    id_obj = itertools.count(1)

    def __init__(self, name, dau, cuoi):
        self.id = next(Cophieu.id_obj)
        self._name = name
        self._dau = float(dau)
        self._cuoi = float(cuoi)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def dau(self):
        return self._dau

    @dau.setter
    def dau(self, value):
        self._dau = value

    @property
    def cuoi(self):
        return self._cuoi

    @cuoi.setter
    def cuoi(self, value):
        self._cuoi = value

    def sub(self):
        return self.cuoi - self.dau

    def cophieu(self):
        return self.dau, self.cuoi


class VIC(Cophieu):
    name_vic = 'VIC'
    def __init__(self, dau, cuoi):
        super().__init__('VIC', dau, cuoi)


class FLC(Cophieu):
    name_flc = 'FLC'
    def __init__(self, dau, cuoi):
        super().__init__('FLC', dau, cuoi)



class HSG(Cophieu):
    name_hsg = 'HSG'
    def __init__(self, dau, cuoi):
        super().__init__('VIC', dau, cuoi)
