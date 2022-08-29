#!/usr/bin/python3
def print_list_integer(my_list=[]):
<<<<<<< HEAD
    for n in my_list:
        print("{:d}".format(n))
=======
    """Print list of integers
    Args:
    size: length of list
    i: loop through list
    Returns:
     return nothing but prints my_list on a new line
    """
    size = len(my_list)
    for i in range (0, size):
        print("{}".format(my_list[i]))
>>>>>>> 2afe5b06763107c5c132849a00dbb5da0f2d1089
