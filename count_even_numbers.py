# Make a command to ask for 10 numbers and count how many are even
def count_even_numbers():
    # Start a counter at zero to keep track of the even numbers we find
    even_count = 0

    # Create a loop that will repeat the next steps exactly 10 times
    for i in range(10):
        # Ask the user to type a whole number. 
        # We use 'int' (integer) instead of 'float' because odd/even only works on whole numbers.
        current_number = int(input("\033[96mEnter integer number " + str(i + 1) + ": \033[0m"))
        
        # The '%' symbol finds the remainder after dividing by 2.
        # If the remainder is exactly zero ('==' means exactly equal), the number is even!
        if current_number % 2 == 0:
            # Add 1 to our running tally of even numbers
            even_count = even_count + 1

    # After the loop finishes checking all 10 numbers, print the final count in green text
    print("\033[92mTotal even numbers:\033[0m", even_count)
# This part tells the computer to actually start the program
if __name__ == "__main__":
    # Run the counting command we made at the top
    count_even_numbers()