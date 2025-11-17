
import math
def triangle_area(a, b, c):

    # wzor
    s = (a + b + c) / 2
    
    if s <= a or s <= b or s <= c:
        return "Invalid triangle: The side lengths do not satisfy the triangle inequality."

    # Heron obliczanie
    wynik = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return wynik

# 3, 4, 5 (wynik: 6)
wynik1 = triangle_area(3, 4, 5)
print(f'The area of a triangle with sides 3, 4, 5 is {wynik1}')

# 5, 12, 13 (wynik: 30)
wynik2 = triangle_area(5, 12, 13)
print(f'The area of a triangle with sides 5, 12, 13 is {wynik2}')

# 7, 24, 25 (wynik: 84)
wynik3 = triangle_area(7, 24, 25)
print(f'The area of a triangle with sides 7, 24, 25 is {wynik3}')
