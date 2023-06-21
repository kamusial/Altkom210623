def add(x, y):
    return x + y


def multiplication(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and a > 0 and b > 0:
        return round(a * b)
    elif isinstance(b, str) or isinstance(a, str):
        return a * b
    return 0


def fissbuzz(i):
    if isinstance(i, (int, float)) and i > 0:
        i = round(i)
        if i % 3 == 0 and i % 5 == 0:
            return 'fissbuzz'
        elif i % 3 == 0:
            return 'fiss'
        elif i % 5 == 0:
            return 'buzz'
        return i
    return 0
