#  Kod produktu składa się z cyfr, gdzie czwarta cyfra jest cyfrą kontrolną. 
#  Zdefiniuj funkcję f(product_code), która sprawdza poprawność kodu. 
#  Funkcja zwraca True, jeśli czwarta cyfra jest równa reszcie z dzielenia sumy pozostałych cyfr przez 7, lub False w przeciwnym wypadku.
#  Przykładowy wynik: f("1082") zwraca True f("2035") zwraca True


def f(product_code):
    cyfra1 = int(product_code[0])
    cyfra2 = int(product_code[1])
    cyfra3 = int(product_code[2])
    cyfra4 = int(product_code[3])
    suma_roznicy = cyfra1 + cyfra2 + cyfra3
    podzielnosc = suma_roznicy % 7

    if cyfra4 == podzielnosc:
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    print(f('2035'))