# This program prints the multiplication table of a given number.
num = int(input("Enter a number: "))  # Ask the user to enter a number
for i in range(1, 11):  # Loop through numbers 1 to 10
    print(f"{num} x {i} = {num * i}")  # Print the multiplication result