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