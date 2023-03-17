class Drink:
    def __init__(self, name, make, volume, price, duration):
        self._name = name
        self._make = make
        self._volume = volume
        self._price = price
        self._duration = duration

    @property
    def make(self):
        return self._make

    @property
    def volume(self):
        return self._volume

    @property
    def price(self):
        return self._price
    def display(self):
        print(self._name)
        print(self._make)
        print(self._volume)
        print(self._price)
        print(self._duration)
