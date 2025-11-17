###
# Calculates the sum of the digits in a number
#
def sum_digits(number):     # moze byc dodatki ujemny lub 0 na luzie
    absolute_number = abs(number)

    num_str = str(absolute_number)

    digit_sum = 0 

    for char_digit in num_str:
        # Convert each character back to an integer
        digit_value = int(char_digit)
        
        # v. Sum Digits: Add each integer value to a running total
        digit_sum += digit_value
        
    # vi. Output the Result: Return the sum of the digits
    return digit_sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')