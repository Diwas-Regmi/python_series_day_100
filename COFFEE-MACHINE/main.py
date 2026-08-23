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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_sufficient_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry! There is not Enough {item}")
            return False
    return True
def make_coffee(item_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {item_name}")

def calculate_total():
    print("Insert Coins: ")
    total = int(input("How many Quarters: "))* 0.25
    total += int(input("How many dimes: "))* 0.10
    total += int(input("How many nickles: "))* 0.05
    total += int(input("How many pennies: "))* 0.01
    return total
is_on = True
while is_on:

    choice = input("What would you like? (espresso/cappuccino/latte): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water = {resources["water"]}ml")
        print(f"Milk = {resources["milk"]}ml")
        print(f"Coffee = {resources["coffee"]}g")
        print(f"Money = ${profit}")
    else:
        drink = MENU[choice]
        if is_sufficient_enough(drink["ingredients"]):
            payment = calculate_total()
            make_coffee(choice, drink["ingredients"])


