# znizki lol

kwota_string = input('Type your price:')
kwota = float(kwota_string)

znizka_string = input('Type your discount:')
znizka = float(znizka_string)

price_w_discount = kwota - kwota*(znizka/100)
reduction = kwota - price_w_discount

print(f'Przy kwocie {kwota} i znizka {znizka}')
print(f'Aktualna cena wynosi {price_w_discount:.2f} a roznica to {reduction:.2f}')