s1,s2 = input("Enter string one: "), input("Enter string two:")
s1,s2 = s1[0]+s2[1]+s1[2:],s2[0]+s1[1]+s2[2:]
print("Combined: ", s1, s2)
colors=input("Enter colors separated by comma: ").split(',')
print("Alternative colrs:",colors[::2])
