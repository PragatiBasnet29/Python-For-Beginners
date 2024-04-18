# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class
class MyClass:
    num = 3003


# Create Object
obj1 = MyClass()
print(obj1.num)

print("\n")
print("\n")


# The __init__() Function
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


s1 = Student("Sampath", 33)
print(s1.name)
print(s1.grade)

print("\n")



# The __str__() Function
class Person:
    def __init__(self, name, age):
        self.name =name
        self.age = age

    def __str__(self):
        return f"I'm {self.name} and ({self.age}) years old." 

p1 = Person("Sampath Tharanga", 33)
print(p1)


# string Formatting
## we can also use F, '', ''''', """"""'
#f"string"

## arithmetic expression
print(f"{5 * 5}")


print("\n")


# Object Methods
class Customer:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def myfun(self):
        print("Hello " + self.name)

c1 = Customer("Sampath", "Anurashapura")
c1.myfun()

#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

print("\n")

# The self Parameter
class Teacher:
    def __init__(myobject, name, subject):
        myobject.name = name
        myobject.subject = subject

    def myfun(x):
        print("Hello, your " + x.subject + " teacher is " + x.name + ".")

t1 = Teacher("Sampath Tharanga", "Mathematics")
t1.myfun()


# The pass Statement

# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Sales:
    pass