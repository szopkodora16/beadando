import sys
import numpy as np
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
n3 = int(sys.argv[3])
n4 = int(sys.argv[4])

def matrixszorzas(n1,n2,n3,n4):
    if n2 != n3:
        return "A két mátrix nem összeszorozható"
    mat1 = np.random.randint(1,5,(n1,n2))
    print(mat1)
    mat2 = np.random.randint(1,5,(n3,n4))
    print(mat2)

    eredm = np.random.randint(1,5,(n1,n4))

    for k in range(n1):
        for i in range(n4):
            szam = 0
            for j in range(n2):
                szam += mat1[k,j] * mat2[j,i]
            eredm[k,i] = szam

    return eredm


print(matrixszorzas(n1,n2,n3,n4))