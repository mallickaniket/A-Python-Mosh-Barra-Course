course = "Python's Course for \"Beginners\""    # Here escape character is used to include double quotes inside the string. 
                                                # Also, to include single quotes inside the string, we can use double quotes to define the string.
                                                # We can also use triple quotes to define a string that spans multiple lines.
print(course)

text = '''

Hello John

Here is our first email to you.

Glad to have you on board.

'''
print(text)

test = "We are testing this"

print(test[0])    # This will print the first character of the string, which is 'W'. 
                    # The square brackets are used to access individual characters in the string. 
                    # The index starts at 0, so the first character is at index 0, the second character is at index 1, and so on.
print(test[-1])   # This will print the last character of the string, which is 's'. 
                    # The negative index starts at -1, so the last character is at index -1, the second last character is at index -2, and so on.
                    # The negative index ignore the escape character and count from the end of the string. 
                    # So, the character at index -1 is the last character of the string, which is 's'.
print(test[0:6])  # This will print the first 6 characters of the string, which is 'Python'. 
                    # The colon (:) is used to specify a range of characters to extract from the string.
                    
another = test[:]   # This will create a copy of the entire string.
print(another)

name = "Jennifer"
print(name[1:-1])   # This will print the string without the first and last character.
                    # But, here -1 is used to ignore the last character and print the string without the first and last character.
                    # This is string slicing, which is used to extract a portion of the string.
                    # In this, start index is inclusive and end index is exclusive. So, the character at index 1 is included and the character at index -1 is excluded.