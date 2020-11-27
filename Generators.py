# Generators are memory efficient as they dont store the entire values in the memory
# it waits until the developers next call, so this allows us to work with one value at a time
# unlike a list where the entire values are loaded into the memory and you can fetch the data through index number
# this is not memory efficient

my_nums = (x**3 for x in range(10))  # the () makes it a generator
my_nums2 = [x**3 for x in range(10)]  # the [] makes it a list

print('Type of my_numes ', type(my_nums))
print('Type of my_numes2 ', type(my_nums2))

print()

print('Printing my_numes: ', my_nums)
print('Printing my_numes: ', my_nums2)


print()

# to iterate through the generator you can use the next function but it will only iterate once
#  you need to keep calling it everytime you want to iterate
print('Last number the generator visited', next(my_nums))
print()

# Looping through the generator, the loop wont start at 0 it will start at 1
#  as we already iterated once above using the next function
# so the generator will pick from where it left
print('Generator looping')
print()

for i in my_nums:
    print(i)

print()
print('List looping')

for i in my_nums2:
    print(i)

print()
print('Fibonacci Sequence')


def gen_fibon(n):
    a = 1
    b = 1

    for i in range(n):     
    # generators can rememeber a place in a sequence without holding the entore sequenece
    # generators remembers what the previous values was and returns what the formula is following
        yield a  # yield is like a return statment except its used for generators so this yield will retuen a to the for loop down below and print it as i check thisout for more understanding: https://www.youtube.com/watch?v=1t_NUJFh33Y
        a, b = b, a+b

for i in gen_fibon(10):
    print(i)
