# This program prints the multiplication table of a given number.
num = int(input("Enter a number: "))  # Ask the user to enter a number
for i in range(1, 11):  # Loop through numbers 1 to 10
    print(f"{num} x {i} = {num * i}")  # Print the multiplication result



# This part finds the sum of the first N natural numbers using a while loop.
n = int(input("Enter a value for N: "))

if n < 1:
    # Natural numbers start from 1, so zero or negative N has no numbers to add
    print("N must be 1 or more, so the sum is 0.")
else:
    total = 0    # running total, starts at 0
    count = 1    # the number being added, starts at 1

    while count <= n:
        total = total + count   # add the current number to the total
        count = count + 1       # move to the next number

    print(f"The sum of the first {n} natural numbers is {total}.")


# This part prints a right-angled triangle of asterisks.
rows = int(input("Enter the number of rows: "))

if rows < 1:
    # A triangle needs at least one row
    print("Rows must be 1 or more to draw a triangle.")
else:
    for i in range(1, rows + 1):   # i is the current row number
        print("*" * i)             # row i has i stars