###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a_string = input('a=')
b_string = input('b=')
c_string = input('c=')

a = int(a_string)
b = int(b_string)
c = int(c_string)

volume = a*b*c
surface_area = 2*(a*b + b*c + c*a)

print(f'Volume of the cuboid is {volume}')
print(f'Surface area of the cuboid is {surface_area}')
