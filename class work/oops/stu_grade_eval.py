class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        avg=sum(self.marks)/len(self.marks)
        return avg>=40
s1=Student("Priya",[45,56,60])
print("Passed:",s1.is_passed())
