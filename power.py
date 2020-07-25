class ToHardEquationError(Exception):
    pass


def power(base, exp):
    if exp == 0:
        return 1
    if base == 0 and exp < 0:
        raise ZeroDivisionError
    if isinstance(exp, int):
        result = base
        for _ in range(exp - 1):
            result *= base
        return result if exp > 0 else 1 / (result * base)
    raise ToHardEquationError
