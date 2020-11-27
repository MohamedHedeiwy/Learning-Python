class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # repr is menat to be an unambiguos representation of the object and should be used for debugging, logging and things like that. it is actually meant to be used by the developer
    def __repr__(self):
        return "Customer('{}','{}','{}')".format(self.name, self.age, self.gender)
    # this is a more readable representation of an object, its meant to be used as a display for the end user
    def __str__(self):
        return f'Customer name is: {self.name}, age is: {self.age}, gender is: {self.gender}'
    def __add__(self, other):
        
        return self.age + other.age
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception('Invalid argument, must be int')
        return self.name * x

    
        
a = Person('Mohamed', 20, 'Male')
b = Person('Hedeiwy', 25, 'Male')
print(a.__repr__()) # to print the repr string
print(a)# this will automatically print the str method

print('Adding age together: ', a + b)
print(a.name * 2)

# Check this out for more dunder methods: https://dbader.org/blog/python-dunder-methods