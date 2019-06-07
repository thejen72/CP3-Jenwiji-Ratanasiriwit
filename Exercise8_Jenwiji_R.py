tissue = 25
water = 10
icecream = 15
bread = 35
banana = 8
watermelon = 50
powder = 20

print("----Welcome to ABC Shop----")
user = input("Username:    ")
password = input("Password:    ")
if user == "banana" and password == "123":
    print("You have logged in!")
    print("-------------------")
    print("Please input number of items needed!")
    tis = int(input("Tissue     25 THB:"))
    wat = int(input("Water      10 THB:"))
    ic = int(input("Icecream    15 THB:"))
    br = int(input("Bread       35 THB:"))
    ban = int(input("Banana     8 THB:"))
    wm = int(input("Watermelon  50 THB:"))
    pow = int(input("Powder     20 THB:"))
    print("Total Amount",
          tissue * tis +
          water * wat +
          icecream * ic +
          bread * br +
          banana * ban +
          watermelon * wm +
          powder * pow, "THB")
    print("Thank you for shopping at ABC Shop")

