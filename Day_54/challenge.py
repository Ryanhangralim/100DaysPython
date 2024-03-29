import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    def check_time():
        start_time = time.time()
        function()
        finish_time = time.time()
        print(f"{function.__name__} run speed: {finish_time - start_time}")
    return check_time

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()