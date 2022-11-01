from distutils.sysconfig import customize_compiler

from matplotlib.backend_bases import cursors
import dbconn as db
# Some other example server values are

conn = db.dbconn()
cursor = conn.cursor()
sql = '''insert into blog values
(N'첫번째 글제목', N'첫번째 글내용', N'/static/blog/img/img01.png'),
(N'첫번째 글제목', N'첫번째 글내용', N'/static/blog/img/img01.png')'''
cursor.execute(sql)
conn.commit()
conn.close()