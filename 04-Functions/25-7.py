#  Define the function f(x,y), which returns the sum of numbers in the range <x,y> 
#  that are completely divisible by 2 and 3 and not divisible by 4. Sample result:

# f(1,20) returns 24
# f(10,30) returns 48

def f(x,y):
    total_sum = 0
    for i in range(x, y +1):
        divisible_6 = i % 6 == 0
        not_divisible_4 = i % 4 != 0
        if divisible_6 and not_divisible_4:
            total_sum += i
    return total_sum

if __name__ == "__main__":
    print(f(10,30))