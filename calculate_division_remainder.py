# Make a command to divide two numbers and keep ONLY the leftover remainder
def calculate_remainder():
    # Ask the user for the first number. 
    # 'float' lets them type decimals if they want.
    first_number = float(input("\033[96mEnter the first number: \033[0m"))
    
    # Ask the user for the second number.
    second_number = float(input("\033[96mEnter the second number: \033[0m"))

    # Check to make sure the second number is not zero 
    # (because dividing by zero breaks the computer's math!)
    if second_number != 0:
        # The '%' symbol divides the numbers but only saves the leftover remainder part.
        division_remainder = first_number % second_number
        
        # Print the final leftover remainder in green text
        print("\033[92mThe remainder is:\033[0m", division_remainder)
        
    # If the second number IS zero, do this instead:
    else:
        # Print an error message in red text so the user knows what went wrong
        print("\033[91mCannot divide by zero.\033[0m")