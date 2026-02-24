# Johans Nurkka
# 23 February, 2026
# P2HW2
# Making lists and using for loops

# Prompt user for list inputs

print("Eneter your final grade percentage for the following exams:")
print()

# Create a list and store user inputs

grades = []

for number in range(1, 7):
    score = float(input(f"Module {number}: "))
    grades.append(score)
print()
# Calculate outputs for lowest grade, highest grade, sum of grades & average

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total/len(grades)


print("------------Results------------")
print(f"{"Lowest Grade:":<20} {lowest:>10.2f}")
print(f"{"Highest Grade:":<20} {highest:>10.2f}")
print(f"{"Sum of Grades:":<20} {total:>10.2f}")
print(f"{"Average:":<20} {average:>10.2f}")
print("-------------------------------")