#   Zdefiniuj funkcję f(x,y), która dla podanych współrzędnych punktu zwraca numer ćwiartki układu współrzędnych (1, 2, 3 lub 4), 
#   w której ten punkt się znajduje. 
#   Przykładowy wynik: f(5,2) zwraca 1 f(-5,-2) zwraca 3

def f(x,y):
    if x > 0 and y > 0:
        return f'P({x,y}) is in 1 quarter'
    elif x > 0 and y < 0:
        return f'P({x,y}) is in 2 quarter'
    elif x < 0 and y > 0:
        return f'P({x,y}) is in 3 quarter'
    elif x < 0 and y < 0:
        return f'P({x,y}) is in 4 quarter'
    else:
        return f'Something is wrong, try again.'
    
if __name__ == "__main__":
    print(f(5,2))
