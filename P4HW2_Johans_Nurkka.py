# Johans Nurkka
# March 27, 2026
# P4HW2
# This program calculates pay for multiple employees,
# including overtime and regular pay totals

'''
1) Initialize totals:
    total_overtime_pay = 0
    total_regular_pay = 0
    total_gross_pay = 0
    employee_count = 0
2) Ask user for employee name
3) While employee name is not "Done":
    a) Ask for hours worked
    b) Ask for pay rate
    c) If hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (pay_rate 8 1.5)
        regular_pay = 40 * pay_rate
    d) Else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * pay_rate
    e) gross_pay = regular_pay + overtime_pay
    f) Add to totals:
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        employee_count =+ 1
    g) Display employye breakdown
    h) Ask for next employee name
4) After loop ends: Display totals and number of employees
'''

# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# sentinel loop
employee_name = input('Enter employee name or "Done" to terminate: ')

while employee_name != "Done":

    hours = float(input('Enter number of hours worked: '))
    pay_rate = float(input('Enter pay rate: '))

    # Calculate pay
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * pay_rate

    gross_pay = regular_pay + overtime_pay

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count =+ 1

    # Display employee info
    print(f'\nEmployee name: {employee_name}')
    print(f'Hours Worked: {hours}')
    print(f'Pay Rate: {pay_rate}')
    print(f'OverTime Hours: {overtime_hours}')
    print(f'OverTime Pay: ${overtime_pay:,.2f}')
    print(f'Regular Pay: ${regular_pay:,.2f}')
    print(f'Gross Pay: ${gross_pay:,.2f}')

    # Next employee
    employee_name = input('\nEnter employee name or "Done" to terminate: ')

# Final totals
print('\n------------Summary------------')
print(f'Total number of employees entered: {employee_count}')
print(f'Total amount paid for overtime: ${total_overtime_pay}')
print(f'Total amount paid for regular hours: ${total_regular_pay}')
print(f'Total amount paid in gorss: ${total_gross_pay}')