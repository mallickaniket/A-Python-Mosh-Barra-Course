'''
birth_year = input('What is your birth year? ')
age = 2026 - int(birth_year)
print('You are', age, 'years old.')
'''

int()       #This is int type conversion function used to convert a string value (like "2000") into an integer value (like 2000).
float()     #This is float type conversion function used to convert a string value (like "3.14") into a float value (like 3.14).
bool()      #This is bool type conversion function used to convert a string value (like "True") into a boolean value (like True).

weight = input('What is your weight in pounds? ')
weight_pounds = float(weight)
weight_kgs = weight_pounds * 0.45
print('Your weight in kilograms is:', weight_kgs)