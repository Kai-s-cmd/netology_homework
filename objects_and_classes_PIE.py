class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_rate(self):
        marks_list = []
        for mark in self.grades.values():
            marks_list.append(mark)
            return sum(mark) / len(marks_list[0])

    def __lt__(self, other):
        return self.average_rate() < other.average_rate()

    def __le__(self, other):
        return self.average_rate() <= other.average_rate()

    def __eq__(self, other):
        return self.average_rate() == other.average_rate()

    def __str__(self):
        return f'Имя: {self.name}' \
               f'\nФамилия: {self.surname}' \
               f'\nСредняя оценка за домашние задания: {self.average_rate()}'\
               f'\nКурсы в процессе изучения: {self.courses_in_progress}' \
               f'\nЗавершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rate(self):
        marks_list = []
        for mark in self.grades.values():
            marks_list.append(mark)
            return sum(mark) / len(marks_list[0])

    def __str__(self):
        return f'Имя: {self.name}' \
               f'\nФамилия: {self.surname}' \
               f'\nСредняя оценка за лекции: {self.average_rate()}'

    def __lt__(self, other):
        return self.average_rate() < other.average_rate()

    def __le__(self, other):
        return self.average_rate() <= other.average_rate()

    def __eq__(self, other):
        return self.average_rate() == other.average_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}' \
               f'Фамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student2 = Student('John', 'Raven', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['HTML']
best_student2.courses_in_progress += ['Python']
best_student2.finished_courses += ['HTML']

cool_reviewer = Reviewer('Kate', 'Jen')
cool_reviewer2 = Reviewer('Roy', 'Matis')
cool_reviewer.courses_attached += ['Python']
cool_reviewer2.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'Python', 8)
cool_reviewer.rate_hw(best_student2, 'Python', 9)
cool_reviewer.rate_hw(best_student2, 'Python', 7)


cool_lecturer = Lecturer('Davis', 'Scotch')
cool_lecturer1 = Lecturer('Long', 'Jonson')
cool_lecturer.courses_attached += ['Python']
cool_lecturer1.courses_attached += ['Python']


best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student2.rate_lecturer(cool_lecturer1, 'Python', 10)
best_student.rate_lecturer(cool_lecturer1, 'Python', 9)


print(best_student)
print(best_student2)
print(cool_reviewer)
print(cool_reviewer2)
print(cool_lecturer)
print(cool_lecturer1)
print(cool_lecturer < cool_lecturer1)
print(cool_lecturer <= cool_lecturer1)
print(cool_lecturer == cool_lecturer1)
print(cool_lecturer < cool_lecturer1)
print(best_student.courses_in_progress)


name_of_course = 'Python'
list_of_students = [best_student, best_student2]


def average_rate_all_students(list_of_students, name_of_course):
    average_marks_list = []
    for student in list_of_students:
        if name_of_course in student.courses_in_progress:
            average_marks_list.append(student.average_rate())
        else:
            return '"Возможно студент еще не закончил курс. ' \
                   'Или такого курса не существует"'
    return sum(average_marks_list) / \
        len(average_marks_list)


print(f"Средняя оценка для студентов "
      f"{average_rate_all_students(list_of_students, name_of_course)}"
      f" по курсу {name_of_course}")


name_of_course_for_lecturer = 'Python'
list_of_lecturers = [cool_lecturer, cool_lecturer1]


def average_rate_all_lecturer(list_of_lecturers, name_of_course_for_lecturer):
    average_marks_list = []
    for lecturer in list_of_lecturers:
        if name_of_course_for_lecturer in lecturer.courses_attached:
            average_marks_list.append(lecturer.average_rate())
        else:
            return '"Tакого курса не существует"'
    return sum(average_marks_list) / \
        len(average_marks_list)


print(f"Средняя оценка для лекторов "
      f"{average_rate_all_lecturer(list_of_lecturers, name_of_course_for_lecturer)}"
      f" по курсу {name_of_course}")