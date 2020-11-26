# Use upper case for each word when naming a class for example StudentId OR MohamedMustafa
class Computer:
    # Class variable
    brand = 'Level 51'

    # to use class variable you have to use class methods, you have to declare its a class method by using the @classmethod
    # the @ is also known as decorators
    @classmethod
    def getBrandName(cls):
        return cls.brand

    # if you dont want to relate the method to a class or a object keep it empty this will mean its a static method
    # this will be helphul if you want to perform any operations
    # have to use #staticmethod so that python would know that this is a static method
    @staticmethod
    def info():
        return 10 + 5

    def __init__(self, cpu, ram, memory):  # constructor
        # object/instance variable
        self.cpu = cpu
        self.ram = ram
        self.memory = memory

    def config(self):
        print(self.cpu, self.ram, self.memory)


a = Computer('Ryzen 9', '16gb', '500gb SSD')
b = Computer('Ryzen 5', '16gb', '1000gb SSD')
a.config()
b.config()
print('this is the class method: ', Computer.getBrandName())
print('this is the static method: ', Computer.info())

# can access class variable through object or through class name
print(a.brand)
print(Computer.brand)

# using object name to change class variable will only change the variable for that object only
a.brand = 'Dell'
print('Brand for object a after using object a to change class variable: ', a.brand)
print('Brand for object b after using object a to change class variable: ', b.brand)
# using class name to change the class variable will change the value for all objects
Computer.brand = 'Dell'
print('Brand for object a after using object a to change class variable: ', a.brand)
print('Brand for object b after using class name to change variable: ', b.brand)
