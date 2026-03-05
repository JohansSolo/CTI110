# Johans Nurkka
# March 2, 2026
# P3LAB
# Program prompts user to enter a dollar amount and calculates the most
# efficient return in whole dollars, quarters, dimes, nickles and pennies

'''
1. Prompt user for a dollar amount as a float.
2. Convert the amount to total cents as an integer for precision.
3. Calculate the number of whole dollars and find the remaining cents.
4. From the remaining cents, calculate quarters, dimes, nickels and pennies.
5. Display each denomination only if the count is greater than zero.
6. Apply proper singular/plural grammar for each printed denomination.
7. If the total is zero, display "no change"
'''

# Prompt user for dollar entry and calculate total amount avoiding floating point errors

user_amount = float(input("Enter a dollar amount: $"))
user_money_int = int(round(user_amount, 2))

# Calculate subsequent denominations utilizing floor division and modulus
#################################################################### Dollars

dollars = user_money_int // 100
user_money_int = user_money_int % 100

#################################################################### Quarters

quarters = user_money_int // 25
user_money_int = user_money_int % 25

#################################################################### Dimes

dimes = user_money_int // 10
user_money_int = user_money_int % 10

#################################################################### Nickles

nickels = user_money_int // 5
user_money_int = user_money_int % 5

#################################################################### Pennies

pennies = user_money_int

# Print conditional results with subject-verb agreement

if dollars > 0:
    if dollars == 1:
        print(f"{dollars} dollar")
    if dollars > 1:
        print(f"{dollars} dollars")
if quarters > 0:
    if quarters == 1:
        print(f"{quarters} quarter")
    if quarters > 1:
        print(f"{quarters} quarters")
if dimes > 0:
    if dimes == 1:
        print(f"{dimes} dime")
    if dimes > 1:
        print(f"{dimes} dimes")
if nickels > 0:
    print(f"{nickels} nickel")
if pennies > 0:
    if pennies == 1:
        print(f"{pennies} penny")
    if pennies > 1:
        print(f"{pennies} pennies")
else:
    print("no change")

# Keep terminal window open for review before closing
input("Press Enter to quit program")