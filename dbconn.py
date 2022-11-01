import pyodbc

def dbconn():
    server = '127.0.0.1' 
    database = 'DoItSQL'
    username = 'sa'
    password = 'qwer1234'
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    return conn

def create_blog():
    conn = dbconn()
    cursor = conn.cursor()
    sql = '''IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'blog')
	create table blog(
	id int identity not null primary key,
	title nvarchar(255) not null,
	content nvarchar(1000) not null,
	img_path nvarchar(255),
	date datetime default getdate()
    )'''
    cursor.execute(sql)
    conn.commit()
    conn.close()