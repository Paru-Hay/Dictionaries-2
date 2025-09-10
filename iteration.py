d = {1: 'Python', 2: 'Dictionaries'}

for key in d:
    print(key) #iterate over keys

for value in d.values():
    print(value) #iterate over values

for key, value in d.items():
    print(f"{key}: {value}") #iterate over key-value pairs