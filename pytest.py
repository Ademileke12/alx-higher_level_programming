"""#!/usr/bin/python3
def add_integer(a, b=98):
   """ """ returns the addition of two integers """ """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    elif type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    else:
        return (int(a) + int(b))

The ``0-add_integer`` module
======================

Using ``add_integer``
-------------------

This is an example text file in reStructuredText format.  First import
``add_integer`` from the ``0-add_integer`` module:

    >>> from 0-add_integer import add_integer

Now use it:

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98"""
"""#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if type(first_name)!= str:
        raise TypeError('first_name must be a string' or 'last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
    
say_my_name("John", "Smith")
say_my_name("Walter", "White")

say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)"""
"""#!/usr/bin/python3
def print_square(size):
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    else:
        for i in range(size):
            print("{}".format(size * '#'))

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")"""
"""class Student:
    def __init__(self, name, matric, dept):
        self.name = name
        self.matric = matric
        self.dept = dept
    def getname(self):
        print( self.name)
    def getmatric(self):
        return(self.matric)
    def details(self):
       return self.name, self.matric, self.dept
        
s1 = Student("4","5","5")
print(s1.getmatric())"""


#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError('text must be a string')
    else:
        if '.' or '?' or ':' in text:
            text = text.replace(".", (("\n\n")))
            text = text.replace("?", (("\n\n")))
            text.replace(":", (("\n\n")))
            print(text)

text_indentation(""".Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \ 
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

"""def matrix_divided(matrix):
   for i in range(len(matrix)):
       return("{}".format(, end=""))
       

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix))
#print(matrix)"""
