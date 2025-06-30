class Student:
    def __init__(self,name,roll):
        self.name=name;
        self.roll=roll;
    def display(self):
        print(f"name: {self.name} , roll : {self.roll}")
s1=Student("swathi",15)
print(s1.name)
s1.display()