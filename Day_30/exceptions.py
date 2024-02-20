try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.tx", "a")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
#code in else will run after try and exepts    
else:
    content = file.read()
    print(content)
#code in finally will always run no matter what
finally:
    file.close()