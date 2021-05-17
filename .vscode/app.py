from flask import Flask,render_template,request,url_for,session,redirect
from flask_mysqldb import MySQL,MySQLdb
import bcrypt
import pickle 
import numpy as np 

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PORT']=3308
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='disease'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)


@app.route('/')
def Home():
    return render_template("index.html")

@app.route('/login',methods=["GET","POST"])
def login():
    msg=' '
    if request.method == 'POST'and 'username' in request.form and 'password' in request.form:
        username=request.form['username']
        password = request.form['password']

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute('SELECT * FROM user WHERE username=%s and password=%s',(username,password,))
        user = curl.fetchone()
        curl.close()

        if user:
                session['loggedin']=True
                session['Username'] = user['Username']
                msg='Logged in successfully!'
                return render_template('disease.html',msg=msg)
        else:
            msg='Incorrect Details!'
    return render_template("login.html",msg=msg)
    

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (username,password) VALUES (%s,%s)",(username,password))
        mysql.connection.commit()
        session['username'] = request.form['username']
        return redirect(url_for('Home')) 



filename2 = 'heart.pkl'
mlp = pickle.load(open(filename2, 'rb'))


 
    

    
 

@app.route('/Heart')
def heart():return render_template('Heart.html')

@app.route('/disease')
def disease():return render_template('disease.html')



    
@app.route('/Heart', methods=['POST'])
def Heart():						

    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope= request.form['slope']
        ca = request.form['ca']
        thal=request.form['thal']
        data = np.array([[age, sex, cp, trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        my_prediction = mlp.predict(data)
        
        return render_template('heart_result.html', prediction=my_prediction)
    


if __name__=="__main__":
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(debug=True)
