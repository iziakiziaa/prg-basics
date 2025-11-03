###
# Program, który sprawdza, czy liczba jest
# dodatnia, ujemna, czy równa zero.
#
number = int(input('Enter a number: '))

if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
else:
    # Jeśli liczba nie jest ani > 0, ani < 0, musi być równa 0
    print(f'Number {number} is 0')
    
