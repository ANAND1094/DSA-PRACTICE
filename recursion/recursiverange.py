from ast import Num


def recursiveRange(n):
#    assert n >=0 and int(n) ==n,'The number must be positive integer'
    if n <= 0:
        return 0
    else:
        return n + recursiveRange(n-1)
print(recursiveRange(7.8))