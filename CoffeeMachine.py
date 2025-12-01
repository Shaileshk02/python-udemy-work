#  Prompt user by asking “ What would you like? (espresso/latte/cappuccino):​
# Espresso : 1.2, Latte : 1.35, Cappuccino : 2.45


def make_coffee (sChoice):
    check_resources(sChoice)
    print("making coffee")
    update_resources()
    print("Enjoy the coffee")

def check_resources(sChoice):
    if sChoice == "Espresso":
        if water < 100:
            print("Water is insufficient")
        elif coffee < 50:
            print("Coffee is insufficient")
        elif milk < 50:
            print("milk is insufficient")

    elif sChoice == "Latte":
        if water < 250:
            print("Water is insufficient")
        elif coffee < 36:
            print("Coffee is insufficient")
        elif milk < 65:
            print("milk is insufficient")

    elif sChoice == "Cappuccino":
        if water < 136:
            print("Water is insufficient")
        elif coffee < 26:
            print("Coffee is insufficient")
        elif milk < 45:
            print("milk is insufficient")


            
def calculate_money(sChoice):
    coin_25 = 0
    coin_10 = 0
    coin_05 = 0
    coin_01 = 0
    temp = 0
    cost = 0

    if sChoice == "Espresso":
        cost = 120
    elif sChoice == "Latte":
        cost = 135
    elif sChoice == "Cappuccino":
        cost = 248
    else:
        print("wrong choice")
        return
        
    coin_25 = cost/25
    temp = cost%25
    coin_10 = temp/10
    temp = temp%10
    coin_05 = temp/5
    temp = temp%5
    coin_01 = temp

    print("25 paise coin required : " + str(int(coin_25)))
    print("10 paise coin required : " + str(int(coin_10)))
    print("5 paise coin required : " + str(int(coin_05)))
    print("1 paise coin required : " + str(coin_01))    



def update_resources():
    global water
    global milk
    global coffee

    print("updating resources")
    if sChoice == "Espresso":
        water = water - 100
        coffee = coffee - 50
        milk = milk - 50
    elif sChoice == "Cappuccino":
        water = water - 136
        coffee = coffee - 26
        milk = milk - 45
    elif sChoice == "Latte":
        water = water - 250
        coffee = coffee - 36
        milk = milk - 65

    calculate_money(sChoice)



# main below
water = 500
milk = 2000
coffee = 560
money = 15

while True : 
    sChoice = input("What would you like? Espresso/Latte/Cappuccino ?")
    print(sChoice)

    if sChoice == "off":
        print("machine is shutting down")
        break
    
    if sChoice == "report":
        print_report()
    elif sChoice == "Espresso" or sChoice == "Latte" or sChoice == "Cappuccino":
        make_coffee(sChoice)
    else:
        print("Wrong selection")



def print_report():
    print("here is report")

def make_coffee (sChoice):
    check_resources(sChoice)
    print("making coffee")
    update_resources()
    print("Enjoy the coffee")

def check_resources(sChoice):
    global water
    global milk
    global coffee

    if sChoice != "Espresso":
        if water < 100:
            print("Water is insufficient")
        elif coffee < 50:
            print("Coffee is insufficient")
        elif milk < 50:
            print("milk is insufficient")

    elif sChoice != "Latte":
        if water < 250:
            print("Water is insufficient")
        elif coffee < 36:
            print("Coffee is insufficient")
        elif milk < 65:
            print("milk is insufficient")

    elif sChoice != "Cappuccino":
        if water < 136:
            print("Water is insufficient")
        elif coffee < 26:
            print("Coffee is insufficient")
        elif milk < 45:
            print("milk is insufficient")


