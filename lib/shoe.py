#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size

   
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        elif value < 0:
            print("size must be greater than or equal to 0")
        else:
            self._size = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
