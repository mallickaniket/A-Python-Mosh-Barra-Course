is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")

elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")

else:
    print("It's a lovely day")


print("Enjoy your day")

#Here, if the variable is_hot is True, the code inside the indented if block will run, printing "It's a hot day" and "Drink plenty of water". 
#Regardless of whether the condition is True or False, the last print statement "Enjoy your day" will always execute.
# The elif statement allows you to check multiple conditions. If the first condition is False, it checks the next one. 
# If both conditions are False, the else block will execute.

house_price = 1000000
has_good_credit = False

if has_good_credit:
    dp = house_price * 0.1

else:
    dp = house_price * 0.2
    
print(f"Down Payment: ${dp}")