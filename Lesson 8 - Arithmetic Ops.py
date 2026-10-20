print(10 / 3)       # This is division operator, which will print the result of dividing 10 by 3 to the console.
print(10 + 3)       # This is addition operator, which will print the result of adding 10 and 3 to the console.
print(10 - 3)       # This is subtraction operator, which will print the result of subtracting 3 from 10 to the console.
print(10 * 3)       # This is multiplication operator, which will print the result of multiplying 10 by 3 to the console.
print(10 // 3)      # This is floor division operator, which will print the result of dividing 10 by 3 and rounding down to the nearest integer.
print(10 % 3)       # This is modulo operator, which will print the remainder of dividing 10 by 3 to the console.
print(10 ** 3)      # This is exponentiation operator, which will print the result of raising 10 to the power of 3 to the console.

x = 20
x = x + 5           # This will add 5 to the current value of x and assign the result back to x.
x += 5              # This is a shorthand for x = x + 5, which will add 5 to the current value of x and assign the result back to x.
                    # This is called an augmented assignment operator.
                    # The way it is written, the + sign and the = sign show that we are adding something to the current value of x and assigning the result back to x.
                    # The same applies to other arithmetic operators, such as -=, *=, /=, //=, %=, and **=.

# Operator Precedence
# Operator precedence determines the order in which operations are performed in an expression.
# It follows the order of operations, which is often remembered by the acronym PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction).
# Example: 
y = 10 + 3 * 5 ** 2     # This expression will be evaluated as follows:
                        # 1. Exponentiation: 5 ** 2 = 25
                        # 2. Multiplication: 3 * 25 = 75
                        # 3. Addition: 10 + 75 = 85
print(y)  # This will print 85 to the console.