class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        """ Метод подсчета средней оценки за домашнюю работу за все курсы """

        avg_sum = []
        for keys, values in self.grades.items():
            avg_sum.append(sum(values) / len(values))
        return round(sum(avg_sum), 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self.avg_grade() < other.avg_grade()

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        avg_sum = []
        for keys, values in self.grades.items():
            avg_sum.append(sum(values) / len(values))
        return round(sum(avg_sum), 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self.avg_grade() < other.avg_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def average_score_students(student_list, course):
    score_list = []
    for student in student_list:
        if course in student.courses_in_progress:
            for keys, values in student.grades.items():
                if keys == course:
                    res = round(sum(values) / len(values), 1)
                    score_list.append(res)
    return sum(score_list)


def average_score_lecturers(lecturers_list, course):
    score_list = []
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            for keys, values in lecturer.grades.items():
                if keys == course:
                    res = round(sum(values) / len(values), 1)
                    score_list.append(res)
    return sum(score_list)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Введение в программирование']

another_student = Student('James', 'Linderman', 'your_gender')
another_student.courses_in_progress += ['Python']
another_student.courses_in_progress += ['C++']
another_student.finished_courses += ['Git']
another_student.finished_courses += ['Java']

new_lecturer = Lecturer('Mikhail', 'Ivanov')
new_lecturer.courses_attached += ['Python']
new_lecturer.courses_attached += ['C++']

second_lecturer = Lecturer('Artem', 'Petrov')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['C++']

cool_reviewer = Reviewer('Alexander', 'Red')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C++']

new_reviewer = Reviewer('Denis', 'Smirnov')
new_reviewer.courses_attached += ['Python']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'C++', 5)
cool_reviewer.rate_hw(best_student, 'C++', 3)

cool_reviewer.rate_hw(another_student, 'Python', 3)
cool_reviewer.rate_hw(another_student, 'Python', 4)
cool_reviewer.rate_hw(another_student, 'Python', 4)

cool_mentor = Mentor('Some', 'Buddy')
new_mentor = Mentor('Big', 'Boss')

best_student.rate_lecturer(new_lecturer, 'Python', 10)
best_student.rate_lecturer(new_lecturer, 'Python', 9)
best_student.rate_lecturer(new_lecturer, 'Python', 8)
best_student.rate_lecturer(new_lecturer, 'C++', 10)

another_student.rate_lecturer(second_lecturer, 'Python', 5)
another_student.rate_lecturer(second_lecturer, 'Python', 6)
another_student.rate_lecturer(second_lecturer, 'Python', 4)
another_student.rate_lecturer(second_lecturer, 'C++', 1)

students_list = [best_student, another_student]
lecturers_list = [new_lecturer, second_lecturer]


#Пустые print'ы для более выразительного вывода
print(cool_reviewer)
print()
print(new_reviewer)
print()
print(new_lecturer)
print()
print(second_lecturer)
print()
print(best_student)
print()
print(another_student)
print()
print(new_lecturer < second_lecturer)
print(best_student > another_student)
print()
print(average_score_students(students_list, 'Python'))
print(average_score_students(students_list, 'C++'))
print()
print(average_score_lecturers(lecturers_list, 'Python'))
print(average_score_lecturers(lecturers_list, 'C++'))
