def print_pyramid(num, curr=0):
    if curr == num:
        return
    
    print(" " * (num - curr - 1), end="")

    print("* " * (curr + 1))

    print_pyramid(num, curr + 1)


num = int(input("Enter the number: "))
print_pyramid(num)