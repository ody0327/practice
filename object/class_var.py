class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        print("{}번째 학생이 생성됨".format(Student.count))

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("강민경", 98, 92, 96, 92),
    Student("박수빈", 95, 98, 98, 98),
    Student("김태훈", 64, 88, 92, 92)
]

print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))