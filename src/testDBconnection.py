import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-EH0BFR0;'
                      'Database=WebAPI_Python_DB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('select * from WebAPI_Python_DB.dbo.ShoppingList')

for row in cursor:
    print(row)
