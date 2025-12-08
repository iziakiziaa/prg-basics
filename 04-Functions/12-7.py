#  Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:

#  f(4) returns "*/*/*/*"
#  f(1) returns "*"

def f(n):
    return "/".join(["*"] * n)

if __name__ == "__main__":
    print(f(1))