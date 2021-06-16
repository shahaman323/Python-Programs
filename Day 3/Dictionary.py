#Dictionary store values in key:value pairs
my_dict={
    "book":"Python",
    "Author":"abc",
    "year":2021
    }
print(my_dict)

#duplicate values overwrite themselves

my_dict={
    "book":"Python",
    "Author":"abc",
    "year":2021,
    "year":2010
    }
print(my_dict)

#dict len()
print(len(my_dict))

#access
x=my_dict["year"]
print(x)

#to get keys
y=my_dict.keys()
print(y)

#how to add
my_dict["price"]=250
print(y)

#items access
z=my_dict.items()
print(z)

#loop
for p in my_dict:
    print(my_dict[p])

#for both key and values
for r,s in my_dict.items():
    print(r,s)





