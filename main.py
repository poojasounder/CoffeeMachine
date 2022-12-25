from menu import MENU, resources

MONEY = 0


def modify_resources(curr_order):
    water_required = MENU[curr_order]['ingredients']['water']
    coffee_required = MENU[curr_order]['ingredients']['coffee']
    resources['water'] = resources['water'] - water_required
    resources['coffee'] = resources['coffee'] - coffee_required
    if curr_order != 'espresso':
        milk_required = MENU[curr_order]['ingredients']['milk']
        resources['milk'] = resources['milk'] - milk_required


def enough_resources(curr_order):
    flag = True
    if resources['water'] < MENU[curr_order]['ingredients']['water']:
        print("Sorry there is not enough " + 'water')
        flag = False
    if resources['coffee'] < MENU[curr_order]['ingredients']['coffee']:
        print("Sorry there is not enough " + 'coffee')
        flag = False
    if curr_order != 'espresso':
        if resources['milk'] < MENU[curr_order]['ingredients']['milk']:
            print("Sorry there is not enough " + 'milk')
            flag = False
    if flag:
        modify_resources(curr_order)
    return flag


def process_coins(curr_order,quarters,dimes,nickles,pennies):
    given_money = float((quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01))
    actual_cost = MENU[curr_order]['cost']
    if given_money < actual_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif given_money > actual_cost:
        balance = round((given_money - actual_cost), 2)
        print(f"Here is ${balance} in change.")
        print(f"Here is your {curr_order}. Enjoy!")
        return True
    else:
        print(f"Here is your {curr_order}. Enjoy!")
        return True


should_continue = True

while should_continue:
    order = input("What would you like to have? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${MONEY}")
    elif order == "off":
        should_continue = False
    else:
        if enough_resources(order):
            print("Please insert coins.")
            num_quarters = int(input("how many quarters?: "))
            num_dimes = int(input("how many dimes?: "))
            num_nickles = int(input("how many nickles?: "))
            num_pennies = int(input("how many pennies?: "))
            if process_coins(order, num_quarters, num_dimes, num_nickles, num_pennies):
                MONEY = MONEY + MENU[order]['cost']

