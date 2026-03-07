# Johans Nurkka
# March 3, 2026
# P3HW1_Debugging
# This program takes a number grade, determines average and displays letter grade for average.

'''
1. Prompt user to enter grades per module
2. Conatain grades in a list
3. Calculate min, max, sum, and average and assign them to variables
4. Print lowest and highest percentage, sum of grade percentages, and average grade percentage
5. Format conditional print statements assigning a letter grade for percentage ranges
'''
# Prompt user inputs for module grades

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
print()

# Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Calculate min, max, sum, and average

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Print results

print('-------------Results------------')
print(f'{"Lowest Grade:":<20} {low:<10.2f}')
print(f'{"Highest Grade:":<20} {high:<10.2f}')
print(f'{"Sum of Grade:":<20} {total:<10.2f}')
print(f'{"Average:":<20} {avg:<10.2f}')
print('--------------------------------')

# Determine and print letter grade for corresponding percentage

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')

# And as always keep the terminal open for review

print()
input('Press Enter to exit terminal')