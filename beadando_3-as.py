def prim(a):
    if a <=1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


def lnkpo(a, b):

    for i in range(b, 1, -1):
        if a % i == 0 and b % i == 0:
            if prim(i)==True:
                return i


print(lnkpo(123456,78932))