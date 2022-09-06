from decimal import Decimal

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

total_profit = 0.00


def print_report():
    print(f"""
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}g
    Money: ${total_profit}
    """)


def add_profit(money):
    global total_profit
    total_profit += money


def resources_are_sufficient(drink_order):
    menu_drink = MENU[drink_order]
    are_sufficient = True

    for ingredient in menu_drink["ingredients"]:
        quantity = menu_drink["ingredients"][ingredient]
        if not resources[ingredient] >= quantity:
            print(f"Sorry there is not enough {ingredient}.")
            are_sufficient = False

    return are_sufficient


# TODO: 5. Process coins.


def process_coins():
    print("Please insert coins")
    quarters = int(input("quarters: ")) * 25
    dimes = int(input("dimes: ")) * 10
    nickles = int(input("nickles: ")) * 5
    pennies = int(input("pennies: "))
    dollars = (quarters + dimes + nickles + pennies) // 100
    change = (quarters + dimes + nickles + pennies) % 100

    if len(str(change)) == 1:
        change *= 10

    return float(f"{dollars}.{change}")


def is_transaction_successful(drink_order, money):
    menu_order_cost = MENU[drink_order]["cost"]
    if money < menu_order_cost:
        print(f"Sorry that's not enough money. ${money} refunded.")
        return -1
    else:
        add_profit(menu_order_cost)
        change = Decimal(f'{money}') - Decimal(f'{menu_order_cost}')
        print(f"Here is ${change} in change.")
        return change


def make_coffee(drink_order):
    menu_order_ingredients = MENU[drink_order]["ingredients"]

    for ingredient in menu_order_ingredients:
        resources[ingredient] -= menu_order_ingredients[ingredient]

    print_report()
    print(f"Here is your {drink_order}. Enjoy!")


orders_pending = True
while orders_pending:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == 'off':
        orders_pending = False
    else:
        while not order == "espresso" and not order == "latte" and not order == "cappuccino":
            order = input("Not a valid option. What would you like? (espresso/latte/cappuccino): ")

        coins = process_coins()

        if int(is_transaction_successful(order, coins)) >= 0 and resources_are_sufficient(order):
            make_coffee(order)



