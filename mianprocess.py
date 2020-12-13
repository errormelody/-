from flask import Flask,request,render_template,redirect,session
import json
import time
import pymysql
app = Flask (__name__)
app.secret_key = "ajkdhkjankjxdwkea"

haha = ''
haha2 = {}
user = ''
password = ''
target = ''
a=''
b=''
c=''
d=''
e=''
reason =''
backdate = ''
newkey = ''
@app.route('/main', methods=['GET','POST'])
def m():
    return render_template("主界面.html")
@app.route('/', methods=['GET','POST'])
def login():
    session['referer'] = 'http://127.0.0.1:5000/'
    global haha
    if request.method == 'GET':
         return render_template('login&.html')
    if request.method == 'POST':
        global user
        user = request.form.get('user')
        print (user)
        global password
        password = request.form.get('password')
        haha = mysql_deal()
        if user =="":
            haha = '登录失败'
            putup4()
            return redirect('/',code=302)
        elif haha == None:
            haha = '没有该用户名，登陆失败'
            putup4()
            return redirect('/', code=302)
        elif haha['login_password'] == password:
            session['user_info'] = user
            haha = '登陆成功'
            putup4()
            return redirect('/first', code=302)
        else:
            haha = '密码错误，登陆失败'
            putup4()
            return redirect('/', code=302)


@app.route('/sign',methods = ['GET','POST'])
def sign_in():
    session['referer'] = 'http://127.0.0.1:5000/sign'
    global target
    global haha
    global haha2
    user_info = session.get('user_info')
    if  request.method == "GET"and user_info:
        return render_template('sign&.html')
    elif request.method == "GET"and not user_info:
        print(2)
        return redirect('/',code = 302)
    if request.method == 'POST':
        num = request.form.get('num')
        target = session.get('user_info')
        if num =='1':
            haha = mysql_deal6()
            putup4()
            return render_template('sign&.html')
        elif num == '0':
            global backdate
            global reason
            month = request.form.get('month')
            date = request.form.get('date')
            year = request.form.get('year')
            backdate = year +"-"+ month + "-" + date
            reason = request .form . get('reason')
            print (reason)
            haha2 = mysql_deal7()
            putup3()
            haha = ''
            return render_template('sign&.html')
        else :
            return render_template('first&&.html')

@app.route('/first',methods=['GET','POST'])
def deal_with():
    user_info = session.get('user_info')
    referrer = session.get('referer')
    print(referrer)
    if  request.method == "GET"and user_info and referrer == 'http://127.0.0.1:5000/':
        session['referer'] = 'http://127.0.0.1:5000/first'
        referrer = session.get('referer')
        print(1)
        return render_template('first&&.html')
    elif request.method == "GET"and user_info :
        print(1)
        return render_template('first&.html')
    elif request.method == "GET"and not user_info:
        print(2)
        return redirect('/',code = 302)
    if request.method == 'POST':
        global num
        global target
        global changenum
        global changewhat
        global a,b,c,d,e
        num = request.form.get('num')
        target = request.form.get('target')
        changenum = request.form.get('changenum')
        changewhat = request.form.get('changewhat')
        a = request.form.get('a')
        b = request.form.get('b')
        c = request.form.get('c')
        d = request.form.get('d')
        e = request.form.get('e')
        global haha2
        global haha
        if num == '1':
            haha2 = mysql_deal2()
            putup3()
        elif num == '2':
            haha = mysql_deal3()
            putup4()
            haha = ''
        elif num == '3':
            haha = mysql_deal4()
            putup4()
            haha = ''
        elif num == '4':
            haha = mysql_deal5()
            putup4()
            haha = ''
        elif num == '-1':
            pass
        num = '-1'
        return render_template('first&.html')
@app.route('/putup2', methods=['GET', 'POST'])
def putup3():
    global haha2
    print(haha2)
    return haha2
@app.route('/putup', methods=['GET', 'POST'])
def putup4():
    global haha
    return haha
