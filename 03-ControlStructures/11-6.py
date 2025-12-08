#A computer program analyses the price of a product in an online store. If the product price decreases by at least 10%, the program prints a purchase recommendation:

#Buy the product!!
#Product price reduced by 17%

product_price = int(input('Whats the price of the product?: '))
price_reduce = int(input('Whats the reduce %: '))

if price_reduce >= 10: # 10%
    print("Buy this product!")
    print(f' This product is reduced by {price_reduce}%!')
else:
    print("Dont buy this yet!")
    print(f'This product is reduced ONLY by {price_reduce}%!')