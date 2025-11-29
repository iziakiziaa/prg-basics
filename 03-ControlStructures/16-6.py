###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n): ')
extra_spin = input('Extra spin? (y/n): ')

if program == 'j':
    if extra_rinse == 'y':
        total_washing_time = 40 + 15
        print(f'Washing time is {total_washing_time}')
    elif extra_spin == 'y':
        total_washing_time = 40 + 9
        print(f'Washing time is {total_washing_time}')
    elif extra_rinse == 'y' and extra_spin == 'y':
        total_washing_time = 40 + 15 + 9
        print(f'Washing time is {total_washing_time}')
    else:
        total_washing_time = 40
        print(f'Washing time is {total_washing_time}')
elif program == 'u':
    if extra_rinse == 'y':
        total_washing_time = 70 + 15
        print(f'Washing time is {total_washing_time}')
    elif extra_spin == 'y':
        total_washing_time = 70 + 9
        print(f'Washing time is {total_washing_time}')
    elif extra_rinse == 'y' and extra_spin == 'y':
        total_washing_time = 70 + 15 + 9
        print(f'Washing time is {total_washing_time}')
    else:
        total_washing_time = 70
        print(f'Washing time is {total_washing_time}')
elif program == 's':
    if extra_rinse == 'y':
        total_washing_time = 20 + 15
        print(f'Washing time is {total_washing_time}')
    elif extra_spin == 'y':
        total_washing_time = 20 + 9
        print(f'Washing time is {total_washing_time}')
    elif extra_rinse == 'y' and extra_spin == 'y':
        total_washing_time = 20 + 15 + 9
        print(f'Washing time is {total_washing_time}')
    else:
        total_washing_time = 20
        print(f'Washing time is {total_washing_time}')
else:
    print("Incorrect: Try again")

