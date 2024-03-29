# Objective: Read and write from a file




# Imports
import random


# Constants...if you want to change the names of the files that are being used change them here
NEW_FILE = 'people_updated.txt'
OLD_FILE = 'people.txt'


# Declare Variable types
records = list()
ages = list()
temp_list = list()

# Initialize all variables
records = []
ages = []
temp_list = []

# Populate ages list with random numbers 
for x in range(50):
    num = random.randrange()        # Choose a start and end number - randrange(#,#)
    ages.append(num)

# try to open the file to read from
try:
    # Read from a file with names in it
    file = open("""ADD THE FILE TO READ FROM""", 'r')               # FIX THIS, USE CONSTANT
    temp_list = file.readlines()
    for index in range(len(temp_list)):
        temp_list[index] = temp_list[index].rstrip('\n') 
# If we can't open the file print the error to the console
except Exception as system_message:
    print(system_message)
# Close the file if there was no errors opening it
else:
    print('Successfully read from file')
    # Append ages to the end of the names
    for index in range(len(temp_list)):
        records.append(temp_list[index] + ' ' + str(ages[index]))
    file.close()


    



# Try opening file to write to 
try:
    # write every record to new file (another way to read/write)
    with open("""ADD THE FILE TO READ FROM""", 'w') as f:           # FIX THIS, USE CONSTANT
        for record in records:
            f.write() # ------------------------------------------- # FIX, Write each record ended with a new line to the file
# If we can't open the file print the error to the console
except Exception as system_message:
        print(system_message)
# Close the file if there was no errors opening it
else:
     print('Successfully wrote to file')
     f.close()


