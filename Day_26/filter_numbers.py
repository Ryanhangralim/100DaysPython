list_of_strings = input().split(",")

even_numbers = [int(number) for number in list_of_strings if int(number) % 2 == 0]

print(even_numbers)