#creating set
#it starts with {}
my_set= {"aman","kaustav","gagan","prakhar","pankaj"}
print(my_set)


#duplicates value are ignored
my_set= {"aman","kaustav","gagan","prakhar","pankaj","aman"}
print(my_set)

#using len function again
print(len(my_set))

#uisng type() to get data type
print(type(my_set))

#access
for x in my_set:
    print(x)

#update
#The object in the update() method does not have to be a set,
#it can be any iterable object (tuples, lists, dictionaries etc.).

my_title=["shah","bora","dhadiwal","bhatia"]
my_set.update(my_title)
print(my_set)
print(type(my_set))

