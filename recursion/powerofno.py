def power(base, exp):
    assert exp >=0 and int(exp)==exp,"The exponent must be positive integer"
    if exp == 0:
        return 1
    if base == 1:
        return base


    return base * power(base, exp-1)

print(power(2,4))