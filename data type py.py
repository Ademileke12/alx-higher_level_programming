"""#!/usr/bin/python3
def print_list_integer(my_list=[]):
    size = len(my_list)
    for i in range(0, size):
        my_list = i
        print("{}".format(i))
my_list = [1, 2, 3, 4, 5]
print(print_list_integer(my_list))
print(type(print_list_integer(my_list)))"""
"""my_list = [1, 2, 3, 4, 5]
size = len(my_list)
for i in range(0 ,size):
    print(print_list_integer(my_list[i]))"""

"""#!/usr/bin/python3
def element_at(my_list, idx):
    return my_lis, idx
my_list = [1, 2, 3, 4, 5]
lenth = len(my_list)
idx = int(input())
if idx in my_list:
    print("Element at index {} is {}".format(idx, my_list[idx]))
elif idx < 0:
    print("none")
elif idx > lenth:
    print("none")   return to be fixed"""
"""#!/usr/bin/python3
def replaace_in_list(my_list, idx, element):
    return my_list, idx, element
my_list = [1, 2, 3, 4, 5]
idx = int(input())
element = 9
index = my_list.index(idx)
my_list[index] = element
print(my_list)
left for idx negative and out of range"""

"""#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if idx < 0 or idx > size:
        return None
    else:
        return my_list[idx]

my_list =[1, 2, 3, 4, 5]
idx = int(input()) 
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))"""
"""#!/usr/bin/python3
def no_c(my_string):
    if ('C' not in my_string) and ('c' not in my_string):
        return
    else:
        my_string = my_string.translate({ord(i): None for i in 'cC'})
        return my_string
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))"""

"""def matric_print(matrix=[]):
    for i in range(len(matrix)):
        print("{}".format(matrix[i]))
matrix =[1,2,3,4,5]
print(matric_print(matrix))"""

"""def turp(turp=()):
    for i in turp:
        print("{}".format(turp(i)))
turple = (1, 2, 3, 4)
print(turp(turple))"""

"""Needs fixing
def divisible_by_2(my_list=[]):
    for i in my_list:
        list1_list = my_list
        index_list = list1_list.index(my_list[i])
        check_list = index_list % 2
        if check_list == 0:
            return check_list, True
        else:
            return check_list, False
my_list = [0, 1, 3, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))

   i += 1"""
'''import random
import string
def passw_a(length, password):
    if password in password:
        return ''.join(random.choice(password) for _ in range(length))
length = 14
passw = password = string.ascii_lowercase + string.digits + string.punctuation
print(passw_a(length, passw))'''
"""turples"""
"""def rem_list(n):
    if x in n:
        n.remove(x)
    return n
n = [1, 2, 3, 4, 5]

x = int(input())
print(n)
print(rem_list(n))"""
"""def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for x in new_matrix:
        new_matrix[0] = list(map(lambda x: x**2, range(3)))
    return (new_matrix matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

#list(map(lambda x: x**2, range(10)))"""
"""def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    if search in new_list:
        search = new_list.index(search)
        new_list[search] = replace
        return new_list
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)"""
"""def common_elements(set_1, set_2):
    if C in set1 and set2:
        return

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
"""
def uniq_add(my_list=[]):
    my_list = list(dict.fromkeys(my_list))
    total = sum(my_list)
    return total
my_list = [1, 2, 3, 1, 4, 2, 5]
print(uniq_add(my_list))
