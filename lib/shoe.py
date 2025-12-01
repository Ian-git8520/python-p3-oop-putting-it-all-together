class Shoe:
    def __init__(self, brand="", size=0):
        self.brand = brand
        self.size = size
        self.condition = ""

   
    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        if not isinstance(value, str):
            raise TypeError("brand must be a string")
        self._brand = value

    brand = property(get_brand, set_brand)

    
    def get_size(self):
        return self._size

    def set_size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        self._size = value

    size = property(get_size, set_size)

   
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
