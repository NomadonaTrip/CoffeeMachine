from MENU import MENU
from MENU import resources
from MENU import units

money = 0

def payment():
    """This function collects coins (pennies, nickels, dimes and quarters) and returns the value of the
    collected coins"""
    print("Please insert coins")
    received = int(input("How many pennies? ")) *0.01
    #print(f"{received} received")
    received += int(input("How many nickels? ")) * 0.05
    #print(f"{received} received")
    received += int(input("How many dimes? ")) * 0.10
    #print(f"{received} received")
    received += int(input("How many quarters? ")) * 0.25
    print(f"${received} received" )
    return received

def notsufficient(resources, choice):
    for resource in resources:
        if MENU[choice]["ingredients"][resource] > resources[resource]:
            return True



coffee_active = True
while coffee_active == True:
    choice = input("What would you like? Espresso, latte or cappuccino? ")
    """This section triggers takes in the word 'off' as an input and returns a False value for coffee_active
    to turn off the coffee machine"""

    if choice == "off":
        coffee_active = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money:${money}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        print(f"{choice} is a great choice!")
        insufficient = notsufficient(resources, choice)



        if insufficient:
            for resource in resources:
                if MENU[choice]["ingredients"][resource] > resources[resource]:
                    print(f"Sorry, there is not enough {resource}")
        else:
            userpay = payment()
            if userpay < MENU[choice]["cost"]:
                print(f"Sorry, that's not enough money.${userpay} refunded.")
            elif userpay >= MENU[choice]["cost"]:
                money += MENU[choice]["cost"]
                change = round(userpay - MENU[choice]["cost"],2)
                for resource in resources:
                    resources[resource] -= MENU[choice]["ingredients"][resource]
                print(f"Here's your {choice}, enjoy!")
                if change != 0:
                    print(f"Here's ${change} in change")















#1: Ask the user for their choice of coffee

#2: Generate a report on available resources and cash in the till
# Check whether there are sufficient resources to deliver the coffee requested
#3.1: Create variables to access resource levels and coffee choice requirements
#3.2: Create a function to compare water, milk and coffee levels with the required quantity for coffee choice

#4: Request for payment, collecting pennies, quarters, nickels and dimes. Confirm payment completion and return a
# floating point cash evaluation
#4.1: Request for
#5: Check if cash payment covers cost of coffee requested and refund if criteria not met
#6: Return change if payment exceeds cost of coffee
#7: Add coffee price to cash in store and deduct resources from inventory
#8: Deliver coffee

