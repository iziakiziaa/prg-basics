# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]
suma_jedzenie = 0
suma_transport = 0
suma_media = 0

sumy_tygodniowe = []
suma_totalna = 0

for tydzien in monthly_expenses:
    suma_tygodnia = sum(tydzien)
    sumy_tygodniowe.append(suma_tygodnia)
    suma_totalna += suma_tygodnia

for i in range(4):
    suma_jedzenie += monthly_expenses[i][0]
    suma_transport += monthly_expenses[i][1]
    suma_media += monthly_expenses[i][2]

print('MONTHLY EXPENSES')
print('--------------------')
print(f'Food:     {suma_jedzenie:.2f}')
print(f'Transport:{suma_transport:.2f}')
print(f'Utilities:{suma_media:.2f}')
print('--------------------')
print(f'Week 1:   {sumy_tygodniowe[0]:.2f}')
print(f'Week 2:   {sumy_tygodniowe[1]:.2f}')
print(f'Week 3:   {sumy_tygodniowe[2]:.2f}')
print(f'Week 4:   {sumy_tygodniowe[3]:.2f}')
print('--------------------')
print(f'TOTAL:    {suma_totalna:.2f}')