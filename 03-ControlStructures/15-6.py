# EAN-13 (European Article Number) is a barcode for marking goods. 
# The first 3 digits (590) usually indicate goods manufactured in Poland.
# Write a program that checks whether the EAN-13 number entered from the keyboard consists of exactly 13 characters (digits). 
# Print a message if the number is correct.
# Additionally, only when the article number is correct, print a message when the product was manufactured in Poland. Sample result:

#   Enter EAN-13 article number: 5901230094938
#   Article number is correct
#   Article manufactured in Poland

ean_number = input("Enter your 13 digit EAN number: ")

if len(ean_number) == 13:
    if ean_number.isdigit():
     print(f' Number {ean_number} is correct!')
     print(f' Number {ean_number} was manufactured in Poland!')
    else:
       print("number is not an EAN-13")
else:
    print('Wrong number')