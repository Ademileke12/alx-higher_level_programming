#!/usr/bin/python3
def no_c(my_string):
    if ('C' not in my_string) and ('c' not in my_string):
        return
    else:
        my_string = my_string.translate({ord(i): None for i in 'cC'})
    return my_string