@app.route('/person',methods=['GET','POST'])
def person_deal():
    user_info = session.get('user_info')
    global target
    target = user_info
    global newkey
    if request.method == "GET" and user_info:
        return render_template('person.html')
    elif request.method == "GET" and not user_info:

        return redirect('/', code=302)
    if request.form == 'POST':
        oldkey = request .form.get('oldkey')
        newkey = request .form .get('newkey')
        global haha
        haha2 = mysql_deal()
        if haha2['name'] == oldkey:
            haha = '1'
            putup4()
            mysql_deal8()
        else:
            haha = '0'
            putup4()
        return render_template('persom.html')


def mysql_deal():
    conn = pymysql.connect(host = 'localhost',port = 3306 , user = 'root',password = 'error', db = '软工设计')
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    global user
    cursor.execute("select login_password  from login where login_user=%s",[user,])
    obj = cursor.fetchone()
    conn .commit()
    cursor.close()
    conn.close()
    return obj
def mysql_deal2():
    conn = pymysql.connect(host = 'localhost',port = 3306 , user = 'root',password = 'error', db = '软工设计')
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    global target
    cursor.execute("select *  from allpeople where peoplename =%s",[target,])
    obj = cursor.fetchone()
    conn .commit()
    cursor.close()
    conn.close()
    return obj
def mysql_deal3():
    conn = pymysql.connect(host = 'localhost',port = 3306 , user = 'root',password = 'error', db = '软工设计')
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    global a,b,c,d,e
    cursor.execute("insert into allpeople value (%s,%s,%s,%s,%s)",[a,b,c,d,e,])
    cursor.execute("insert into sign value (%s, '00-00-00','00-00-00' ,' ')",[a,])
    obj = cursor.fetchone()
    conn .commit()
    cursor.close()
    conn.close()
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''
    return '1'
def mysql_deal4():
    conn = pymysql.connect(host = 'localhost',port = 3306 , user = 'root',password = 'error', db = '软工设计')
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    global target
    cursor.execute("delete from allpeople where peoplename = %s",[target,])
    obj = cursor.fetchone()
    conn .commit()
    cursor.close()
    conn.close()
    return '1'
def mysql_deal5():
    conn = pymysql.connect(host = 'localhost',port = 3306 , user = 'root',password = 'error', db = '软工设计')
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    global a,b,c,d,e
    cursor.execute("update allpeople set peoplename= %s,peoplesex= %s ,peopleemail =%s,peoplestudentnum =%s,peoplephone = %s where peoplename = %s",[a,b,c,d,e,target,])
    obj = cursor.fetchone()
    conn .commit()
    cursor.close()
    conn.close()
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''
    return '1'
def mysql_deal6():
    conn = pymysql.connect(host = 'localhost',port = 3306 , user = 'root',password = 'error', db = '软工设计')
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    global target
    print(1)
    start_trans = time.strftime("%Y-%m-%d", time.localtime())
    print(start_trans)
    cursor.execute("update sign set signdate =%s where signname = %s",[start_trans,target,])
    obj = cursor.fetchone()
    conn .commit()
    cursor.close()
    conn.close()
    return start_trans
def mysql_deal7():
    conn = pymysql.connect(host = 'localhost',port = 3306 , user = 'root',password = 'error', db = '软工设计')
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    global target
    global reason
    global backdate
    global haha
    cursor.execute("update sign set backdate =%s,reason =%s where signname = %s",[backdate,reason,target,])
    obj = cursor.fetchone()
    conn .commit()
    cursor.close()
    conn.close()
    return {'backdate':backdate,'reason':reason}
def mysql_deal8():
    conn = pymysql.connect(host = 'localhost',port = 3306 , user = 'root',password = 'error', db = '软工设计')
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    global target
    global newkey
    cursor.execute("update allpeople set login_password =%s where login_user = %s",[newkey,target,])
    obj = cursor.fetchone()
    conn .commit()
    cursor.close()
    conn.close()
    return '1'
if __name__ == '__main__':
    app.run()
