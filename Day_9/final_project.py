from art import logo

#initialize variables
bids = {}
choice = 'yes'

#menu
print(logo)
print("Welcome to the secret auction program.")

def add_bidders(name, bid):
    bids[name] = bid


def get_result():
    highest_bid = 0
    for keys in bids:
        if bids[keys] > highest_bid:
            highest_bid = bids[keys]
            highest_bid_name = keys
    print(f"The winner is {highest_bid_name} with a bid of ${highest_bid}.")


while choice == "yes":
    name = input("What is your name? : ")
    bid = int(input("What's your bid?: $"))
    add_bidders(name, bid)
    choice = input("Are there another bidders? Type 'yes' of 'no'.\n")
get_result()