# Make a command to check if two numbers are different
def check_if_not_equal():
    # Ask the user to type the first number.
    # 'float' lets them type decimals if they want.
    first_number = float(input("\033[96mEnter the first number: \033[0m"))
    
    # Ask the user to type the second number.
    second_number = float(input("\033[96mEnter the second number: \033[0m"))

    # Check if the first number is different from the second number
    # (We use '!=' which means "not equal")
    if first_number != second_number:
        # If they are different, print "Not Equal" in green text
        print("\033[92mNot Equal\033[0m")
# This part tells the computer to actually start the program
if __name__ == "__main__":
    # Run the command we made at the top
    check_if_not_equal()