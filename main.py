from MENU import MENU
from MENU import resources
from MENU import units
from debug_coffeemachine import choice

money = 0



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
        print(f"{"choice"} is a great choice!")









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

