#   Define the function f(n), which returns numbers from 1 to n as a string. Sample result:

#   f(11) returns "1234567891011"
#   f(4) returns "1234"

def f(n):
    wynik = ''
    for i in range(1, n +1):
        wynik += str(i)
    return wynik
    
if __name__ == "__main__":
    print(f(11))