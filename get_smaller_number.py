# Make a command to find the smaller number
def get_smaller_number():
    # Ask the user for the first number.
    # 'float' lets them type decimals.
    first_number = float(input("\033[96mEnter the first number: \033[0m"))
    
    # Ask the user for the second number.
    second_number = float(input("\033[96mEnter the second number: \033[0m"))

    # Check if the first number is smaller than the second number
    # (We use the '<' sign which means "less than")
    if first_number < second_number:
        # If it is smaller, print the first number in green
        print("\033[92mThe smaller number is:\033[0m", first_number)
        
    # Check if the second number is smaller instead
    elif second_number < first_number:
        # If it is smaller, print the second number in green
        print("\033[92mThe smaller number is:\033[0m", second_number)
        
    # If neither is smaller, they must be exactly the same
    else:
        # Print that they are equal in yellow
        print("\033[93mBoth numbers are equal.\033[0m")