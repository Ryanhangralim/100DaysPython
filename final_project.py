MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#initialize variables
profit = 0

#initialize functions
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}gr")
    print(f"Money: ${profit}")


def calculate_money(quarters, dimes, nickles, pennies):
    total = quarters * 0.25
    total += dimes * 0.1
    total += nickles * 0.05
    total += pennies * 0.01
    return total


def is_available(drink_ingredients):
    for ingredient in drink_ingredients:
        if resources[ingredient] < drink_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def payment_successful(money, drink_price):
    if money < drink_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money >= drink_price:
        global profit
        change = round(money - drink_price, 2)
        profit += drink_price
        print(f"Here is ${change} dollars in change.")
        return True


def make_coffee(drink):
    drink_ingredients = MENU[drink]['ingredients']
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {drink}. Enjoy!")

def main():
    on = True
    while on:
        user_choice = input("What would you like? (espresso/latte/cappuccino):")
        if(user_choice == "off"):
            on = False
        elif(user_choice == "report"):
            print_report()
        else:
            drink = MENU[user_choice]
            if(is_available(drink['ingredients'])):
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                user_money = calculate_money(quarters, dimes, nickles, pennies)
                if(payment_successful(user_money, drink['cost'])):
                    make_coffee(user_choice)


if __name__ == "__main__":
    main()