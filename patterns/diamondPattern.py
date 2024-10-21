def pyramid(rows):
    # Print the upper part of the pyramid
    for i in range(rows):
        print(' ' * (rows - i - 1) + '* ' * (i + 1))

    # Print the lower part of the pyramid
    for j in range(rows - 1, 0, -1):
        print(' ' * (rows - j) + '* ' * j)

# Get user input
try:
    user_input = int(input("Enter the number of rows for the pyramid: "))
    pyramid(user_input)
except ValueError:
    print("Please enter a valid integer.")
