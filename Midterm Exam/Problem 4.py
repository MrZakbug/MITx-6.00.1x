def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''

    exponent = 0
    result = 0
    previousResult = 0

    while result < num:
        previousResult = base ** (exponent - 1)
        result = base ** exponent
        exponent += 1

    if abs(num - previousResult) > abs(num - result):
        return exponent - 1
    else:
        return exponent - 2

print(closest_power(4, 62)) # example