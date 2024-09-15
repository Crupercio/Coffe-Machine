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
    "water": 900,
    "milk": 200,
    "coffee": 30,
}

def print_resources(current_resources, current_profits):
    key_list_res = list(current_resources.keys())

    print(f"{key_list_res[0].title()}: {current_resources[key_list_res[0]]}ml")
    print(f"{key_list_res[1].title()}: {current_resources[key_list_res[1]]}ml")
    print(f"{key_list_res[2].title()}: {current_resources[key_list_res[2]]}g")

    key_list_profits = list(current_profits.keys())
    print(f"{key_list_profits[0].title()}: ${current_profits[key_list_profits[0]]:.2f}")

def check_resources(current_resources, order_ingredients):
        all_resource = True
        for resource in order_ingredients:
            if all_resource == True:
                if current_resources[resource] >= order_ingredients[resource]:
                    all_resource = True
                else:
                    all_resource = False

        return all_resource
def remove_resources(current_resources, order_ingredients):
        for resource in order_ingredients:
            current_resources[resource] -= order_ingredients[resource]
def print_missing_resource(current_resources, order_ingredients):
    all_resource = True
    for resource in order_ingredients:
        if all_resource:
            if current_resources[resource] >= order_ingredients[resource]:
                all_resource = True
            else:
                all_resource = False
                return print(f"Sorry there is not enough {resource}.")

    return print("There is an error on checking for resources")

def procces_coins(coffe_cost, order):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    customer_money = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    if customer_money > coffe_cost:
        print(f"Here is ${customer_money-coffe_cost:.2f} in change.")
        print(f"Here is your {order}. Enjoy.")
        return coffe_cost
    elif customer_money == coffe_cost:
        print(f"Here is your {order}. Enjoy.")
        return coffe_cost
    else:
        return 0

#TODO 1: Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
coffe_machine_on = True
profits = {
    "money": 0.0,
}
while coffe_machine_on:
    customer_order = input("What would you like? (espresso/latte/cappuccino): ").lower()




    if customer_order == "off":
        coffe_machine_on = False
    elif customer_order == "report":
        print_resources(resources, profits)
    elif customer_order == "espresso":
        if check_resources(resources, MENU[customer_order]["ingredients"]):
            if procces_coins(MENU[customer_order]["cost"], customer_order) == 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                remove_resources(resources, MENU[customer_order]["ingredients"])
                money = profits["money"] + MENU[customer_order]["cost"]
                profits["money"] = money
        else:
            print_missing_resource(resources, MENU[customer_order]["ingredients"])
    elif customer_order == "latte":
        if check_resources(resources, MENU[customer_order]["ingredients"]):
            if procces_coins(MENU[customer_order]["cost"],customer_order) == 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                remove_resources(resources, MENU[customer_order]["ingredients"])
                money = profits["money"] + MENU[customer_order]["cost"]
                profits["money"] = money
        else:
            print_missing_resource(resources, MENU[customer_order]["ingredients"])
    elif customer_order == "cappuccino":
        if check_resources(resources, MENU[customer_order]["ingredients"]):
            if procces_coins(MENU[customer_order]["cost"],customer_order) == 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                remove_resources(resources, MENU[customer_order]["ingredients"])
                money = profits["money"] + MENU[customer_order]["cost"]
                profits["money"] = money
        else:
            print_missing_resource(resources, MENU[customer_order]["ingredients"])








