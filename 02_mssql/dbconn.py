import pyodbc

def dbconn():
    server = '127.0.0.1' 
    database = 'DoItSQL'
    username = 'sa'
    password = 'qwer1234'
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    return conn

if __name__ == "__main__":
    print(__name__) #자기파일이 실행될때만 동작 / 다른파일에서 실행되면 동작x