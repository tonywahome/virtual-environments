# dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# access items
print(band["guitar"])
print(band.get("vocals"))

#list allkeys
print(band.keys())

# list all values
print(band.values())

#list as tuples
print(band.items())

# verify a key exists
if "bass" in band:
    print("Yes")
else:
    print("No")

band["bass"] = "Jones"
band.update({"drums": "Bonham"})
print(band)

#remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

#delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

#not how to copy dicts
# band2 = band #create a reference
# print("bad copy")
# print(band2)
# print(band)


band2 = band.copy()
band2["bass"] = "Jones"
print("good copy")
print(band2)
print(band) 

#copying using the dic constructor func
band3 = dict(band)
print("good copy")
print(band3)

# nested dict
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)

print(band["member1"]["name"])

# sets
nums = {1, 2, 3, 4, 5}
nums2 = set((1, 2, 3, 4, 5))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no duplicates allowed
nums = {1, 2, 2, 4, 5, 5}
print(nums)

# True is a dupe of 1 Flase is a dupe of 0
nums = {1, 2, True, False, 0}
print(nums)

#check if value is in a set
print(1 in nums)

#but you cannot refer to an element in set with an index

# add new element to set
nums.add(6)
print(nums)

# add elemeents from one set to another
morenums = {7, 8, 9}
nums.update(morenums)
print(nums)

# you can use update with lists tuples and dicts
#merge 2 sets to create a new set
one = {1, 2, 3}
two = {4, 5, 6}
mynewset = one.union(two)
print(mynewset)

# keep only duplicates
one = {1, 2, 3}
two = {4, 5, 6}

one.intersection_update(two)
print(one) 

# keep everything but the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)