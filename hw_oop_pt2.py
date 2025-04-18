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

