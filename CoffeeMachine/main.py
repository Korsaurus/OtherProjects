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
    "money": 0
}


def coffee_machine():
    order = input(f"What would you like? (Espresso - ${MENU['espresso']['cost']}, Latte - ${MENU['latte']['cost']},"
                  f" Cappuccino - ${MENU['cappuccino']['cost']}):\n").lower()

    def get_report():
        rep = f"Water: {resources['water']}ml\n" f"Milk: {resources['milk']}ml\n" \
              f"Coffee: {resources['coffee']}g\n" f"Money: ${resources['money']}"
        return rep

    def make_coffee(drink):
        if not order == "espresso":
            milk_cost = MENU[drink]["ingredients"]["milk"]
            resources["milk"] -= milk_cost

        water_cost = MENU[drink]["ingredients"]["water"]
        coffee_cost = MENU[drink]["ingredients"]["coffee"]

        resources["water"] -= water_cost
        resources["coffee"] -= coffee_cost

        print(f"Here is your {order}, enjoy!")

    def check_resources(drink):
        for item in MENU[drink]["ingredients"]:
            if MENU[drink]["ingredients"][item] > resources[item]:
                print(f"Sorry, not enough {item}")
                return 0

    def prompt_payment():

        required_payment = MENU[order]["cost"]

        print("Please insert payment.")

        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickles?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01

        change = round((total - required_payment), 3)

        if total > required_payment:
            print(f"Your change is: ${change}, thank you!")
            resources["money"] += required_payment
        elif total == required_payment:
            resources["money"] += required_payment
        elif total < required_payment:
            print("Sorry, not enough money.")
            return 0

    if order == "off":
        return
    elif order == "report":
        report = get_report()
        print(report)
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        y = check_resources(order)
        if y == 0:
            return
        x = prompt_payment()
        if x == 0:
            return
        make_coffee(order)
    coffee_machine()


coffee_machine()
