dictionary = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
if key in dictionary:
    print(f"Key '{key}' found with value: {dictionary[key]}")
else:
    print(f"Key '{key}' not found in the dictionary.")

d1 = {'x': 10, 'y': 20}
d2 = {'y': 20, 'z': 30}
d1.update(d2)
print("Merged dictionary:", d1)

d = {'p': 5, 'q': 15, 'r': 25}
asc = dict(sorted(d.items()))
desc = dict(sorted(d.items(), reverse=True))
print("Ascending order:", asc)
print("Descending order:", desc)

inverted = {}
for k,v in d.items():
    inverted[v]=k
print("Inverted dictionary:", inverted)