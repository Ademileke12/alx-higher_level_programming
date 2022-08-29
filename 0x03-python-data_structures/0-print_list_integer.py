#!usr/bin/python3
def print_list_integer(my_list=[]):
    """Print list of integers

    Args:
    size: length of list
    i: loop through list

    Returns:
     return nothing but prints my_list[i]
    """
    size = len(my_list)
    for i in range(0, size):
        print("{}".format(my_list[i]))
