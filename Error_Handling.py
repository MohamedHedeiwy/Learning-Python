def add(a,b):
    try:
        print(a+b)
    except:
        print('you got an error')
    else:
        print('you got no error')

def add1(a,b):
    try:
        x = a+b
    except:
        print('you got an error')
    else:
        print('you got no error')
        return print(x)

print('add')
add(12,2)

print()

print('add1')
add1(12,2)

def in1():
    while True:
        try:
            x = int(input('enter number: '))
        except:
            print('thats not a number')
            continue
        else:
            print('thats a number')
            break

in1()