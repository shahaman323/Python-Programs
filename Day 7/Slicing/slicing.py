#using slicing
# slice(start,stop,step)
my_name = 'amanshah'
slice_object = slice(1,7,2)
print(my_name[slice_object])

#using negative index
my_object = 'helloaman'
slice_object = slice(-1,-5,-3)
print(my_object[slice_object])

#alternative obj[start:stop:step]
print(my_object[::])

#slicing in list
my_list=[1,2,3,4,5,6]
print(my_list[1:5:2])
