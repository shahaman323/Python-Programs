#and keyword
x=634
y=543
z=231
if x>y and x>z:
    print("x is greater than y and z")

#now using or keyword
if x>y or z>y:
    print("either x or y is greater than y")

#nested if
marks=90
if marks>60:
    print("pass")
    if marks>70:
        print("average")
    else:
        print("fail")

#pass statement: it avoids error if we dont want to print anything
a=44
b=33
if a>b:
   # print() it prints blank line
   #whereas pass doesnot print anything
    pass
