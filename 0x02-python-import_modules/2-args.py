#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenthT = len(sys.argv)
    if lenthT <= 1:
        print("0 arguments.")
    else:
        if lenthT == 1:
            print("{} arguments:".format(lenthT))
        else:
            print("{} argument:".format(lenthT - 1))
            for i in range(1, lenthT):
                print("{}: {}".format(i, sys.argv[i]))
