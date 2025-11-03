###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.15 # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'

if is_bonus:

    bonus_amount = basic_salary * bonus_rate
   
    total_salary = basic_salary + bonus_amount
else:
   
    total_salary = basic_salary

print(f'Basic salary: {basic_salary} PLN')
print(f'Bonus included: {bonus_amount} PLN') # Wyświetla 0 jeśli nie ma premii
print(f'Total salary: {total_salary} PLN')