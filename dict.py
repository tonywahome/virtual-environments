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