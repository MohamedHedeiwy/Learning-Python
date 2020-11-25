# these are functions without a name
def square(a):
    return a*a

print(square(5))

#instead of defining a function for something this simple, create a Lambda as shown below
f = lambda a : a*a
print(f(5))

#you can pass many arguments but it can only be one expression
x = lambda a,b : a+b
print(x(1,2))
