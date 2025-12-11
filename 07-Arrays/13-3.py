def f(number,array):
    if number in array:
        return f'number {number} appears in {array}'
    

if __name__ == "__main__":
    print(f(23,[15,38,7,23,14]))