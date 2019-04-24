try:
    n = int(input("adj egy számot köcsög: "))
    ls = []
    while n != 0:
        ls.append(n)
        n = int(input("adj meg mégegy számot te nagyon köcsög:"))
    tomb = np.array(ls)
    print(tomb)

    x = np.arange(0,len(ls))
    print(x)
    tomb.sort()
    plt.plot(x,tomb, "bo")
    plt.show()
except ValueError:
    print("nem szám tesó")

