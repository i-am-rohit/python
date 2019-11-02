def hollow(n):
    k = 0
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end="")

        while (k != (2 * i - 1)):
            if (k == 0 or k == 2 * i - 2):
                print("*", end="")
            else:
                print(" ", end="")
            k = k + 1
        k = 0
        print("")
    n = n - 1



    for i in range(n, 0, -1):
        for j in range(0, n - i + 1):
            print(" ", end="")
        k = 0
        while (k != (2 * i - 1)):
            if (k == 0 or k == 2 * i - 2):
                print("*", end="")
            else:
                print(" ", end="")
            k = k + 1
        print("")


n = 5
hollow(n)

