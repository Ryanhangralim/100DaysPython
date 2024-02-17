# '*' allows multiple positional argument to be passed
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    print(total)

add(1,2,3,4,5)

# '**' allows multiple keyword argument to be passed
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, color="red", **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = color

my_car = Car(make="Nissan", color="blue")
print(my_car.model)
print(my_car.color)