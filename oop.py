#class
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        #method
    def display(self):
        print(self.first_name, self.last_name)

        #object


my_student = Student('John', 'Smith')
my_student.display()
my_student2=Student('Shiru', 'Grace')
my_student2.display()
my_student3=Student('Arthur', 'Morgan')
my_student3.display()
