print(10 / 3)
print(10 // 3)  # Using // prints the number in an integer form instead of a float

multiline = """ 
This
is
a
multi
line
string
"""
print(multiline)

# The Back slash tells python to ignore what comes after it
print("Mohamed's \"Laptop\"")
print('C:\Desktop\number')
print(r'C:\Desktop\number')  # The r tells python to ignore the \n

# Lists in python are mutable and can accept different types
List = [12, 'Mohamed']
# Tupples are immutable which makes it memory efficent, also can store different typs
Tupple = (21, 23, 'MOHAMED')
# Values are printed in random order and igonres any dublicated values
Sets = {22, 12, 12, 'fa', 'fa'}
print(Sets)

Dictionary = {'Chicken': 3, 'Beef': 5}
print(Dictionary['Chicken'])
print(Dictionary.get('Chicken'))
print(Dictionary.get('Fish', 'Not Found!'))
# Combining 2 lists into a Dictionary
Keys = ['Mohamed','Hedeiwy','Mustafa']
Values = [20, 23, 32]
Combining = dict(zip(Keys, Values))
print(Combining)

Range = range(0,10)
print(Range)
print(list(range(0,10)))
#Or
print(list(Range))
 