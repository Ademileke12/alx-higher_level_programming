"""#!/usr/bin/python3
#task0
class Square:
    pass
my_Square = Square()
print(type(my_Square))
print(my_Square.__dict__)
"""
"""#!/usr/bin/python3
#task1
class Square:
    __size = None

    

    def __init__(self, size):
        self.__size = size
        

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)"""

"""class Square:

    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)
try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)"""
"""class Square:
    
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        area = self.__size ** 2
        return area
#!/usr/bin/python3
#Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))"""

"""class Square:

    def __init__(self, size=0):
        self.__size = size
        
    @property   
    def size(self):
        return self.__size
        
    @size.setter   
    def size(self, size):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
    def area(self):
        area = (self.__size) ** 2
        return area
    
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
task4
    """
"""
task 5
class Square:
    def __init__(self, size=0):
        self.__size = size
        
    @property    
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
    def area(self):
        area = (self.__size) ** 2
        return area
    
    def my_print(self):
        for i in range(self.__size):
            print("{}".format("#" *(self.__size)))
            if self.__size == 0:
                print('')
my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")"""

class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
    def __init__(self, size=0, position=(0,0)):
        self.__position = position
        self.__size = size
        
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, size, position):
        if position[0] and position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        area = (self.__size) ** 2
        return area

    def my_print(self):
        for i in range(self.__size):
            print("{}".format("#" *(self.__size)))
            if self.__size == 0:
                print('')

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
