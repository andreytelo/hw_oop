class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        summ = 0
        count = 0
        for g in self.grades.values():
            for k in g:
                summ += k
                count += 1
                average = round((summ / count), 1)
            return average

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_grade()} \n' \
              f'Курсы в процессе изучения: {self.courses_in_progress} \n' \
              f'Завершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не является студентом!')
            return
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self):
        summ = 0
        count = 0
        for g in self.grades.values():
            for k in g:
                summ += k
                count += 1
                average = round((summ / count), 1)
            return average

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {self.average_grade()} '
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является лектором!')
            return
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}'
        return res


student_one = Student('Антон', 'Антонов', 'male')
student_one.courses_in_progress += ['Python']

student_two = Student('Сергей', 'Сергеев', 'male')
student_two.courses_in_progress += ['Python']

lecturer_one = Lecturer('Иван', 'Иванов')
lecturer_one.courses_attached += ['Python']

lecturer_two = Lecturer('Александр', 'Александров')
lecturer_two.courses_attached += ['Python']

reviewer_single = Reviewer('Петр ', 'Петров')
reviewer_single.courses_attached += ['Python']

student_one.rate_lc(lecturer_one, 'Python', 9)
student_one.rate_lc(lecturer_one, 'Python', 10)
student_one.rate_lc(lecturer_two, 'Python', 8)
student_two.rate_lc(lecturer_one, 'Python', 7)
student_two.rate_lc(lecturer_two, 'Python', 8)
student_two.rate_lc(lecturer_two, 'Python', 7)

reviewer_single.rate_hw(student_one, 'Python', 9)
reviewer_single.rate_hw(student_one, 'Python', 8)
reviewer_single.rate_hw(student_one, 'Python', 5)
reviewer_single.rate_hw(student_two, 'Python', 10)
reviewer_single.rate_hw(student_two, 'Python', 9)
reviewer_single.rate_hw(student_two, 'Python', 5)

student_grades_list = [student_one, student_two]
lecturer_grades_list = [lecturer_one, lecturer_two]


def average_students_grades(grades_list, course):
    summ = 0
    count = len(grades_list)
    if course == 'Python':
        for student in grades_list:
            summ += Student.average_grade(student)
        avrg = f'Средняя оценка студентов на курсе: {round((summ / count), 2)}'
        return avrg
    else:
        print('Неправильно указан курс')


def average_lecturer_grades(grades_list, course):
    summ = 0
    count = len(grades_list)
    if course == 'Python':
        for lecturer in grades_list:
            summ += Lecturer.average_grade(lecturer)
        avrg = f'Средняя оценка лекторов за лекции: {round((summ / count), 2)}'
        return avrg
    else:
        print('Неправильно указан курс')


print(student_one)
print()
print(student_two)
print()
print(lecturer_one)
print()
print(lecturer_two)
print()
print(reviewer_single)
print()
print(student_two < student_one)
print()
print(lecturer_two < lecturer_one)
print()
print(average_students_grades(student_grades_list, 'Python'))
print()
print(average_lecturer_grades(lecturer_grades_list, 'Python'))
