def prim(a):
    if a <= 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

print(prim(1))