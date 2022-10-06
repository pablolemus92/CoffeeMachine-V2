from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

menu_ = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    options = menu_.get_items()
    user_choice = input(f"What would you like? ({options}): ")
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu_.find_drink(user_choice)
        #print(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

