#  Zdefiniuj funkcję f(n), która zwraca łańcuch znaków składający się z kolejnych liczb całkowitych od 1 do n. 
#  Przykładowy wynik: f(4) zwraca "1234" f(0) zwraca ""

def f(n):
    wynik = ""
    # Pętla od 1 do n (włącznie)
    for i in range(1, n + 1):
        # Konwersja liczby na ciąg znaków i dodanie do wyniku
        wynik = wynik + str(i)
        
    return wynik

if __name__ == "__main__":
    print(f(0))