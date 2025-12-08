import math
amount_string = input('Kwota:')
amount = int(amount_string)

vat = amount*0.77

print(f'The vat of {amount} is {vat:.2f}')