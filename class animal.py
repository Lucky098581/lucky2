class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic Animal sound"


class Dog(Animal): #Dog inherits from Animal
    def __init__(self,name, breed):
        super().__init__(name)   # Call the parent class's constructor
        self.breed = breed

    def speak(self): # Oerride the speak method
        return "Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball."
    
    #create an instance of the child class(dog)
my_dog=Dog("snoopy","pomerian")

#access attributes and methods from both parent and child classes
print(f"Name: {my_dog.name}")
print(f"Breed:{my_dog.breed}")
print(my_dog.speak())
print(my_dog.fetch())
