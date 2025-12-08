# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.quirk = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student3.quirk = "Ice"
    student2.name = "Olivia"
    student2.age = 21
    student2.quirk = "Haluccination"
    student3.name = "Bakugo"
    student3.age = 25
    student3.quirk = "Explosions"
    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old and has {student1.quirk} quirk')
    print(f'{student2.name}, {student2.age} years old and has {student2.quirk} quirk')
    print(f'{student3.name}, {student3.age} years old and has {student3.quirk} quirk')

if __name__ == "__main__":
    main()