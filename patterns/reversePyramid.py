

# The third parameter is for step means it gives u this 
# for i in range(1, 11, 2): 
#     print(i)

num = int(input("Enter number of rows: "))

for i in range(num, 0,  -1):
    for j in range(0, num - i):
        print(end=" ")

    for j in range(0, i):
        print("*", end=" ")
    print()
