import time 

def delay_decorator(function):
    def wrapper_functions():
        time.sleep(2)
        function()
        function()
    
    return wrapper_functions

@delay_decorator
def say_hi():
    print("HI")

say_hi()