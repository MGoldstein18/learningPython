class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)

    def get_average(self):
        total = 0
        for each in self.grades:
            total += each
        self.average = total/len(self.grades)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def if_passing(self):
        if self.score >= self.minimum_passing:
            self.passing = True
        else:
            self.passing = False


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

new_grade = Grade(100)
pieter.add_grade(new_grade)
