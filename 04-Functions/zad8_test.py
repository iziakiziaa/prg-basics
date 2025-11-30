#   Zdefiniuj funkcję f(speed1,speed2), która porównuje dwie prędkości: 
#   speed1 podaną w km/h oraz speed2 podaną w m/s. Funkcja zwraca True, jeśli prędkości są sobie równe, lub False w przeciwnym wypadku.
#   Przykładowy wynik: f(36,10) zwraca True f(20,20) zwraca False

def f(speed1,speed2):
    speed1_ms = speed1 / 3.6
    if speed1_ms == speed2:
        return True
    elif speed1_ms > speed2:
        return False
    elif speed1_ms < speed2:
        return False
    
if __name__ == "__main__":
    print(f(20,20))