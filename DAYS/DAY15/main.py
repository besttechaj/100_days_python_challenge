
#* COFFEE MACHINE PROGRAM


MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.50},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.50},
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.00,
    },
}


machine_profit = 0

resources = {"water": 300, "milk": 200, "coffee": 100}

# cent
money_unit = {"penny": 0.01, "dime": 0.10, "nickel": 0.05, "quarter": 0.25}


def is_resource_sufficient(drink):
    """Check the status of the resources"""
    for ele in drink:
        if drink[ele] >= resources[ele]:
            print(f"Sorry there is not enough {ele}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coin")
    total_amount = int(input("How many quarters\n")) * 0.25
    total_amount += int(input("How many dimes\n")) * 0.1
    total_amount += int(input("How many nickels\n")) * 0.05
    total_amount += int(input("How many pennies\n")) * 0.01
    return total_amount


def transaction_details(paid_amount, drink_amount):
    """Return True if payment is accepted, or return False if money is insufficient"""

    if paid_amount >= drink_amount:
        change = round(paid_amount - drink_amount, 2)
        print(f"Here is ${change} in change.")
        global machine_profit
        machine_profit += drink_amount
        return True
    else:
        print("Sorry --> not enough money. Money refunded")
        return False


def make_a_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ..... !!! ")


is_on = True

while True:
    coffee = input("What would you like? (Espresso/ Latte/ Cappuccino)").lower()
    # if maintainer wants to work ( secret code )
    if coffee == "off":
        is_on = False
    elif coffee == "report":
        for ele in resources:
            print(f"\n{ele} : {resources[ele]}")
        print(f"\nMoney: {machine_profit}$")
        print("\n")
    else:
        # check whether do we have sufficient resources or not?
        drink = MENU[coffee]
        if is_resource_sufficient(drink["ingredients"]):
            payment_received = process_coins()
            print(f"You have paid {payment_received}$")
            if transaction_details(payment_received, drink["cost"]):
                make_a_coffee(coffee, drink["ingredients"])
