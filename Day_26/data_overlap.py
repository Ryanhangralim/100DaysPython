#read number from files
with open("file1.txt") as file:
    file_1 = [int(number) for number in file.readlines()]

with open("file2.txt") as file:
    file_2 = [int(number) for number in file.readlines()]

result = [number for number in file_1 if number in file_2]
print(result)