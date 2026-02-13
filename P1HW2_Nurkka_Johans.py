# Johans Nurkka
# 12 February 2026
# P1HW2
# Simple budget calculator

# Display banner to explain purpose of the program

print("----This program calculates and displays travel expenses----")
print()
print()

# Prompt user to enter travel budget, planned expenses, and destination

budget = float(input("Enter Budget: "))
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
hotel = float(input("Approximately, how much will you need for accomodations/hotel? "))
print()
food = float(input("Lastly, how much do you need for food? "))
print()
destination = input("Enter your travel destination: ")
print()
print()

# Add user expenses to determine total deductions and subtract them from budget to determine balance

deductions = gas + hotel + food
balance = budget - deductions

# Display formatted travel expense summary

print("------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:,.2f}")
print()
print(f"Fuel: ${gas:,.2f}")
print(f"Accomodation: ${hotel:,.2f}")
print(f"Food: ${food:,.2f}")
print()
print(f"Remaining Balance: ${balance:,.2f}")
print()

# If remaining balance is less than zero display warning; otherwise display positive reinforcement; pause script until user quits program

if balance < 0:
    print("Good news! You'll be enjoying more of the wonderful outdoors than you had initially anticipated 😁!")
else:
    print("Have a wonderful trip 😊!")
print()
input("Press Enter to Quit Program")