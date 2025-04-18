class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.lectur_attached = []

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.lectur_attached and course in lecturer.lecture_given:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        for course, grade in self.grades.items():
            grade = sum(grade)/len(grade)
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{grade}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}')
        return result
    
    def __eq__(self, lecturer):
        return self.grades == lecturer.grades
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname
        self.courses_attached = [] 
        self.grades = {}
        self.lecture_given = []
    
    def __str__(self):
        for course, grade in self.grades.items():
            grade = sum(grade)/len(grade)
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {grade}')
        return result

class Reviewer(Mentor):

    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname
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
        result = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return result
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_lecturer = Lecturer('Some', 'Buddy')
best_lecturer.lecture_given += ['Python']
cool_student = Student('Ruoy', 'Eman', 'your_gender')
cool_student.lectur_attached += ['Python']
cool_student.rate_hw(best_lecturer, 'Python', 10)
cool_student.rate_hw(best_lecturer, 'Python', 10)
cool_student.rate_hw(best_lecturer, 'Python', 10)

some_reviewer = Reviewer('Some', 'Buddy')

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.lecture_given += ['Pyton']
score_student = Student('Ruoy', 'Eman', 'your_gender')
score_student.lectur_attached += ['Pyton']
score_student.rate_hw(some_lecturer, 'Pyton', 10)
score_student.rate_hw(some_lecturer, 'Pyton', 10)
score_student.rate_hw(some_lecturer, 'Pyton', 10)


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Pyton','Git']
some_student.finished_courses += ["Введение в программирование"]
score_reviewer = Reviewer('Some', 'Buddy')
score_reviewer.courses_attached += ['Pyton']
score_reviewer.rate_hw(some_student, 'Pyton', 10)
score_reviewer.rate_hw(some_student, 'Pyton', 10)
score_reviewer.rate_hw(some_student, 'Pyton', 10)




