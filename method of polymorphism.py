class Dog:
     def sound(self):
         print("Bow!")
class Cat:
    def sound(self):
        print("Meow!")
#Make a list of different animal objects
animals = [Dog(),Cat()]
#Loop through the list
#Call the 'sound' method on each animal
for animal in animals:
  animal.sound()
    
