nums = [1,2,3,4,5,6]

# filter, all it does is that it filters based on your condition in this case its your lambda
evens = list(filter(lambda n : n%2 == 0, nums))
print (evens)

#m map, used to change/manipulate every single value 
doubles = list(map(lambda n : n*2,evens))
print(doubles)

# import reduce to work with it
from functools import reduce
# reduce, instead of having one value you want 1 value for example adding all the elemnts together
add = reduce(lambda a,b : a+b,doubles)
print(add)