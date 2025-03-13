print("\n.........................Static & Local Variables.........................\n")

class Student:
    """This is documentation part"""
    #1. here we can create the static variable by declaring at this position
    college = 'CUTM' 
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
       # Student.college = 'CUTM' # 2. also we can create static variable like this
    
    def display(self):
        print("Student name :", self.name)
        print("Student roll :", self.roll)
        print("Student marks:", self.marks)
        print(Student.college)
        print()
    
    def diplay_with_local_variable(self):
        college = 'GIET'
        print(college)

# 3. here college is static variable, we have to create before creating the instance of that class
# Student.college = 'CUTM'

S1 = Student("Simba", 101, 99)
S2 = Student("Roy", 102, 98)
print("These are having(college) static variable:")
S1.display()
S2.display()

print("This(college) is local variable:")
S1.diplay_with_local_variable()
