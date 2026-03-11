# Make a command to find and print all odd numbers up to 100 using a 'while' loop
def print_odd_numbers():
    # Print a title message in cyan text so the user knows what is happening
    print("\033[96mOdd numbers from 0 to 100:\033[0m")
    
    # Start our counting number at zero
    current_number = 0

    # Keep repeating the next steps over and over AS LONG AS the number is 100 or less
    while current_number <= 100:
        # The '%' symbol finds the remainder after dividing by 2.
        # If the remainder is NOT zero ('!=' means not equal), it is an odd number!
        if current_number % 2 != 0:
            # Print the odd number we just found in green text
            print("\033[92m" + str(current_number) + "\033[0m")
            
        # Add 1 to our number so we can move on to check the next one.
        # (If we forget this step, the computer will check '0' forever and freeze!)
        current_number = current_number + 1
# This part tells the computer to actually start the program
if __name__ == "__main__":
    # Run the while loop command we made at the top
    print_odd_numbers()