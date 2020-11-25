# the x and y are formal arguments
def add(x ,y): # if you dont want to pass x and y you can create a defualt value for example setting y = 12, this means if u pass one argument which is x only it will take y as 12
    a = x + y
    b = x - y
    return a,b

def test(x,y):
    a = x + y
    b = x - y
    return a,b

# the 4 and 5 are actual arguments
add ,sub = add(11, 12)
print(add,sub)

# another way of calling a function if you forgot the order, this is a keyword argument
add ,sub = test(x = 4, y = 5)
print(add, sub)



# the * before data means it is accepting more than one argument
def person(name, *data):
    print(name)
    print(data)
    #because it is stored as a tuple so if you want to print it individually you have to pass it through a loop 
    for a in data:
        print(a)
#here the 12 and Egypt are unknown
person('Mohamed', 12, 'Egypt')

# now if data is receving more than one argument we need to know what will it be receiving so we have to give a keyword varibale thats why we used ** which means there is a keyword variable neing received
def person1(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
#here we can flag 12 and Egypt with a variable as the function is using ** , this means data will be stored as a dictionary  
person1('Mohamed', age = 12, city = 'Egypt')


# Check this for better function control https://www.youtube.com/watch?v=eci9iU_s6Ag&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=38
# Check this to get a deep understanding of how variables are passed to functions https://www.youtube.com/watch?v=ijXMGpoMkhQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=37