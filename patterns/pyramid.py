num = int(input("Enter the number: "))

for i in range(0, num):
    # Print spaces
    for j in range(0, num-i-1):
        print(" ", end="")
    # Print stars
    for j in range(0, i+1):
        print("*", end=" ")
    print()


