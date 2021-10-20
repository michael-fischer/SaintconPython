class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname =lname

    def details(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, school):
        super().__init__(fname, lname)
        self.school = school

    def details(self):
        print(self.fname, self.lname, self.school)

class Employee(Person):
    def __init__(self, fname, lname, company):
        super().__init__(fname, lname)
        self.company = company

    def details(self):
        print(self.fname, self.lname, self.company)


person = Person("Kate", "Libby")
student = Student("Dade", "Murphy", "Stuyvesant High School")
employee = Employee("Eugene", "Belford", "Ellingson Mineral Company")

people = [person, student, employee]
for p in people:
    p.details()