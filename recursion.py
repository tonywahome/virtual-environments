def add_one(num):
    if (num >= 9):
        return num + 1
    
    total = num + 1
    print(total)

    return add_one(total)

mynewtotal = add_one(0)
print(mynewtotal)


# when you spot that the function is calling itself, you know you have a recursive function
# the function will keep calling itself until the base case is met
# the base case is the condition that stops the function from calling itself

