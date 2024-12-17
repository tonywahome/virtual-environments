def hello():
    print("Hello, world!")

hello() #call to the function

#naming functions
#they need to be in lowercase and separated by underscores

# def sum(a, b): #function that takes 2 arguments
#     print(a + b)

# sum(2, 3)
# sum(7, 6)
# sum(98, 199)

# sum(2, 3, 4) #error because the function only takes 2 arguments


def sum(a=0, b=0): #default values
    if (type(a) is not int or type(b) is not int): #type checking
        return 0 #return 0 if the arguments are not integers
    return a + b 

total = sum()
print(total)

def multiple_items(*args): #arguments
    print(args)
    print(type(args))

multiple_items(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Tom", "Jerry")

def mult_named_items(**kwargs): #keyword arguments
    print(kwargs)
    print(type(kwargs)) 

mult_named_items(first="Tom", last="Jerry") #dictionary

