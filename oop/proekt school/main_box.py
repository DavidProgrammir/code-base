import random
import json
import pathlib
import os


list_of_school = []

# примитивы

late_school_id = 0
late_grade_id = 0
late_student_id = 0


def identification_school(id_: int = late_school_id):
    global late_school_id
    id_ = late_school_id + 1
    late_school_id = late_school_id + 1
    return id_

def identification_grade():
    global late_grade_id
    id_ = late_grade_id + 1
    late_grade_id = late_grade_id + 1
    return id_

def identification_student():
    global late_student_id
    id_ = late_student_id + 1
    late_student_id = late_student_id + 1
    return id_

class school: # (номер/название школы, этажность)
    name_of_school: str
    number_of_school_studehts: int
    number_of_floor: int
    number_of_grades: int
    list_of_grade: list
    id = int

    def __init__(self, name_of_school: str, number_of_floor: int):
        self.name_of_school = name_of_school
        self.number_of_school_studehts = 0
        self.number_of_floor = number_of_floor
        self.number_of_grades = 0
        self.list_of_grade = []
        list_of_school.append(self)
        self._id = identification_school()
        j_box_sch = open('/home/nubuk/Programming/oop/proekt school/grades list.json', 'r')
        j_box_sch.readlines()
        json_grades = json.load(j_box_sch)
    
    def __str__(self):
        return f'''
        name_of_school: {self.name_of_school}
        number_of_school_studehts: {self.number_of_school_studehts}
        number_of_floor: {self.number_of_floor}
        number_of_grades: {self.number_of_grades}
        id: {self.id}'''


class grade: # (школа, год обучения, места, номер класса)
    number_of_grade_studehts: int
    year_of_study: int
    number_of_seat: int
    school_number: str
    abrevature: str
    name_of_grade: str
    list_of_students = []
    id: int



    def __init__(self, school_: school, year_of_study: int = None, nunber_of_seat: int = None, abrevature: str = 'q'):
        self.number_of_grade_studehts = 0
        self.year_of_study = year_of_study
        self.number_of_seat = nunber_of_seat
        self.school_ = school_
        self.abrevature = abrevature
        self.name_of_grade = ((str(str(self.year_of_study)) + abrevature))
        self.school_.number_of_grades += 1
        self.school_.list_of_grade.append(self)
        self.id = identification_grade()



    
    def __str__(self):
        return f'''
        number_of_grade_studehts: {self.number_of_grade_studehts}
        year_of_study: {self.year_of_study}
        nunber_of_seat: {self.number_of_seat}
        school: {self.school_.name_of_school}
        name: {self.abrevature}
        full_name: {self.name_of_grade}
        id: {self.id}'''


def sistem_of_grade_puting(school1: school): #Система распределения учеников по классам
    max = 0
    for i in range(len(school1.list_of_grade)):
        index = school1.list_of_grade[i - 1].number_of_seat - school1.list_of_grade[i - 1].number_of_grade_studehts
        if index > max:
            max = index
            max_grade = school1.list_of_grade[i - 1]
    return max_grade


class student: # (имя, возрост, пол, класс, школа)
    name: str
    age: int
    pol: str
    grade_: grade
    school_: school
    id: int

    def __init__(self, name: str, age: int, pol: str, school_: school):
        self.name = name
        self.age = age
        self.pol = pol
        self.grade_ = sistem_of_grade_puting(school_)
        self.school_ = school_
        self.school_.number_of_school_studehts += 1
        (self.grade_): grade.list_of_students.append(self)
        self.id = identification_student()
    
    def __str__(self):
        return f'''
        name: {self.name}
        age: {self.age}
        pol: {self.pol}
        grade: {self.grade_.name_of_grade}
        school: {self.school_.name_of_school}
        id: {self.id}'''





random.randint(1,100)

def info(objects):
    return str(objects)


    


school_19 = school('19', 3,)
school_10 = school('10', 4)

#print(school_19.number_of_grades)


klass19_1 = grade(school_19, 4, 27, 'А')
klass10_1 = grade(school_10, 7, 33, 'В')
klass19_2 = grade(school_19, 5, 35, 'Б')



David = student('Давид', 13, 'man', school_19)
Gleb = student('Глеб', 15, 'man', school_10)


