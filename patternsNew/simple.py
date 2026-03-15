def simplePattern(size):
    for i in range(size):
        for j in range(size):
            print('*', end=' ')
        print()

n = int(input("Enter the size of the pattern: "))
simplePattern(n)
