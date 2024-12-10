import math

# string type

#literal assignment
first_name = "John"
last_name = "Doe"

print(type(first_name))
print(type(first_name)== str)
print(isinstance(first_name, str))

# constructor function
pizza  = str("Peperoni")
print(type(pizza))
print(type(pizza)== str)
print(isinstance(pizza, str))


#concat
full_name = first_name + " " + last_name
print(full_name)
full_name += "!"
print(full_name)

#casting
decade = str(1980)
print(type(decade))
print(decade)

statement = "I was born in " + decade + "s."
print(statement)

# multiple lines
multi_line = """
Hey there!

How are you doing?

I am doing great!

                and you?
"""
print(multi_line)

# escape characters
sentence = 'I\'m a programmer!\tI write code.\nI am a coder.'
print(sentence)


# string methods
print(first_name)
print(first_name.lower())
print(first_name.upper())
print(first_name)

print(multi_line.title())
print(multi_line.replace('doing', 'feeling'))
print(multi_line)

print(len(multi_line))
multi_line += '                                '
multi_line = "   " + multi_line
print(len(multi_line))
print(len(multi_line.strip()))
print(len(multi_line.lstrip()))
print(len(multi_line.rstrip()))


# Build a menu
title = "menu.upper()"
print(title.center(50, '='))
print('1. Pizza'.ljust(20, '.') + 'Ksh. 500'.rjust(30))
print('2. Burger'.ljust(20, '.') + 'Ksh. 300'.rjust(30))
print('3. Fries'.ljust(20, '.') + 'Ksh. 150'.rjust(30))
print('4. Soda'.ljust(20, '.') + 'Ksh. 100'.rjust(30))

print('') 

print(math.pi)
print(math.sqrt(64))
print(math.ceil(3.4))
print(math.floor(3.4))

#cast a string to a number
zip_code = "00100"
zip_value = int(zip_code)
print(type(zip_value))


