# Objective: Use loops to output text





# Implementation
print('Hello World!')
print('To output text to the screen use the print() function!')
print('Make sure to put your text inbetween single or double quotes!')
print("Try for yourself!")
print('Hello World!')
name = input('What is your name? ')
print(f'Hello {name}!')
age = int(input('How old are you? '))

# Use of basic conditionals
if age < 10:
    print('Wow you\'re under 10 years old!')
elif age <= 13:
    print('Wow you\'re in between 10 and 13 years old!')
elif age <= 16:
    print('Wow you\'re in between 13 and 16 years old!')
else:
    print('Wow you\'re over 16 years old!')

# Use of loops
print('Printing every letter in your name')
for x in name:  
    pass    # Output x (delete pass with correct code)

# Printing your name multiple times
repeat = int(input('How many times would you like to print your name? '))
for x in range():   # Finish for loop
    pass            # Output name (delete pass with correct code)

food_list = []      # Creating list
flag = bool(True)   # Flag is used for controlling while loop
# '''Make this a while loop''' flag != False:     # Make sure to delete '''...'''
#     food =                                      # Ask user for a food they like
#     food_list.append(food)                      # Adding the food the user entered to list of foods they like
#     response = input('Would you like to add another food?(Y/N): ')
#     response = response[0].upper()              # 'Cleaning' the users response and only getting the first letter
#     if response == 'Y':
#         pass    # Do not change this
#     elif response == 'N':
#         pass    # Change this and set flag to flase
#     else:
#         '''Make this a while loop''' True:  # Make sure to delete '''...'''
#             response = input('Invalid choice, would you like to add another food?(Y/N): ')
#             response.upper()
#             response = response[0].upper()
#             if response == 'Y' or response == 'N':
#                 if response == 'N':
#                     pass    # Change this and set flag to flase
#                 break
        
print('Here is a list of all the foods you like')        
# Use a for loop to to output all the foods you entered