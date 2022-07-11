from numpy import extract


def sumofDigit(n):
    assert n >=0 and int(n)==n,'The number must be positive number'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigit(int(n//10))

print(sumofDigit(18))