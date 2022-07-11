def fabonacci(n):
    assert n >=0 and int(n) ==n,'The number must be positive integer'
    if n in [0,1]:
        return n
    else:
        return fabonacci(n-1) + fabonacci(n-2)

print(fabonacci(7))