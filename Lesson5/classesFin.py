# Objective: Create and instantiate a class





# Creating a Person class 
class Person:
    # __init__ is the class initializer
    def __init__ (self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

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