###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

input_char = input('Type one letter: ')
print(f'The letter you typed is {input_char[0]}')

int_from_str = int("20303")
print('The number representing the string "20303" is', int_from_str, type(int_from_str))

binary_str = bin(304)
print('Binary string of 304 is', binary_str)

hex_str = hex(304)
print('Hexadecimal string of 304 is', hex_str)

unicode_code = ord('€')
print('Unicode code of € is', unicode_code)

abs_value = abs(-17)
print('Absolute value of -17 is', abs_value)
