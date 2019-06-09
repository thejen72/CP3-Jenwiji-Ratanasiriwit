totalPrice = int(input("Please input price:  "))
def vatCalculator(totalPrice):
    result = (totalPrice*7/100)+totalPrice
    return result
print(vatCalculator(totalPrice))
