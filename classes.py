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


# Medical Information classes
class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker

    def estimated_insurance_cost(self):
        self.estimated_insurance_costs = 250 * self.age - 128 * self.sex + 370 * \
            self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
        print("{name}'s estimated insurance costs is {cost} dollars.".format(
            name=self.name, cost=self.estimated_insurance_costs))

    def update_age(self, new_age):
        self.age = new_age
        print("{name} is now {age} years old.".format(
            name=self.name, age=self.age))
        self.estimated_insurance_cost()

    def update_num_children(self, new_num_children):
        self.num_of_children = new_num_children
        if self.num_of_children == 1:
            print("{name} has {num} child.".format(
                name=self.name, num=self.num_of_children))
        else:
            print("{name} has {num} children.".format(
                name=self.name, num=self.num_of_children))

        self.estimated_insurance_cost()

    def patient_profile(self):
        patient_information = {}
        patient_information.update({
            "Name": self.name,
            "Age": self.age,
            "Sex": self.sex,
            "BMI": self.bmi,
            "Number of Children": self.num_of_children,
            "Smoker": self.smoker
        })
        return patient_information


patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name + ", " + str(patient1.age) + ", " + str(patient1.sex) + ", " +
      str(patient1.bmi) + ", " + str(patient1.num_of_children) + ", " + str(patient1.smoker))

patient1.update_age(55)
patient1.update_num_children(1)
print(patient1.patient_profile())
