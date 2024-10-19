num = int(input("Take a number: "))

k = 1
for i in range(1, num+1):
    for k in range(1,k+1):
        print("*", end="")
    k = k+2 
    print()   