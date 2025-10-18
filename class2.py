class Lucky:
    def displayLucky(self):
        print("Inheritance Lucky class")

class Prasanna: 
    def displayprasanna(self):
        print("Inheritance Prasanna class")

class Lakshmi:
    def displaylakshmi(self):
        print("Inheritance Lakshmi class")

# 'ChildClass' 
class ChildClass(Lucky, Prasanna, Lakshmi): 
    pass
obj = ChildClass()


print(" Calling methods from the inherited classes ")
obj.displayLucky()
obj.displayprasanna() 
obj.displaylakshmi() 
