# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

kategoria = [0,0,0] # food transport utilities
tydzien = []
suma_calkowita = 0

for wydatki_tyg in enumerate(monthly_expenses):
    suma_tyg = 0
    for indeks_kategorii, kwota_wydatku in enumerate(expense):

