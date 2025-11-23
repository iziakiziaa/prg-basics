###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = float(input("type your first number: "))
number2 = float(input("type your second number: "))
operator = input("type your symbol: ")

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        print("error, nie mozesz przez 0")
        exit()
else:
    print("error unknown operator")
    exit()


# print result
print(f'{number1} {operator} {number2} = {result}')