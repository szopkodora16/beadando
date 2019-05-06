def prim(a):
    if a < 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(2, a // 2):
        if a % i == 0:
            return False
    return True


def lnkpo(a, b):
    if a < b:
        c = a
    else:
        c = b

    for i in range(c, 1, -1):
        if a % i == 0 and b % i == 0:
            if prim(i):
                return i


print(lnkpo(17,34))