# Johans Nurkka
# March 23, 2026
# P4HW1
# Prompts user to input grade range and grades, and returns lowest grade, modified list, average, and letter grade for entered values

'''
1) Prompt user to enter the number of scores they would like calculated as an integer input;
use while loop to trap try/except to correct erroneous input
2) Create a list (grades) to contain scores entered
3) Create a for loop to solicit scores for list (grades) and calculations;
loop variable number for user defined range starting at 1 and spanning user input + 1
4) Format score as a user prompt "Enter score #number: "
5) Build while loop for invalid inputs setting score as the condition
6) Append valid inputs to list (grades)
7) Print results statement
8) print lowest grade using min(grades)
9) Define and print avg
10) Build if/elif for score to letter grade and print letter grade
11) Prompt input for program evaluation
'''

# Prompt user to enter the number of scores they would like calculated as an integer input
user_input = None

while user_input is None:
    try:
        user_input = int(input("How many scores do you want to enter? "))
    except:
        print('Invalid input! Enter a valid numeric integer.')

# Create a list (grades) to contain scores entered
grades = []

# Create a for loop to solicit scores for list (grades) and calculations;
# loop variable i for user defined range starting at 1 and spanning user input + 1

for number in range(1, user_input + 1):
    
    # Format score as a user prompt "Enter score #i: "
    score = float(input(f"Enter score #{number}: "))
    # Build while loop for invalid inputs setting score as the condition
    while score < 0 or score > 100:
        print("INVALID Score Entered!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{number}: "))
    # Append valid inputs to list (grades)
    grades.append(score)

print()

# Assign values to variables
lowest = min(grades)
grades.remove(lowest)
avg = sum(grades)/len(grades)

if avg >= 90:
    letter_grade = 'A'
elif avg >= 80:
    letter_grade = 'B'
elif avg >= 70:
    letter_grade = 'C'
elif avg >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Print results statements
print(f'{'-' * 12}Results{'-' * 12}')
print(f'{'Lowest Score':<15} : {lowest:.1f}')
print(f'{'Modified List':<15} : {grades}')
print(f'{'Scores Average':<15} : {avg:.2f}')
print(f'{'Grade':<15} : {letter_grade}')
print("-------------------------------")

# Allow user to inspect before exit
input("Press Enter to Exit Program")