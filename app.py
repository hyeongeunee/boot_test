from flask import Flask, render_template, request, redirect
import os
import dbconn as db

db.create_blog()

app = Flask(__name__)
#웹(C)에서 서버(S) > 따로 분리되서 관리 // + 요청(request) > 없으면 404 응답(response)

@app.route('/')
def index():
    print('/ 호출 들어옴') #나중에 세이브한 모델 여기에 넣어놓고 리턴해주면 됨
    return render_template('index.html') #html은 tem~에 넣고 이미지는 sta~에 넣으면됨

@app.route('/blog')
def blog():
    print('/blog 호출됨')
    return render_template('blog.html')

@app.route('/blog/<int:id>')
def blog_detail(id):
    print(f'/blog/{id}')
    conn = db.dbconn()
    cursor = conn.cursor()
    sql = '''select id,title,content,img_path,date from blog
            where id=?'''
    cursor.execute(sql, id)
    data = cursor.fetchone()
    print(data)
    conn.close()
    return render_template('blog_detail.html',data=data)

@app.route('/list')
def list():
    print('/list 호출됨')
    conn = db.dbconn()
    cursor = conn.cursor()
    sql = '''select id,title,content,img_path,date from blog'''
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    conn.close()
    return render_template('list.html', data=data)

@app.route('/user/<username>')
def show_username(username): #()안에 파라미터값으로 안에꺼 적어줘야함
    return f'username : {username}'

@app.route('/user/<username>/<int:age>')
def show_username_age(age,username):
    return f'이름은 {username} 나이는 {age}' 

@app.route('/user')
def show_user():
    return f'{request.args.get("age")}' #get 쓰면 없으면 없다고 해줌 (name1~~) / 안쓰면 그냥 오류 뜸.
    #get은 정보가 다 뜨기 때문에 개인정보 관련해서는 못씀.. 봐도 되는거는 post방식으로 사용

@app.route('/formtest', methods=['GET', 'POST'])
def formtest():
    if request.method == 'GET':
        return render_template('formtest.html')
    else:
        print(request.form)
        return render_template('result.html', data = request.form)
    
@app.route('/fileupload', methods=['GET', 'POST'])
def fileupload():
    if request.method == 'GET':
        return render_template('fileupload.html')
    else:
        f= request.files['up_file']
        path = os.path.dirname(__file__)+'/static/upload/'+f.filename
        # print(path)
        f.save(path)
        # print(request.form)
        conn = db.dbconn()
        cursor = conn.cursor()
        sql = '''insert into blog(title, content, img_path) values(?,?,?)'''
        data = (request.form['title'],request.form['content'],f.filename)
        cursor.execute(sql,data)
        conn.commit()
        conn.close()
        return redirect('/list')
        
@app.route('/blogdelete/<int:id>')
def blogdelete(id):
    conn = db.dbconn()
    cursor = conn.cursor()
    sql = 'delete from blog where id=?'
    cursor.execute(sql,id)
    conn.commit()
    conn.close()
    return redirect('/list')

@app.route('/blogupdate/<int:id>', methods=['GET'])
def blogupdateform(id):
        conn = db.dbconn()
        cursor = conn.cursor()
        sql = 'select id, title, content, img_path, date from blog where id=?'
        cursor.execute(sql,id)
        data = cursor.fetchone()
        conn.close()
        return render_template('blogupdate.html', data=data)
    
@app.route('/blogupdate', methods=['POST'])
def blogupdate():
    f= request.files['up_file']
    path = os.path.dirname(__file__)+'/static/upload/'+f.filename
    # print(path)
    f.save(path)
    # print(request.form)
    conn = db.dbconn()
    cursor = conn.cursor()
    sql = '''update blog
    set title = ?,
        content = ?,
        img_path = ?,
        date = getdate()
    where id = ?
    '''
    data = (request.form['title'], request.form['content'], f.filename, request.form['id'])
    cursor.execute(sql,data)
    conn.commit()
    conn.close()
    return redirect('/list')

if __name__=="__main__":
    app.run(port=80, debug=True) #웹서비스 기본포트 : 80 