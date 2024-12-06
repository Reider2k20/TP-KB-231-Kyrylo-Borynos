
class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def __str__(self):
        return f"Student name — {self.name}, age — {self.age}"
    
students = [
    Student("Bob", 23),
    Student("Max", 25),
    Student("Jon", 18),
    Student("Emma", 20),
]

print("Sort by name")
for student in sorted(students, key = lambda student : student.name):
            print(student)

print("\nSort by age")
for student in sorted(students, key = lambda student : student.age):
            print(student)