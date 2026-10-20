first = "John"
last = "Smith"

# Now let's say I want to write this - John [Smith] is a coder.

message = first + ' [' + last + '] is a coder.'     # Here we are using string concatenation to combine the strings and create the desired message.
                                                    # Let's break it down:
                                                    
                                                    # first is the variable that contains the string "John".
                                                    # ' [' is a string that contains a space and an opening square bracket.
                                                    # last is the variable that contains the string "Smith".
                                                    # '] is a coder.' is a string that contains a closing square bracket, a space, and the words "is a coder.".

print(message)    # This will print the message "John [Smith] is a coder." to the console.

# But it is not ideal to use string concatenation to create messages like this, especially when we have multiple variables to include in the message. 
# It can get messy and hard to read.
# So, we can use formatted strings to make it easier to create messages like this.

msg = f'{first} [{last}] is a coder.'   # Here we are using a formatted string to create the desired message.
                                        # Let's break it down:
                                        # Here, what f-string does is it allows us to use expressions inside the string by placing them in curly braces {}.
                                        # The expressions will be replaced with their values when the string is created.
                                        # Basically, it is like writing the message as a template and then filling in the blanks with the values of the variables, 
                                        # Python will automatically replace the expressions with their values when the string is created.