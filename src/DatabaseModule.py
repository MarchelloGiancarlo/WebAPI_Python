import pyodbc


class ShippingListDB:
    def __init__(self):
        self.dbConnection = pyodbc.connect('Driver={SQL Server};'
                                           'Server=DESKTOP-EH0BFR0;'
                                           'Database=WebAPI_Python_DB;'
                                           'Trusted_Connection=yes;')

    def getElementList(self):
        cursor = self.dbConnection.cursor()
        cursor.execute('select * from WebAPI_Python_DB.dbo.ShoppingList')
        return list(cursor)

    def addElement(self, name, quantity):
        cursor = self.dbConnection.cursor()
        cursor.execute("insert into ShoppingList(name, quantity) values (?, ?)", str(
            name), str(quantity))
        self.dbConnection.commit()
        return


if __name__ == "__main__":
    database = ShippingListDB()
    elements = database.getElementList()
    for element in elements:
        print("name:"+str(element.name)+"-quantity:"+str(element.quantity))

    database.addElement("polpette", 1000)
    elements = database.getElementList()
    for element in elements:
        print("name:"+str(element.name)+"-quantity:"+str(element.quantity))
