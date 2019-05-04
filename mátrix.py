import tomb as np
def valami(m,n):
    c=0
    for i in range(0,len(m)):
        c += n[i]*m[i]
    return c
m=np.random.randint(10,50,10)
print(m)
n=np.random.randint(10,50,10)
print(n)
print(valami(m,n))
