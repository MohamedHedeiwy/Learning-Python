def add(*a):
    x = 0
    for i in a:
        x += i
    return x


def sub(*a):
    x = []
    for i in a:
        x.append(i)
    x.sort(reverse=True)
    print(x)
    f = x[0]
    for i in range(1, len(x)):
        f -= x[i]
    return f


def fact(a):
    x = 1
    for i in range(1, a+1):
        x = x * i
    return x



