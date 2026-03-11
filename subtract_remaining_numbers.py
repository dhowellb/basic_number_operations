# Make a command to take a starting number and subtract 9 other numbers from it
def subtract_remaining_numbers():
    # Ask the user for the very first number. 
    # We save this as our starting point.
    first_number = float(input("\033[96mEnter number 1: \033[0m"))
    
    # We create a running total and set it equal to that first number
    total_result = first_number

    # Create a loop that will repeat the next steps exactly 9 times
    for i in range(9):
        # Ask the user to type the next number. 
        # 'str(i + 2)' makes it ask for "number 2", then "number 3", all the way to 10!
        current_number = float(input("\033[96mEnter number " + str(i + 2) + ": \033[0m"))
        
        # Subtract the new number they just typed from our running total
        total_result = total_result - current_number

    # After the loop finishes all 9 times, print the final answer in green text
    print("\033[92mThe result is:\033[0m", total_result)