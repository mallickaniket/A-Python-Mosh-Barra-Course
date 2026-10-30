# Note text -
# if temperature is greater than 30 degrees, print "It's a hot day"
# otherwise, print "It's a cold day"
# otherwise, it's neither hot not cold

temperature = 31

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
    
# Exercise - 1

name = input("Enter your name: ")

if len(name) < 3:
    print("Name must be at least 3 characters")
    
elif len(name) > 50:
    print("Name can be a max of 50 characters")
    
else:
    print("Name looks good!")