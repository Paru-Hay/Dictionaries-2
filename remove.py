d = {1: 'Python', 2: 'Dictionaries', 'age': 22}

del d["age"]  #Using del to remove an item
print(d)

val = d.pop(1) #Using pop() to remove an item and return its value
print(val)

key, val = d.popitem() #Using popitem() to remove and return the last inserted item (key, value)
print(f"Key: {key}, Value: {val}")

d.clear() #Using clear() to remove all items
print(d)
