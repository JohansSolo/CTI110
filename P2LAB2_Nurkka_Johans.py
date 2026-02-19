# Johans Nurkka
# February 17, 2026
# P2LAB2
# Program that looks up a vehicle's MPG from a dictionary
# and calculates fuel required based on trip distance

# Define vehicle dictionary

vehicle = {'camaro': 18.21,
           'prius': 100,
           'model s': 110,
           'silverado': 2
}

# Create & print variable for dictionary keys

keys = vehicle.keys()
values = vehicle.values()
print(keys)

# Prompt user for vehicle input

user_key = input("Enter a vehicle to see its mpg: ").lower()

# Display value output for user key & update dictionary if necessary
if user_key in vehicle:
    print(f"The {user_key} gets {vehicle[user_key]} mpg")
else:
    print(f"Sorry, {user_key} not found.")
    vehicle[f'{user_key}'] = float(input("Enter estimated mpg: "))
    print(f"Updated Dictionary: {vehicle}")

# Prompt user for trip length, calculate consumption and print gas needed for trip

trip = float(input(f"How many miles will you drive the {user_key}? "))
gas = trip/vehicle[user_key]
print(f"{gas: .2f} gallon(s) of gas are needed to drive the {user_key} {trip} miles")

input("Press Enter to Exit")