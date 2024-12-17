value = "y"
count = 0
# while value:
#     print(value)
#     value = False # can be expressed as 0


while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0
        continue
