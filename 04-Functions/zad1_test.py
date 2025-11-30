#   Zdefiniuj funkcję f(tree_circumference), która na podstawie obwodu drzewa sprawdza, 
#   czy jego średnica wynosi co najmniej 50 cm. 
#   Funkcja zwraca True, jeśli średnica jest większa lub równa 50, lub False w przeciwnym wypadku (przyjmij pi = 3.14). 
#   Przykładowy wynik: f(200) zwraca True f(100) zwraca False

PI = 3.14

def f(tree_circumference):
    diameter = tree_circumference / PI
    return diameter >= 50

if __name__ == "__main__":
    print(f(100))