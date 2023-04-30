class school: # (номер/название школы, этажность)
    name_of_school = str
    number_of_school_studehts = int
    number_of_floor = int
    number_of_grades = int
    list_of_grade = list

    def __init__(self, name_of_school: str, number_of_floor: int):
        self.name_of_school = name_of_school
        self.number_of_school_studehts = 0
        self.number_of_floor = number_of_floor
        self.number_of_grades = 0
        self.list_of_grade = []
    
    def __str__(self):
        return f'''
        name_of_school: {self.name_of_school}
        number_of_school_studehts: {self.number_of_school_studehts}
        number_of_floor: {self.number_of_floor}
        number_of_grades: {self.number_of_grades}'''


class grade: # (год обучения, места, школа, номер класса)
    number_of_grade_studehts = int
    year_of_study = int
    number_of_seat = int
    school_ = school
    number = str
    name_of_grade = str
    list_of_students = []

    def __init__(self, year_of_study: int, nunber_of_seat: int, school_: school, number: str):
        self.number_of_grade_studehts = 0
        self.year_of_study = year_of_study
        self.number_of_seat = nunber_of_seat
        self.school_ = school_
        self.number = number
        self.name_of_grade = ((str(self.year_of_study)) + number)
        self.school_.number_of_grades += 1

    
    def __str__(self):
        self.school_
        return f'''
        number_of_grade_studehts: {self.number_of_grade_studehts}
        year_of_study: {self.year_of_study}
        nunber_of_seat: {self.number_of_seat}
        school: {self.school_.name_of_school}
        name: {self.number}
        full_name: {self.name_of_grade}'''


def sistem_of_grade_puting(school1: school): #Система распределения учеников по классам
    max = 0
    for i in range(school1.list_of_grade):
        index = grade(i).number_of_seat - grade(i).number_of_grade_studehts
        if index > max:
            max = index
            max_grade = grade(school1.list_of_grade[i])
    return max_grade


class student: # (имя, возрост, пол, класс, школа)
    name = str
    age = int
    pol = str
    grade_ = grade
    school_ = school

    def __init__(self, name: str, age: int, pol: str, school_: school,):
        self.name = name
        self.age = age
        self.pol = pol
        self.grade_ = grade(sistem_of_grade_puting(school(school_)))
        self.school_ = school_
        self.school_.number_of_school_studehts += 1
        grade(self.grade_).number_of_grade_studehts += 1
    
    def __str__(self):
        return f'''
        name: {self.name}
        age: {self.age}
        pol: {self.pol}
        grade: {self.grade_.name_of_grade}
        school: {self.school_.name_of_school}'''

