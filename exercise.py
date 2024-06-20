class cars:
    def __init__(self,  model, year_of_manufacture , type , color,):

        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.type = type
        self.color = color

    def display(self):
        print(f"My dream car is {self.model} manufactured in {self.year_of_manufacture} being a {self.type} in {self.color}")

my_dream_car=cars('Dodge', '2024','Helcat', 'Purple')
my_dream_car.display()
my_dream_car2=cars('Merc', '2024','GLA', 'White')
my_dream_car2.display()
my_dream_car3=cars('Toyota','2018','Mark X', 'Wine Red')
my_dream_car3.display()