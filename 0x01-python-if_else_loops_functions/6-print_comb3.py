#!/usr/bin/python3
for i in range(9):
    for j in range(i+1, 10):
        if(str(i) != str(j) and str(j) != str(i)):
            print('{0}{1}, '.format(i, j), end="")
