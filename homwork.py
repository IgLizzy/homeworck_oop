class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avereg_grades = []

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lec_grades:
                lecturer.lec_grades[course] += [grade]
            else:
                lecturer.lec_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avereg_grades(self, student):
        abc = []
        for k in self.grades.values():
            abc.extend(k)
            self.avereg_grades = sum(abc) / len(abc)
        return
        
    def __str__(self):
        abc = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.avereg_grades}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: Введение в программирование'
        return abc
            
    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибк сравнения'
        return self.avereg_grades > other.avereg_grades
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.lec_grades = {}
        self.avereg_grades = []
        
class Lecturer(Mentor):
    def _avereg_grades(self, student):
        for k, v in self.lec_grades.items():
            self.avereg_grades = sum(v) / len(v)
        return
    
    def __str__(self):
        abc = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avereg_grades}'
        return abc

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибк сравнения'
        return self.avereg_grades > other.avereg_grades
        
class Reviewer(Mentor):
    def __str__(self):
        abc = f'Имя: {self.name}\nФамилия: {self.surname}'
        return abc
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

stud1 = Student('Ron', 'Weasley', 'M')
stud1.courses_in_progress += ['Python', 'Java']
stud2 = Student('Harry', ' Potter', 'M')
stud2.courses_in_progress += ['Python', 'Java']

revie1 = Reviewer('Severus', 'Snape')
revie1.courses_attached += ['Python', 'Java']
revie2 = Reviewer('Tom', 'Riddle')
revie2.courses_attached += ['Python', 'Java']

lect1 = Lecturer('Minerva', 'McGonagall')
lect1.courses_attached += ['Python']
lect2 = Lecturer('Hagrid', 'Rubeus')
lect2.courses_attached += ['Java']

revie1.rate_hw(stud1, 'Python', 5)
revie1.rate_hw(stud1, 'Java', 5)
revie1.rate_hw(stud2, 'Python', 1)
revie1.rate_hw(stud2, 'Java', 1)

revie2.rate_hw(stud1, 'Python', 9)
revie2.rate_hw(stud1, 'Java', 1)
revie2.rate_hw(stud2, 'Python', 8)
revie2.rate_hw(stud2, 'Java', 5)

stud1.rate_lec(lect1, 'Python', 7)
stud1.rate_lec(lect2, 'Java', 10)

stud2.rate_lec(lect1, 'Python', 9)
stud2.rate_lec(lect2, 'Java', 10)

lect1._avereg_grades(lect1)
lect2._avereg_grades(lect2)
stud1._avereg_grades(stud1)
stud2._avereg_grades(stud2)


print(stud1 > stud2)