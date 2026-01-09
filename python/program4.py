c1 = list(map(int, input("Enter ten numbers: ").split()))
c2 = list(map(int, input("Enter ten more numbers: ").split()))
print("Same length:",len(c1) == len(c2))
print("Same sum :",sum(c1) == sum(c2))
common_elements = set(c1)&(set(c2))
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements")