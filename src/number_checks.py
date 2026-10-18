# Program to classify an integer as even or odd, and as positive, negative or zero

# Ask the user to enter an integer and store it in a variable
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    # % modulus operator returns the remainder of a division operation.
    # A remainder of 0 when dividing by 2 means the number is even.
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

    # Check if the number is positive, negative, or zero
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")