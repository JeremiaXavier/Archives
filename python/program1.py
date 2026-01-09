strg = input("Enter the string: ")
first_char = strg[0]
modified = first_char+strg[1:].replace(first_char, '$')
print("Modified string:", modified)

if(len(strg) > 0):
    print("Exchanged text:", strg[-1] + strg[1:-1] + strg[0])
else:
    print("Exchanged text:", strg)
