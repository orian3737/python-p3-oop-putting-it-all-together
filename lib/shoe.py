#!/usr/bin/env python3
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
            self._size = None

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
