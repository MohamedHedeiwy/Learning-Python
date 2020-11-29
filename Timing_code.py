import timeit
import time

# i want to see which is more efficient func1 or func2
def fun1(n):
    return [str(num) for num in range(n)]

def fun2(n):
    return list(map(str, range(n)))

# One way to time is to messure the time before and after the function call
# Before
start_time = time.time()
fun1(100)
# After
end_time = time.time()
result = print('func1 took: ', end_time - start_time)

print()
# This is the second function call with its own timing
start_time = time.time()
fun2(100)
end_time = time.time()
result = print('func2 took: ', end_time - start_time)

# However sometimes messureing the before and after is not sufficient
# as the code may run in less than a second maybe nano second
# so we will use timit module which is specifically designed to time code
# timeit runs the code over and over again
# you pass the functions as strings not the raw function themselves

print()

# this is what you will be calling over and over again
stmt = """
fun1(100)
"""
# this is what function will it test
setup = """
def fun1(n):
    return [str(num) for num in range(n)]
"""
print('func1 using timeit: ',timeit.timeit(stmt,setup,number=1000000)) # the number refers to how many time do i want to run this 

print()

stmt1 = """
fun2(100)
"""
# this is what function will it test
setup1 = """
def fun2(n):
    return list(map(str, range(n)))
"""
print('func2 using timeit: ',timeit.timeit(stmt1,setup1,number=1000000))


