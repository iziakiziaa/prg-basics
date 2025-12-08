#   Zdefiniuj funkcję f(a,b), która oblicza sumę liczb podzielnych przez 3 znajdujących się w przedziale domkniętym od a do b. 
#   Przykładowy wynik: f(1,6) zwraca 9 f(2,10) zwraca 18

def f(a,b):
    sum = 0
    for i in range(a,b + 1):
        if i % 3 == 0:
            sum = sum + i
    return sum
    
if __name__ == "__main__":
    print(f(2,10))