# '*' allows multiple argument to be passed
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    print(total)

add(1,2,3,4,5)