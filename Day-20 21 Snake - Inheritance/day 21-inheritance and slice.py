class Animal: #super class
    def __init__(self):
        self.num_eyes = 2

    def speak(self):
        print("I am animal")

class Fish(Animal): #Super class goes in parentheses
    def __init__(self):
        super().__init__() #initialiaze the super class
        self.gills = 1
    
    def speak(self): #taking everything that the speak method form superclass is doing and modifying it
        super().speak() 
        print("doing this underwater")
    

    def swim(self):
        print("Swimming")
    
nemo = Fish()

nemo.swim() 
nemo.speak() #Inherits the method from the super class
print(f"I have {nemo.gills} gill(s) and {nemo.num_eyes} eyes")

