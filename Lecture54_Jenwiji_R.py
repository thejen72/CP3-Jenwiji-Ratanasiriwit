def login():
    user = input("Username: ")
    pw = input("Password: ")
    if user == "jen" and pw == "apple":
        return showmenu()
    else:
        return False
def showmenu():
    print("Please choose your menu")
    print("Menu 1. VAT Calculator")
    print("Menu 2. Price Calculator")
    menuSelect()
def menuSelect():
    choice = int(input("Input Menu Number:  "))
    if choice == 1:
        print("Total price + VAT:   ", vatCalculator(int(input("Please input your total price:  "))))
    elif choice == 2:
        print("Total price + VAT:   ",priceCalculator())
    return choice
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculator():
    print("Welcome to price calculator")
    price1 = int(input("Price of first product:     "))
    price2 = int(input("Price of second product:    "))
    return vatCalculator(price1 + price2)

login()

