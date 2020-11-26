class calc:
    #Overloading 
    def __init__(self, *a):
        self.a = a

    def avg(self):
        x = 0
        for i in self.a:
            x += i
        return x
    #Overloading 

    #Overriding
class A():
    def info(self):
        print('Im A')

class B(A):
    def info(self):
        print('Im B')
    #Overriding


#Overloading     
a = calc(1, 2, 3)# you can change the input number that can be accepted, you can send 1 or more number the method will still work
print(a.avg())
#Overloading 


#Overriding
B1 = B()
# as you can see info is a method available in class A and B, but still when i asked to print info statment it took the B method as it has been overriden even though it is a child class
B1.info()
#Overriding
