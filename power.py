def power(x, y):
    if y == 0:
        return 1
    if x == 0 and y < 0:
        raise ZeroDivisionError
    if isinstance(y, int) and y > 0:
        result = x
        for i in range(y - 1):
            result *= x
        return result
    if isinstance(y, int) and y < 0:
        result = 1/x
        for i in range(-y - 1):
            result /= x
        return result
