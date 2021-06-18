#using for loop
friends = ["aman","kaustav","gagan","prakhar"]
for x in friends:
    print(x)

#looping through string
for y in "aman":
    print(y)

#break statement
for p in friends:
    print(p)
    if p== "gagan":
        break

#continue
titles = ["shah","bora","dha","bhatia"]
for x in titles:
    if x=="bora":
        continue
    print(x)

#range() function
for x in range(2,6):
    print(x)
#increment
for x in range(2,20,4):
    print(x)

#else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#using else in for loop with break
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#nested loop

n=["red","yellow","blue"]
m=["pink","green","orange"]

for v in n:
    for b in m:
        print(v,b)









