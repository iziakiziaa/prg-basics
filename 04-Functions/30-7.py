#  Define a function sum_natural(n) that for the given natural number n calculates the sum of all natural numbers between 1 and n.
#  Apply recursion. Then, create a program that calculates the sum of natural numbers in the range <1,10>.

def sum_natural(n):
    sum = 1
    for i in range(1, n+1):
        sum += i
    return sum

if __name__ == "__main__":
    print(sum_natural(10))
