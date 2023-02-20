# Objective: Create and instantiate a class





# Creating a Person class 
class Person:
    # __init__ is the class initializer
    def __init__ (self): # Fix paramater list to take age, name and grade
        pass # Correctly impliment 

    ''' ***Do this at the very end***'''
    # __repr__ is used to show show a string representation of an object
    #def __repr__(self): # Don't need to chage anything in the paramater list
    #    return '' # This will need to return a string.  

    # Getter functions
    def getName(self):
        pass # Correctly impliment
    
    def getAge():
        pass # Correctly impliment

    def getGrade():
        pass # Correctly impliment
    
    # Setter functions
    def setName():
        pass # Correctly impliment
    
    def setAge():
        pass # Correctly impliment
    
    def setGrade():
        pass # Correctly impliment


# Creating an instance of a Person object
p1 = Person()
print('Directly accessing the class attributes')
print() # Use . operator to directly access name attrubute (instance.attribute)
print() # Use . operator to directly access age attrubute
print() # Use . operator to directly access grade attrubute
print('\n\nUsing getter functions to retrieve attributes')
print() # Use class method (getter function) to get name attribute
print() # Use class method (getter function) to get age attribute
print() # Use class method (getter function) to get grade attribute
print('\n\nSetting new data for the instances attributes')
p1 # Use setter function for updating name
p1 # Use setter function for updating age
p1 # Use setter function for updating grade
print() # Output updated name
print() # Output updated age
print() # Output updated grade

p2 = Person() # Create another instance of a person object

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
#print(f'{p1 = }')
#print(f'{p2 = }')