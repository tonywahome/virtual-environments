users = ["Alice", "Bob", "Charlie"]

data = ['Antony, 5, True']

empty = []

print("Antony" in users)

print(users[0])
print(users[-2])

print(users.index("Bob"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("David")
print(users)

users += ["Eve", "Frank"]
print(users)

users.extend(["Grace", "Helen"])
print(users)    

users.extend(data)
print(users)

users.insert(1, "Ivan")
print(users)

users[2:2] = ["John", "Kate"]
print(users)

users[1:3] = ['Roberrt', 'Alan']
print(users)

users.remove("David")
print(users)    

print(users.pop())
print(users)

del users[0]
print(users)

data.clear()
print(data)

users[1:2] = ['asil']
users.sort()
print(users)   

users.sort(key=str.lower)
print(users)

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)