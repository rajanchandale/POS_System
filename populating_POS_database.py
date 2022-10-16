import sqlite3

itemsInfo = [{"itemName":"Papdi Chaat","quantity":0,"price":2.99,"transactionPrice":0,"spaces":2},
             {"itemName":"Aloo Tikki Chaat","quantity":0,"price":2.99,"transactionPrice":0,"spaces":2},
             {"itemName":"Daulat Ki Chaat","quantity":0,"price":2.99,"transactionPrice":0,"spaces":2},
             {"itemName":"Samosa Chaat", "quantity":0, "price":2.99, "transactionPrice":0,"spaces":2},
             {"itemName":"Chicken Tikka Wrap","quantity":0,"price":3.99, "transactionPrice":0,"spaces":1},
             {"itemName":"Kebab Wrap","quantity":0,"price":3.99,"transactionPrice":0,"spaces":3},
             {"itemName":"Mixed Wrap","quantity":0,"price":4.99, "transactionPrice":0,"spaces":3},
             {"itemName":"Paneer Wrap","quantity":0,"price":3.99, "transactionPrice":0,"spaces":2},
             {"itemName":"Lamb Samosa","quantity":0,"price":1.99,"transactionPrice":0,"spaces":2},
             {"itemName":"Veg Samosa","quantity":0,"price":1.49,"transactionPrice":0,"spaces":3},
             {"itemName":"Fish Pakora","quantity":0,"price":1.99,"transactionPrice":0,"spaces":2},
             {"itemName":"Veg Pakora","quantity":0,"price":1.49,"transactionPrice":0,"spaces":3},
             {"itemName":"Chole Bhature","quantity":0,"price":5.99,"transactionPrice":0,"spaces":2},
             {"itemName":"Spring Rolls","quantity":0,"price":1.49, "transactionPrice":0,"spaces":2},
             {"itemName":"Gol Gappe","quantity":0,"price":2.99, "transactionPrice":0,"spaces":3},
             {"itemName":"Masala Chips","quantity":0,"price":2.29, "transactionPrice":0,"spaces":2},
             {"itemName":"Chutney","quantity":0,"price":0.49, "transactionPrice":0,"spaces":3},
             {"itemName":"Mint Chutney","quantity":0,"price":0.49, "transactionPrice":0,"spaces":2},
             {"itemName":"Raita","quantity":0,"price":0.79, "transactionPrice":0,"spaces":3},
             {"itemName":"Salad","quantity":0,"price":0.89, "transactionPrice":0,"spaces":3},
             {"itemName":"Poppadoms","quantity":0,"price":0.99, "transactionPrice":0,"spaces":3},
             {"itemName":"Coca-Cola","quantity":0,"price":1.39, "transactionPrice":0,"spaces":3},
             {"itemName":"Diet Coke","quantity":0,"price":1.39, "transactionPrice":0,"spaces":3},
             {"itemName":"Limca", "quantity":0,"price":1.69, "transactionPrice":0,"spaces":3},
             {"itemName":"ThumsUp","quantity":0,"price":1.69, "transactionPrice":0,"spaces":3},
             {"itemName":"Water","quantity":0,"price":0.99, "transactionPrice":0,"spaces":3},
             {"itemName":"Juice","quantity":0,"price":0.99, "transactionPrice":0,"spaces":3},
             {"itemName":"Masala Chai","quantity":0,"price":1.99, "transactionPrice":0,"spaces":2},
             {"itemName":"Karak Chai","quantity":0,"price":1.99, "transactionPrice":0,"spaces":3},
             {"itemName":"Lassi","quantity":0,"price":1.89, "transactionPrice":0,"spaces":3}]

def updateProductID(productID):
    numPart = int(productID[4:])
    numPart += 1
    numPart = str(numPart)
    while len(numPart) != 5:
        numPart = "0" + numPart
    return "PROD"+numPart

database = sqlite3.connect("POS_DATABASE.db")
c = database.cursor()

productID = "PROD00000"
for item in itemsInfo:
    productID = updateProductID(productID)
    c.execute('''INSERT INTO Products VALUES(?,?,?,?)''',(productID,item['itemName'],item['price'],item['spaces']))

database.commit()
database.close()












