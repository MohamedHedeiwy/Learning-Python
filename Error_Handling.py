def add(a, b):
    try:
        print(a+b)
    except:
        print('you got an error')
    else:
        print('you got no error')


def add1(a, b):
    try:
        x = a+b
    except:
        print('you got an error')
    else:
        print('you got no error')
        return print(x)


print('add')
add(12, 2)

print()

print('add1')
add1(12, 2)


def in1():
    while True:
        # you want to be specific on what you are trying to catch dont simply put all your code here
        # you may catch an excepetion but not one that was expected 
        # so its better to only use it if you are expecting an error
        # then you can continue with yuor statments in the else section after the exception
        try:
            x = int(input('enter number: ')) 
        except:
            print('thats not a number')
            continue
        else:
            print(f'{x} + 3 is: ', x + 3)
            print('{} - 3 is: '.format(x), x - 3)
            print('thats a number')
            break
        # this will run whether or not there is an error
        # so this can be used to make sure you properly close down certain things
        # such as database or something that needs to be done regardless if the code is successful or not
        finally:
            pass


in1()
