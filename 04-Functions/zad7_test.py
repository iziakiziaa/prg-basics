#   Zdefiniuj funkcję f(number), która sprawdza, czy podana liczba należy do ciągu Fibonacciego. 
#   Funkcja zwraca True, jeśli liczba jest elementem ciągu, lub False w przeciwnym wypadku. 
#   Przykładowy wynik: f(5) zwraca True f(7) zwraca False

import math

def f(number):
    # Obsługa przypadku 0 (jest w ciągu) i liczb ujemnych (nie ma w ciągu)
    if number < 0:
        return False
    if number == 0:
        return True 

    # Ustawienie dwóch pierwszych liczb Fibonacciego
    a = 0  # Pierwsza liczba
    b = 1  # Druga liczba
    
    # Generuj następne liczby, dopóki nie przekroczymy liczby do sprawdzenia
    while b < number:
        
        # Obliczamy następną liczbę (to będzie suma dwóch poprzednich)
        c = a + b 
        
        # Przesuwamy się dalej w ciągu:
        a = b  # Stara druga liczba staje się nową pierwszą
        b = c  # Nowa suma staje się nową drugą liczbą
    
    # Po zakończeniu pętli sprawdzamy:
    # Czy ostatnia wygenerowana liczba (b) jest równa liczbie docelowej?
    if b == number:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f(5))