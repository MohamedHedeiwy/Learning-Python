from array import *


# the i is to specify the type of the array wich is int
vals = array('i', [1, 2, 3, 4])

for i in range(len(vals)):
    print(vals[i])

print()

# Copying an Array
newArr = array(vals.typecode, (a*a for a in vals))   
# this is more efficent but you dont use index to grab values
for i in newArr:
    if i == 88:
        print(i)
        break
# For else
else:
    print('Not Found')
       

 

# Check this if you forgot https://www.youtube.com/watch?v=6a39OjkCN5I&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=30
