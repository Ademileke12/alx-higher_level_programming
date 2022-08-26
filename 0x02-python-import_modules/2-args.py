#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenthT = len(sys.argv)
    if lenthT <= 1:
        print("{} arguments.".format(lenthT - 1))
    else:
        if lenthT == 2:
            print("{} argument:".format(lenthT - 1))
            for i in range(1, lenthT):
                print("{}: {}".format(i, sys.argv[i]))
        else:
            print("{} arguments:".format(lenthT - 1))
            for i in range(1, lenthT):
                print("{}: {}".format(i, sys.argv[i]))
