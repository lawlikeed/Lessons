# Objective: Use conditionals to output text





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