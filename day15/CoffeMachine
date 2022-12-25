from data import MENU, resources

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"money: {money}$")


def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for key in ingredients:
        if resources[key] < ingredients[key]:
            return False
    return True 


def get_money():
    print("Please insert coins:")
    coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0,
    }
    for key in coins:
        coins[key] = int(input(f"How many {key}?: "))
    return 0.25*coins["quarters"] + 0.1*coins["dimes"] + 0.05*coins["nickles"] + 0.01*coins["pennies"]


def process_order(user_money, user_choice, money, resources):
    change = user_money - MENU[user_choice]["cost"]
    print(f"Here is your {change:.1f}$ change.")
    print(f"Here is your {user_choice}. Enjoy!")
    money += MENU[user_choice]["cost"]
    for key in MENU[user_choice]["ingredients"]:
        resources[key] -= MENU[user_choice]["ingredients"][key]
    return money, resources

money = 0
turn_off = False
while not turn_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    #to turn the machine off
    if user_choice == "off":
        turn_off = True
    #to show the report
    elif user_choice == "report":
        report()
    #to process the order
    else:
        #if there is enough resources
        if check_resources(user_choice):
            user_money = get_money()
            #check if the input money is enough
            if user_money < MENU[user_choice]["cost"]:
                print("​Sorry that's not enough money. Money refunded.​")
            else:
                money, resources = process_order(user_money, user_choice, money, resources)
        else:
            print("Sorry there is not enough resources.")

