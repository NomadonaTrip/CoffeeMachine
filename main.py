from MENU import MENU
from MENU import resources

money = 0
# A function to print a report of available coffee ingredients and their respective quantities
def report():
    for resource in resources:
        print(f"{resource}:  {resources[resource]}")
    print(f"Money:  ${money}")



# A function to convert the numerals typed in by users into coffee choices
def selection():
    print("What would you like? Espresso/latte/ cappuccino")
    coffee_choice = input("Choose '1' for Espresso, '2' for Latte or '3' for Cappuccino: ")
    if coffee_choice == "1":
        return "espresso"
    elif coffee_choice == "2":
        return "latte"
    elif coffee_choice == "3":
        return "cappuccino"
    elif coffee_choice == "report":
        return "report"


choice = selection()
# Receives the choice made by the user and either prints a report or informs them of their coffee selection.


def payment():

    this_sale = 0
    pennies = int(input(f"How many pennies: "))
    pennies = 0.01 * pennies
    this_sale += pennies
    print(f"This sale: {this_sale}")
    nickels = int(input("How many nickels: "))
    nickels = 0.05 * nickels
    this_sale += nickels
    print(f"This sale: {this_sale}")
    dimes = int(input("How many dimes: "))
    dimes = 0.10 * dimes
    this_sale += dimes
    print(f"this sale: {this_sale}")
    quarters = int(input("How many quarters:"))
    quarters = 0.25 * quarters
    this_sale += quarters
    print(f"This sale: {this_sale}")
    readytobuy = input("Ready to checkout? Type 'y' or 'n'").lower()
    if readytobuy == "y":
        print(f"This sale is: {this_sale}")
    return this_sale


def checkout(this_sale, money):

    if this_sale < MENU[choice]["cost"]:
        print(f"Sorry, that's not enough money. {this_sale} refunded")
    else:
        money += this_sale
        for resource in resources:
            resources[resource] -= MENU[choice]["ingredients"][resource]
        change = this_sale - MENU[choice]["cost"]
        if change != 0:
            print(f"Here's your change: {change}")

        print("Brewing...\n")
        print("Brewing...\n")
        print("Brewing...\n")
        print(f"Here's your {choice} ☕, enjoy!")


resource_list = ["water", "milk", "coffee"]

def check_resource(choice):
    for resource in resource_list:
        if MENU[choice]["ingredients"][resource] >= resources[resource]:
            print(f"Sorry, there is not enough {resource}")
            return

    print("Please insert coins")
    payment_amount = payment()
    checkout(payment_amount, money = money)

make_coffee = "y"
while make_coffee == "y":
    if choice == "report":
        report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        print(f"{choice}, great choice!")
        check_resource(choice)
        make_coffee = input("Would you like to make another coffee? type 'y' or 'n': ")
        choice = selection()

    else:
        print("please choose a coffee variant or request a report")






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

