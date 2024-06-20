class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_name(self):
        print(f" My name is {self.first_name} {self.last_name} and I am  {self.age} years old.")


class Student(Person):
      def __init__(self, first_name, last_name, age,):
          # self.score = score
          super().__init__(first_name, last_name, age)
myStudent = Student("Dennis", "Tergech", 23)
myStudent.print_name()
myStudent2 = Student("Martin", "Taylor", 43,)
myStudent2.print_name()
myStudent3 = Student("Kevin", "Friend", 47,)
myStudent3.print_name()
myStudent4 = Student("Gareth", "Fala", 45,)
myStudent4.print_name()