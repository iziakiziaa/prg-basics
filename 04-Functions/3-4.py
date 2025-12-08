###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a,b,c):
    wynik = 0.5*(a+b+c)
    s = wynik*(wynik-a)*(wynik-b)*(wynik-c)
    result = math.sqrt(s)
    return result


pierwszy = triangle_area(3,4,5)
print(f'The area of ​​a triangle with sides 3,4,5 is {pierwszy} ')
drugi = triangle_area(5,12,13)
print(f'The area of ​​a triangle with sides 5,12,13 is {drugi}')
trzeci = triangle_area(7,24,25)
print(f'The area of ​​a triangle with sides 7,24,25 is {trzeci}')
