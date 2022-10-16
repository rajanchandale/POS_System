import sqlite3

currentItemsInfo = []

def linearSearchCurrentItems(desiredItem,returnVal):
    for item in currentItemsInfo:
        if item['itemName'] == desiredItem:
            if returnVal == "itemDict":
                return item
            elif returnVal == "itemIndex":
                return currentItemsInfo.index(item)
    return -1

def updateItemsInfoQty(itemName):
    print("UPDATE FUNC")
    print(currentItemsInfo)
    updateIndex = linearSearchCurrentItems(itemName,"itemIndex")
    currentItemsInfo[updateIndex]['quantity'] += 1

def updateTransactionPrice(itemName):
    database = sqlite3.connect("POS_DATABASE.db")
    c = database.cursor()
    c.execute('''SELECT ProductPrice FROM Products WHERE ProductName == ?''',(itemName,))
    productPrice = float(c.fetchall()[0][0])
    updateIndex = linearSearchCurrentItems(itemName, "itemIndex")
    currentItemsInfo[updateIndex]['transactionPrice'] = round(currentItemsInfo[updateIndex]['transactionPrice'] + productPrice,2)


