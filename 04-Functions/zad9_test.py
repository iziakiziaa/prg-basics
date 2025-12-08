#    Rozmiary odzieży określone są symbolami S, M oraz innymi (traktowanymi jako większe, np. L/XL). 
#    Zdefiniuj funkcję f(size1,size2), która porównuje dwa rozmiary.
#    Funkcja zwraca 1, jeśli size1 jest większy, 2 jeśli size2 jest większy, lub 0 jeśli rozmiary są takie same.
#    Przykładowy wynik: f("L","S") zwraca 1 f("M","L") zwraca 2


def f(size1,size2):
    sizeS = 'S'
    sizeM = 'M'
    sizeL = 'L'
    sizeXL = 'XL'
    sizeS < sizeM < sizeL < sizeXL
    if size1 < size2:
        return 1
    elif size1 == size2:
        return 0
    elif size1 > size2:
        return 2
    
if __name__ == "__main__":
    print(f('M','L'))