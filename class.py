#single inheritance
class A:
    def displayA(self):
        print("inheritance A class")
class B(A):
    def displayB(self):
        print("inheritance B class")

obj = B()
obj.displayA()
obj.displayB()

print()
#Multi Label inheritance
class Lucky:
    
    def displayLucky(self):
        print("Inheritance Lucky class")
class Prassu(A):

    def displayprassu(self):
         print("inheritance Prassu class")
class lakshmi(B):
    def displaylakshmi(self):
        print("inheritance Lakshmi class")

obj = c()
obj.displayLucky()
obj.displayPrassu()
obj.displaylakshmi()
class Lucky:
    def displayLucky(self):
        print("Inheritance Lucky class")

class Prassu: # Prassu is now a standalone base class
    def displayprassu(self):
        print("Inheritance Prassu class")

class Lakshmi: # Corrected class name capitalization (optional, but good practice)
    def displaylakshmi(self):
        print("Inheritance Lakshmi class")

# The main child class 'ChildClass' inherits from all three parents
class ChildClass(Lucky, Prassu, Lakshmi): 
    pass























