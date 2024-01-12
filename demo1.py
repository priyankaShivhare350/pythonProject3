import sys

def generator(x):
    for i in range(x):
        yield i

print(sys.getsizeof(range(8999999)))
print(sys.getsizeof(generator(8999999)))


class A:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self,value):
        self.__name=value

    @staticmethod
    def mymethod():
        print("hello")

obj=A("maya",67)
# print(obj._A__name)
print(obj.Name)
obj.Name="pop"
print(obj.Name)

A.mymethod()

##type indicator
def myfunct(A : int ,B :str)->str:
    print(A,B)
    return "1"
myfunct(9,"9")

