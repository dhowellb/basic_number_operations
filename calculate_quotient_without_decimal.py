# Make a command to divide two numbers and keep only the whole number
def calculate_floor_quotient():
    # Ask the user for the first number. 
    # 'float' lets them type decimals if they want.
    first_number = float(input("\033[96mEnter the first number: \033[0m"))
    
    # Ask the user for the second number.
    second_number = float(input("\033[96mEnter the second number: \033[0m"))

    # Check to make sure the second number is not zero 
    # (because dividing by zero breaks the computer's math!)
    if second_number != 0:
        # Divide using the '//' double slash. This chops off the decimal part.
        # We also use 'int()' to make sure the computer treats it as a strict whole number.
        floor_quotient = int(first_number // second_number)
        
        # Print the final whole number answer in green text
        print("\033[92mThe quotient without decimal is:\033[0m", floor_quotient)
        
    # If the second number IS zero, do this instead:
    else:
        # Print an error message in red text so the user knows what went wrong
        print("\033[91mCannot divide by zero.\033[0m")
# This part tells the computer to actually start the program
if __name__ == "__main__":
    # Run the floor quotient command we made at the top
    calculate_floor_quotient()