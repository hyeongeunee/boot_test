import pyodbc
#some other example server values are

server = '127.0.0.1' #to specify an alternate port port : 1433
database = 'DoItSQL'
username = 'sa'
password = 'qwer1234'

#ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always spec~~
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
cursor = conn.cursor()
cursor.execute("SELECT top 5 * from stock")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()