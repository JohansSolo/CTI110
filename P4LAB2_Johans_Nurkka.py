# Johans Nurkka
# March 15, 2026
# P4LAB2
# Multiplies a positive user input by integers 0 - 12

'''
1) Determine the condition for the while loop; yes = run again, no = quit program
2) Prompt user to enter an integer
3) Define if statement to branch a less than 0 response; if input is less than 0
notify user that the program does not process negative values
4) Define else statement; for range and print outputs for
user input and range as multiples and their factors
5) Prompt user to reset the condition or exit the program
'''
# Set the condition for the while loop
run_again = "yes"

# Initiate the while loop logic
while run_again == "yes":

    # Prompt user to enter an integer
    try:
        user_input = int(input("Enter an integer: "))
    except ValueError:
        print("An error occured, please enter an integer")
        continue
    
    # Notify integer error if value is less than zero and prompt response to terminate or reset program
    if user_input < 0:
        print("This program does not handle negative numbers.")

    # If value is greater than zero proceed with program calculations and print outcomes
    else:
        for number in range(1, 13):
            print(f"{user_input} * {number} = {user_input * number}")

    # Prompt user to reset or close while loop
    run_again = input("Would you like to run the program again? ").lower()