names = ["Ryan", "Bob", "Pedro", "Walter", "White", "Junior"]
short_names = [name.upper() for name in names if len(name) > 4]
print(short_names)