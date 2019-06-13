itemList = []
priceList = []

def myReceipt():
    total =0
    for myItems in range(len(itemList)):
        print(itemList[myItems], priceList[myItems])
        total += int(priceList[myItems])
    print("Total amount:    ", total)

print("welcome to my supermarket")
while True:
    item = input("Please input item:     ")
    if(item.lower()=="exit"):
        break
    else:

        price = input("Please input price:  ")
        itemList.append(item)
        priceList.append(price)

myReceipt()