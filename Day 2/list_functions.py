price=[4,32,11,66,87]
fruits=["apple","mango","banana","pine","guave","banana"]

#using extend function
fruits.extend(price)
print(fruits)

#using append to add at last
fruits.append("grapes")
print(fruits)

#using insert to add at indexed value
fruits.insert(1,"pome")
print(fruits)

#using remove
fruits.remove("apple")
print(fruits)

#uisng pop to pop out from top of stack
fruits.pop()
print(fruits)

#checking if particular item is present in list or not
print(fruits.index("banana"))

# count particular item present in list
print(fruits.count("banana"))

#using sort
price.sort()
print(price)

#reverse
price.reverse()
print(price)

#copy one list to another

fruits2= fruits.copy()
print(fruits)
