# Make a command to subtract one number from another
def calculate_difference():
    # Ask the user for the first number. 
    # 'float' lets them type decimals if they want to.
    first_number = float(input("\033[96mEnter the first number: \033[0m"))
    
    # Ask the user for the second number.
    second_number = float(input("\033[96mEnter the second number: \033[0m"))
    
    # Subtract the second number from the first number using the '-' minus sign
    total_difference = first_number - second_number

    # Print the final subtracted answer in green text
    print("\033[92mThe difference is:\033[0m", total_difference)