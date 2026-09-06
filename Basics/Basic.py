class Dog:
    def __init__(self,name):
        # Its technically not a constructor cause pythin already creates the object 

        self.name = name 
        # if init raises a value error then the obejct never was created 
    
    def __repr__(self):
        return f"Dog name {self.name}" 
        # Python calls this whn its neede ti dispaly your object in print() with it 
        # returing <__main__.Dog object at 0x7f...>.

    # Operators dunder such as __add__ , __mul__ , rmul__

    # a + b is  python is nothing but a.__add__(b)

class Point:
    def __init__(self,x):
        self.x =x 
    
    def __add__(self,other):
        return Point(self.x + other.x)
    
    def __repr__(self):
        return self.x

print(Point(3) + Point(4))


class Point:
    def __init__(self,x):
        self.x = x

    def __mul__(self,scalar):
        return Point(self.x * scalar)
    
    def __rmul__(self,scalar):
        return self.__mull__(scalar)
    
## Decorators Generaly 
# Its a function that takes a function and returs a modified function 
# @Foo abive def bar() means -> bar = foo(bar)

def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@shout
def great():
    return "hello"

print(great())

# @property method -> makes a method look like a  plain attribute no needed for ()

class Point:
    def __init__(self,x):
        self.x = x
    @property
    def doubled(self):
        return self. x * 2

p = Point(5)
print(p.doubled)

# @staticmethod -> gets neither cls or self , its a plain gunction that just lives isnide the class namespace because 
#  Tget dnt need a oarticular instace at all 


class Multiplier:
    @staticmethod
    def add(a,b):
        return a + b 

Multiplier.add(5,2)