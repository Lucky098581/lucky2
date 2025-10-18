class Shape:
    def no_of_sides(self):
        print("This shape has many sides")
class Square(Shape):
    def no_of_sides(self):
        print("A square has 4 sides")

s1 = Shape()
s2 = Square()

s1.no_of_sides()
s2.no_of_sides()
