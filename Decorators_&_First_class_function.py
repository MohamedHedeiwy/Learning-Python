# # First class functions
# # First class functions can be passed as arguments, returned from a function, and assigned to a variable
# # CHECK THIS OUT IF YOU FORGOT fIRST CLASS FUNCTIONS: https://www.youtube.com/watch?v=kr0mpwqttM0
# def t(a):

#     def d():
#         print('testing: ', a)
#     return d # if we add the () the function will be executed

# # assigning a function to a variable
# a = t(1) # now the a is equal to the function d
# print(a()) # now we can execute function d as since a = d, so a() means d()

# print()

# def tz(a):

#     def d():
#         print('testing: ', a)

#     def c():
#         print('second: ', a + 1)
#     return d,c # returning back multiple functions

# a = tz(1)

# # have to pass it through a loop as its retuened back as a tuple
# x = 0
# for i in a:
#     print(a[x]())
#     x += 1


# def f1(a):
#     def f3():
#         print('starting....')
#         a()
#         print('Ending....')
#     return f3

# @f1
# def f():
#     print('sup')

# f()

print('LOOK                    G')

def f11(a):
    def f3(*x,**c):
        print('starting....')
        a(*x,**c)
        print('Ending....')
    return f3

@f11
def f2(**a):
    print('sup: ',a)

@f11
def f3(x):
    print('second: ', x)

f2(age = 1, name = 2)
f3(1)

