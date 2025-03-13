print("\n.........................Creating Class.........................\n")
class Student:
    """This is the documentation part"""
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
    # self is not keyword or reserved wordd in python. we can give any name.
    def __str__(myself):
        return 'This is Student class.'
        
    def display(myself):
        print("Student name :", myself.name)
        print("Student roll :", myself.roll)
        print("Student marks:", myself.marks)
        print()

S = [Student('Simba', 101, 99), Student('Roy', 102, 98)]
S1 = Student('Prabhas', 103, 99.9)
print("This is the documentation of the Student class:", S1.__doc__) # or we can use print("This is the documentation of the class:", S1)
for i in S:
    i.display()