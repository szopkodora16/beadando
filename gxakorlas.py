# import sys
# import numpy as np
# n1 = int(sys.argv[1])
# n2 = int(sys.argv[2])
# n3 = int(sys.argv[3])
# n4 = int(sys.argv[4])
#
# def matrixszorzas(n1,n2,n3,n4):
#     if n2 != n3:
#         return "A két mátrix nem összeszorozható"
#     mat1 = np.random.randint(1,5,(n1,n2))
#     print(mat1)
#     mat2 = np.random.randint(1,5,(n3,n4))
#     print(mat2)
#
#     eredm = np.random.randint(0,1,(n1,n4))
#
#     for k in range(n1):
#         for i in range(n4):
#             szam=0              #azért ide kell mert valahanyszor uj sorba megy le kell 0-ni
#             for j in range(n2):
#                 szam+=mat1[k,j] * mat2[j,i]
#             eredm[k,i] = szam
#
#     return eredm
#
#
# print(matrixszorzas(n1,n2,n3,n4))


import sys
try:
    n=int(sys.argv[1])
    for i in range(1,n+1):
        s=" "
        for j in range(1,i+1):          #hosszáfűzi a többi számot pl:1_hez 2,3-at..
            s+=str(j)
        a=s[::-1]                       #hosszáfűzi a forditottját
        s+=a[1:]                        #azért kell hogy a középső elemet ne ketszer irja ki és hogy hozzáfüzze az elözöeket is
        print("{:^40}".format(s))
except ValueError:
    print("Nem számot adtál meg!")