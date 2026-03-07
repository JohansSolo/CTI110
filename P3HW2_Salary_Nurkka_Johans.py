# Johans Nurkka
# March 6, 2026
# P3HW3 Salary
# Salary plus overtime calculator

'''
1. Prompt user input for name
2. Prompt user input for number of hours worked this week
3. Prompt user input for pay rate
4. Conditionally format hours for regular hours and overtime hours using if/else statement
5. Determine pay for regular pay, overtime pay and gross pay
6. Print: Name, rate, hours worked, overtime hours, overtime pay, regular pay, gross pay
'''
# Generate prompts for user inputs: Name, Hours, Rate

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))
print("-" * 100)

# Determine overtime and corresponding hours and overtime

if hours > 40:
    reg_hours = 40
    overtime = hours - 40
else:
    reg_hours = hours
    overtime = 0

# Determine pay rates and salaries

reg_pay = reg_hours * rate
over_pay = overtime * rate * 1.5
gross = reg_pay + over_pay

# Print results format for asthetics

print(f"{"Hours Worked":<17} {"Pay Rate":<13} {"OverTime":<13} {"OverTime Pay":<17} {"RegHour Pay":<16} {"Gross Pay":<17}")
print("-" * 100)
print(f"{hours:<17} {rate:<13.2f} {overtime:<13} ${over_pay:<17,.2f} ${reg_pay:<16,.2f} ${gross:<17,.2f}")

# My signature move

print()
input("Press Enter to exit terminal")