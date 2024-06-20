class Animals:
    def speak(self):
        print("Animal is speaking")
class Dog(Animals):
    def bark(self):
        print("Dog is barking")
class Cat(Animals):
     def meow(self):
         print("Cat is meowing")
class Cow(Animals):
     def moow(self):
         print("Cow is moowing")
d=Dog()
d.bark()
c=Cat()
c.meow()
d.speak()
c=Cow()
c.moow()