# while loop
# value = 1 
# while value <= 10:
#     print(value)
#     if value == 5:
#         continue
#     value += 1

# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
#     else:
#     print('Value is equal to ' + str(value))

# names = ['John', 'Paul', 'George', 'Ringo']
# for x in names:
    # print(x)


# for x in  "Umbrella":
    # print(x)

# for x in names:
#     if x == 'George':
#         break
#     print(x)

# for x in names:
#     if x == 'George':
#         continue
#     print(x)


# for x in range(2, 4):

# for x in range(0, 100, 5):
#     print(x)
# else:
#     print('Loop is done')

names = ['John', 'Paul', 'George', 'Ringo']
actions = ['singing', 'playing guitar', 'playing guitar', 'drumming']

# for name in names:
#     for action in actions:
#         print(name + ' is ' + action)
#         break
#     else:
#         print('No actions found')

for action in actions:
    for name in names:
        print(name + ' is ' + action)
    


    