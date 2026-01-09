color_list = ["red","blue","green","white","black","yellow"]
color_list2 = ["violet","indigo","blue","green","yellow","orange","red"]
print("Colors that present in list1 and not in list2:")
for c in color_list:
    if c not in color_list2:
        print(c)
print("Colors that present in list2 and not in list1:")
for c in color_list2:
    if c not in color_list:
        print(c)   
# The above code finds and prints colors that are unique to each of the two lists.  
num = [1,2,3,4,3,6,7,7,1,9,10]
unique_num = list(set(num))
print("Unique numbers from the list:", unique_num)
# The above code removes duplicates from the list of numbers and prints the unique numbers.
