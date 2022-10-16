import sqlite3
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

def processIndividualAnalysis(searchBySelection, searchForSelection, timeSelection):
    database = sqlite3.connect("POS_DATABASE.db")
    c = database.cursor()
    analysis = []
    todayDate = date.today()
    requiredDate = determineDateRange(timeSelection[0])
    for name in searchForSelection:
        runningQty = 0
        runningRev = 0
        for selection in searchBySelection:
            if selection == "Units Sold":
                c.execute('''SELECT Transaction_Products.Quantity
        FROM Transaction_Products, Products, Transactions
        WHERE ProductName = ? AND Transactions.TransactionDate BETWEEN ? AND ? AND
        Products.ProductID = Transaction_Products.ProductID AND
        Transactions.TransactionID = Transaction_Products.TransactionID ''',(name,requiredDate,todayDate,))
                results = c.fetchall()
                for result in results:
                    runningQty += int(result[0])
                new = True
                for data in analysis:
                    if data['name'] == name:
                        data['quantity'] = runningQty
                        new = False
                if new == True:
                    analysis.append({"name":name, "revenue":None,"quantity":runningQty})
            elif selection == "Revenue":
                c.execute('''SELECT Transaction_Products.TransactionPrice
        FROM Transaction_Products, Products, Transactions
        WHERE ProductName = ? AND Transactions.TransactionDate BETWEEN ? AND ? AND
        Products.ProductID = Transaction_Products.ProductID AND
        Transactions.TransactionID = Transaction_Products.TransactionID ''',(name,requiredDate,todayDate,))
                results = c.fetchall()
                for result in results:
                     runningRev += float(result[0])
                new = True
                for data in analysis:
                    if data['name'] == name:
                        data['revenue'] = runningRev
                        new = False
                if new == True:
                    analysis.append({"name":name,"revenue":runningRev,"quantity":None})

    database.commit()
    database.close()
    return analysis

def receiptRetrieval(timeSelections):
    database = sqlite3.connect("POS_DATABASE.db")
    c = database.cursor()
    values = []
    for time in timeSelections:
        todayDate = date.today()
        requiredDate = determineDateRange(time)
        c.execute('''SELECT Transactions.ReceiptFile, Transactions.TransactionDate,Transactions.TransactionTime
    FROM Transactions
    WHERE Transactions.TransactionDate BETWEEN ? AND ?''',(requiredDate,todayDate,))
        values.append(c.fetchall())
    return values


def customReceiptRetrieval(startDate,endDate):
    database = sqlite3.connect("POS_DATABASE.db")
    c = database.cursor()
    c.execute('''SELECT Transactions.ReceiptFile, Transactions.TransactionDate, Transactions.TransactionTime
    FROM Transactions
    WHERE Transactions.TransactionDate BETWEEN ? AND ?''',(startDate,endDate,))
    return c.fetchall()


def determineDateRange(time):
    if time == "7 Days":
        return date.today() - datetime.timedelta(days=7)
    elif time == "1 Month":
        return date.today() + relativedelta(months=-1)
    elif time == "3 Months":
        return date.today() + relativedelta(months=-3)
    elif time == "6 Months":
        return date.today() + relativedelta(months=-6)
    elif time == "1 Year":
        return date.today() + relativedelta(months=-12)
    elif time == "3 Year":
        return date.today() + relativedelta(months=-36)
    elif time == "All-Time":
        return "0000-01-01"



    
