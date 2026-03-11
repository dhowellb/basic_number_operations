# Make a command to print numbers up to 100, but skip the ones ending in 0 or 5
def print_numbers_except_zero_five():
    # Print a title message in cyan text so the user knows what is happening
    print("\033[96mNumbers from 0 to 100 except those ending in 0 or 5:\033[0m")

    # Create a loop that goes from 0 all the way to 100
    for i in range(101):
        # Dividing by 10 and keeping the remainder ('% 10') is a clever trick 
        # to find the very last digit of any number!
        last_digit = i % 10
        
        # Check if the last digit is NOT zero AND the last digit is NOT five.
        # Both of these rules must be true for the computer to move to the next line.
        if last_digit != 0 and last_digit != 5:
            # If it passes both tests, print the number in green text
            print("\033[92m" + str(i) + "\033[0m")
# This part tells the computer to actually start the program
if __name__ == "__main__":
    # Run the printing command we made at the top
    print_numbers_except_zero_five()