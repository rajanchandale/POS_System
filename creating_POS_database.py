import sqlite3

database = sqlite3.connect("POS_DATABASE.db")
c = database.cursor()
c.execute('''CREATE TABLE Products
(ProductID TEXT PRIMARY KEY,
ProductName TEXT,
ProductPrice TEXT,
ProductSpaces TEXT)''')

c.execute('''CREATE TABLE Transactions
(TransactionID TEXT PRIMARY KEY,
ReceiptFile TEXT,
TransactionDate TEXT,
TransactionTime TEXT)''')

c.execute('''CREATE TABLE Transaction_Products
(TransactionID TEXT,
ProductID TEXT,
Quantity INTEGER,
TransactionPrice REAL)''')

database.commit()
database.close()
