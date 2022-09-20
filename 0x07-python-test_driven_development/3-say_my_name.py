#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))