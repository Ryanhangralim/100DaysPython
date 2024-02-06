from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    #defining objects
    menu = Menu()
    coffeeMaker = CoffeeMaker()
    moneyMachine = MoneyMachine()

    on = True
    while on:
        user_choice = input(f"What would you like? ({menu.get_items()}):")
        if(user_choice == "off"):
            on = False
        elif(user_choice == "report"):
            coffeeMaker.report()
            moneyMachine.report()
        else:
            drink = menu.find_drink(user_choice)
            if(drink):
                if(coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost)):
                    coffeeMaker.make_coffee(drink)
                    

if __name__ == "__main__":
    main()