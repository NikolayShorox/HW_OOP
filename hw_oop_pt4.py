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
best_student.courses_in_progress += ['Pyton']
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Pyton']
cool_reviewer.rate_hw(best_student, 'Pyton', 10)
cool_reviewer.rate_hw(best_student, 'Pyton', 10)
cool_reviewer.rate_hw(best_student, 'Pyton', 10)

best_lecturer = Lecturer('Some', 'Buddy')
best_lecturer.lecture_given += ['Pyton']
cool_student = Student('Ruoy', 'Eman', 'your_gender')
cool_student.lectur_attached += ['Pyton']
cool_student.rate_hw(best_lecturer, 'Pyton', 8)
cool_student.rate_hw(best_lecturer, 'Pyton', 5)
cool_student.rate_hw(best_lecturer, 'Git', 3)

some_reviewer = Reviewer('Some', 'Buddy')

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.lecture_given += ['Pyton']
score_student = Student('Ruoy', 'Eman', 'your_gender')
score_student.lectur_attached += ['Pyton']
score_student.rate_hw(some_lecturer, 'Pyton', 3)
score_student.rate_hw(some_lecturer, 'Pyton', 9)
score_student.rate_hw(some_lecturer, 'Pyton', 10)

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Pyton','Git']
some_student.finished_courses += ["Введение в программирование"]
score_reviewer = Reviewer('Some', 'Buddy')
score_reviewer.courses_attached += ['Pyton']
score_reviewer.rate_hw(some_student, 'Pyton', 10)
score_reviewer.rate_hw(some_student, 'Pyton', 10)
score_reviewer.rate_hw(some_student, 'Pyton', 10)

student_1 = Student('masha', 'glasha','sasha')
student_1.courses_in_progress += ['Pyton']
student_1.finished_courses += ['Rasta']
student_2 = Student('tanya', 'manya', 'kanya')
student_2.finished_courses += ['Man']
student_2.courses_in_progress += ['Git', 'Java' ]
student_3 = Student('vanya', 'lanya', 'sanya')
student_3.finished_courses += ['Peace']
student_3.courses_in_progress += ['Pyton', 'Fifa']

reviewer_1 = Reviewer('Snoop', 'Dog')
reviewer_1.courses_attached += ['Pyton','Java','Git']
reviewer_1.rate_hw(student_1, 'Pyton', 5)
reviewer_1.rate_hw(student_1, 'Pyton', 8)
reviewer_1.rate_hw(student_1, 'Pyton', 6)
reviewer_1.rate_hw(student_1, 'Pyton', 3)
reviewer_1.rate_hw(student_2,'Git', 8)
reviewer_1.rate_hw(student_2, 'Java', 2)
reviewer_1.rate_hw(student_2,'Git', 5)
reviewer_1.rate_hw(student_2, 'Java', 7)
reviewer_1.rate_hw(student_3,'Pyton', 10)
reviewer_1.rate_hw(student_3,'Pyton', 3)
reviewer_1.rate_hw(student_3,'Fifa', 10)
reviewer_1.rate_hw(student_3,'Pyton', 7)
reviewer_1.rate_hw(student_3,'Pyton', 9)
reviewer_1.rate_hw(student_3,'Fifa', 5)

students = [student_1, student_2,student_3]
courses = 'Pyton'

def average_stud(list_student, course):
    app = []    
    for score in list_student:
        if course in score.grades:
            for score_1 in score.grades.values():
                app.extend(score_1)
    return(sum(app)/len(app))

print(average_stud(students,courses))

lecturers = [best_lecturer, some_lecturer]

def average_lectur(list_lectur, course):
    app = []    
    for score in list_lectur:
        if course in score.grades:
            for score_1 in score.grades.values():
                app.extend(score_1)
    return(sum(app)/len(app))

print(average_lectur(lecturers, courses))
        
    
              
             
    


    
