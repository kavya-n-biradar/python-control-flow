# Ask the user to enter an integer and store it in a variable
number = int(input("Enter an integer: "))

# % modulus operator returns the remainder of a division operation.
if number % 2 == 0: # Check if the number is even
    print("The number is even.")
else: # Check if the number is odd
    print("The number is odd.") 

# Check if the number is positive, negative, or zero
if number > 0:  # check if the number is positive
    print("The number is positive.")
elif number < 0:  # check if the number is negative
    print("The number is negative.")
else: # check if the number is zero
    print("The number is zero.")