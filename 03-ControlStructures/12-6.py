#   In one of the online stores, a 25% discount is charged for each product purchased over two. 
#   Write a program that calculates the amount to be paid. 
#   Read the number of purchased products and the product price from the keyboard. Sample result:

# Number of products purchased: 5
# Product price: 40
# Amount to pay: 170.00


number_of_products = int(input("How many products have you purchased?: "))
product_price = int(input("What was the cost of one product?: "))

if number_of_products <= 2:
    amount = number_of_products * product_price
    print(f'Your total for {number_of_products} products is {amount}')
elif number_of_products > 2:
    discounted = number_of_products - 2
    amount = (2 * product_price) + (discounted * product_price) * 0.75
    print(f'Congrats! You just got a discount which lets you pay for {number_of_products} products only for {amount}!')
else:
    print("You didn't buy anything bro....")