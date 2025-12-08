###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 4
elif month >= 4:
    quarter = 2
elif month >= 1:
    quarter = 1
else:
    print('There is 12 months in the calendar dummy....')

print(f'Month {month} is in quarter {quarter}')