# Objective: Create and instantiate a class





# Creating a Person class 
class Person:
    # __init__ is the class initializer
    def __init__ (self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # __repr__ is used to show show a string representation of an object
    def __repr__(self):
        return f'{self.name} {self.age} {self.grade}'

    # Getter functions
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    def getGrade(self):
        return self.grade
    
    # Setter functions
    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age
    
    def setGrade(self, grade):
        self.grade = grade  


# Creating an instance of a Person object
p1 = Person('Mike', 26, 'College grad')
print('Directly accessing the class attributes')
print(p1.name)
print(p1.age)
print(p1.grade)
print('\n\nUsing getter functions to retrieve attributes')
print(p1.getName())
print(p1.getAge())
print(p1.getGrade())
print('\n\nSetting new data for the instances attributes')
p1.setName('Chris')
p1.setAge(23)
p1.setGrade('College')
print(p1.getName())
print(p1.getAge())
print(p1.getGrade())

p2 = Person('Mike', 26, 'College grad')

''' 
Look at how our person object/instance gets printed without 
the repr function correct implimented. It should look pretty 
weird bc it's showing us where the object is located in memory.
This isn't what we want when we print an instance of an object 
so now we can go ahead and correctly implement our repr function.
'''
print(p1)
print(p2)

# Another cool thing you can do is this
print(f'{p1 = }')
print(f'{p2 = }')