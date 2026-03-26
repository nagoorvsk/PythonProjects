count = {"a":1, "b":2}                  # dict("a"=1,"b"=2)

# Adding a new key-value pair
count["c"] = 3

# loop through keys
for key in count:
    print(key)

# loop through values
for value in count.values():
    print(value)

# loop through key-value pairs
for key,value in count.items():
    print(key,value)

print(count)

# Find frequency of characters in a given string...
input = "nagoorshaik"
frequency = {}

for char in input:
    frequency[char] = frequency.get(char,0) + 1

print(frequency)