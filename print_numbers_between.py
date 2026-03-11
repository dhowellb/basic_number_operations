# Make a command to print all the numbers squished between two numbers
def print_numbers_between():
    # Ask the user for the starting number. We use 'int' for whole numbers.
    first_number = int(input("\033[96mEnter the starting number: \033[0m"))
    
    # Ask the user for the ending number
    second_number = int(input("\033[96mEnter the ending number: \033[0m"))

    # Print a nice title showing what numbers we are looking between
    print("\033[96mNumbers between " + str(first_number) + " and " + str(second_number) + ":\033[0m")

    # Scenario 1: The first number is smaller than the second number
    if first_number < second_number:
        # Start the loop one number AFTER the first number ('+ 1')
        # The loop will automatically stop right before it hits the second number
        for i in range(first_number + 1, second_number):
            # Print the number in green text
            print("\033[92m" + str(i) + "\033[0m")
            
    # Scenario 2: The first number is bigger than the second number
    elif first_number > second_number:
        # We do the exact same thing, but we flip it so the smaller number goes first in our range!
        for i in range(second_number + 1, first_number):
            print("\033[92m" + str(i) + "\033[0m")
            
    # Scenario 3: The numbers are exactly the same
    else:
        # If they type "5 and 5", there are no numbers between them! Print a yellow warning.
        print("\033[93mThere are no numbers between them.\033[0m")
# This part tells the computer to actually start the program
if __name__ == "__main__":
    # Run the printing command we made at the top
    print_numbers_between()