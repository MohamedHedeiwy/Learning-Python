a = 100

def no_gloabal():
    a =120
    print('inside no gloabal',a)

def test():
    # this allows you to access the global variable
    global a
    a = 13
    print('inside test',a)


test()
print('outside function',a)
no_gloabal()



def somethiong():
    a = 12
    # if you have the same name for a local and gloabal variable you can use gloabals to only change the gloable value wothout affecting the local
    globals()['a'] = 14
    print(a)
    #this refers to the global variable a outside the function
    print(globals()['a'])

print(somethiong())
