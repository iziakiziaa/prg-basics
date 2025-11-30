#   Zdefiniuj funkcję f(student1, student2), która przyjmuje ciągi ocen dwóch studentów (jako stringi). 
#   Funkcja oblicza średnią ocen (uwzględniając cyfry 2, 3, 4, 5) i porównuje studentów. 
#   Funkcja zwraca 1, jeśli średnia studenta1 jest wyższa, 2 jeśli średnia studenta2 jest wyższa, lub 0 w przypadku remisu. 
#   Przykładowy wynik: f("3,4,5","4,3") zwraca 0 f("3,4,5","5,5,4,5") zwraca 2

def calculate_average(grades_string):
    # Dzieli ciąg ocen (np. "3,4,5") na listę i zamienia na liczby
    grades_list = grades_string.split(',')
    
    if not grades_list or grades_list == ['']:
        return 0.0
        
    # Oblicza sumę i średnią
    sum_of_grades = sum(int(grade) for grade in grades_list)
    return sum_of_grades / len(grades_list)


def f(student1, student2):
    avg1 = calculate_average(student1)
    avg2 = calculate_average(student2)

    if avg1 > avg2:
        return 1
    elif avg1 < avg2:
        return 2
    elif avg1 == avg2:
        return 0
    

if __name__ == "__main__":
    print(f('3,4,5', '5,5,4,5'))