class Fruits:
    def __init__(self , name , color ):
        self.name = name
        self.color = color

    def display(self):
        print(f"The {self.name} fruit is {self.color}")


the_fruits = Fruits("apple","red")
the_fruits.display()
the_fruits3=Fruits("banana","yellow")
the_fruits3.display()
the_fruits4=Fruits("thorn melon","green")
the_fruits4.display()