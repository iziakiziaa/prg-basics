###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    absolute_number = abs(number)
    number_string = str(absolute_number)
    total_sum = 0

    for digit_char in number_string:
        # Convert each character back to an integer and add it to the running total
        digit_value = int(digit_char)
        total_sum = total_sum + digit_value
        
    return total_sum
   
any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')