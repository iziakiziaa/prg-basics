def f(player1,player2):
    values = {
        'A': 10, 'K':10, 'Q':10, 'J':10, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, '1':1
    }
    sum1 = sum(values[c] for c in player1)
    sum2 = sum(values[c] for c in player2)

    if sum1 >= sum2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(f("9532", "K8"))