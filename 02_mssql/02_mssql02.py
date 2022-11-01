import dbconn as db
#Some other example server values are

conn = db.dbconn()
cursor = conn.cursor()
sql = '''IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'blog')
	create table blog(
	id int identity not null primary key,
	title nvarchar(100) not null,
	content nvarchar(255) not null,
	img_path nvarchar(100)
)'''
cursor.execute(sql)
conn.commit()
conn.close()