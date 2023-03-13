import itertools


class Location:
    id_object = itertools.count(1)
    def __init__(self, name, hr, mins):
        self._id = next(Location.id_object)
        self._name = name
        self._hr = hr
        self._mins = mins

    @property
    def hr(self):
        return self._hr

    @hr.setter
    def hr(self, value):
        self._hr = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def mins(self):
        return self._mins

    @mins.setter
    def mins(self, value):
        self._mins = value
