# Define the function f(n) that returns the n-th prime number. 
# A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:

#  f(1) returns 2
#  f(5) returns 11

def f(n):
    count = 0
    num = 2
    while True:
        is_prime = True
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            count += 1
            if count == n:
                return num
        num += 1

if __name__ == "__main__":
    print(f(1))