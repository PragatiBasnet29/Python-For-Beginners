# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
    num = 3003


obj1 = MyClass()
print(obj1.num)

print("\n")
print("\n")


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


s1 = Student("Sampath", 33)
print(s1.name)
print(s1.grade)

