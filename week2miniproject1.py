###################################
# Name:         Brendan Obilo
# Reg No:       100952871
# Description:  A program that processes the employee's name
#               and calculating their earnings for the week
# Date:         14/05/2024
####################################

# asks for the user
employee_name = input('Please enter your fullname: ')
# asks for hourly wage
hourly_wage = input('Please enter your hourly wage: ')
# asks how many hours per week
hours_per_week = input('Please enter how many hours this week: ')

# calculate the weekly earning
weekly_earning = float(hourly_wage) * float(hours_per_week)
# To remove white spaces and capitalize first letter of each word
formated_name = employee_name.strip().title()

# Displays required output of the week earning
print(f"{formated_name} earned ${weekly_earning} this week")