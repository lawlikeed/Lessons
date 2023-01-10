# Objective: Use loops to output text





# Implementation
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
# Printing every letter in your name
for x in name:  
    print(x)

# Printing your name multiple times
repeat = int(input('How many times would you like to print your name? '))
for x in range(repeat):
    print(name)

food_list = []
flag = bool(True)
while flag != False:
    food = input('Enter a food you like: ')
    food_list.append(food)
    response = input('Would you like to add another food?(Y/N): ')
    response = response[0].upper()
    if response == 'Y':
        pass
    elif response == 'N':
        flag = False
    else:
        while True:
            response = input('Invalid choice, would you like to add another food?(Y/N): ')
            response.upper()
            response = response[0].upper()
            if response == 'Y' or response == 'N':
                if response == 'N':
                    flag = False
                break
        
print('Here is a list of all the foods you like')        
for x in food_list:    
    print(x)