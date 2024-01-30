programming_dictionary = {
    123 : "This is 1 2 3"
}
print(programming_dictionary[123])

programming_dictionary[234] = "This is 2 3 4"

print(programming_dictionary[234])

if 234 in programming_dictionary.keys():
    print("Exist")

programming_dictionary[123] = "This is 1 2 3 but better"

print(programming_dictionary[123])

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

for city in travel_log["France"]["cities_visited"]:
    print(city)
print(f'Total visits: {travel_log["France"]["total_visits"]}')

travel_log2 = [
    {
        "country" : "Japan",
        "cities_visites" : ["Tokyo", "Hokaido", "Osaka"],
        "total_visits": 12
    }
]

print(travel_log2[0]["country"])