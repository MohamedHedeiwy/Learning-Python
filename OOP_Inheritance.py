class A:
    def __init__(self):
        print('Class A constructor')

    def feature1(self):
        print('this is feature 1')


# SINGLE LEVEL INHERITANCE
class B(A):
    def __init__(self):
        # to call A constructor use super
        super().__init__()
        print('Class B constructor')

    def feature2(self):
        print('this is feature 2')


# MULTI LEVEL INHERITANCE AS C IS INHERITING B, WHERE B IS ALSO INHERITING A SO THAT MEANS C HAS ACCESS TO BOTH A AND B
class C(B):
    def feature3(self):
        print('this is feature 3')


class D():
    def feature4(self):
        print('this is feature 4')


class E():
    def feature5(self):
        print('this is feature 5')


# THIS IS MULTIPLE INHERITENCE
class F(D, E):
    def feature6(self):
        print('this is feature 6')


b = B()
