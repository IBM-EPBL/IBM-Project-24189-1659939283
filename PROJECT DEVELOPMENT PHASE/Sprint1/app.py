from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail,Message
import pandas as pd
import os
## email.mime subclasses

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=vtw87306;PWD=7Ekg9bFtTZv9f9XV",'','')
print(conn)
print("success")
var_list = []

app = Flask(__name__)
app.secret_key='a'
mail = Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kanthimathiiyyappan01@gmail.com'
app.config['MAIL_PASSWORD'] = 'axhymixsgxvrhmyd'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def home():
  return render_template('login.html')


@app.route('/skillreg',methods=["POST", "GET"])
def dashhome():
  insert_sql = "INSERT INTO SKILLUSERB (EMAILID, PASSWORD, NAME,PHONENUMBER)  VALUES (?,?,?,?)"
  prep_stmt = ibm_db.prepare(conn, insert_sql)
  email = request.form['username']
  password= request.form['password']
  name = request.form['name']
  ph = request.form['phonenum']
  var_list.append(email)
  var_list.append(password)
  var_list.append(name)
  var_list.append(ph)
  ibm_db.bind_param(prep_stmt, 1, email)
  ibm_db.bind_param(prep_stmt, 2, password)
  ibm_db.bind_param(prep_stmt, 3, name)
  ibm_db.bind_param(prep_stmt, 4, ph)
  print("giun")
  ibm_db.execute(prep_stmt)
  return render_template('email.html')


@app.route('/register',methods=["POST", "GET"])
def register():
  return render_template('register.html')

@app.route('/confirm',methods=["POST", "GET"])
def confirm():
  print("hi")
  msg = Message('Registration successfully completed', sender = 'kanthimathiiyyappan01@gmail.com', recipients = [var_list[0]])
  msg.body = "Thank You for registering in Skill/Job recommendation application and Submit your resume in your profile section and Can apply for your desired jobs"
  mail.send(msg)
  print("hj")
  return render_template('skill.html')

@app.route('/skilllogin',methods=["POST", "GET"])
def login():
  msg = ''
  if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
      email = request.form['username']
      password = request.form['password']

      sql = "SELECT * FROM SKILLUSERB WHERE EMAILID =? AND PASSWORD =?"
      stmt = ibm_db.prepare(conn, sql)
      ibm_db.bind_param(stmt,1,email)
      ibm_db.bind_param(stmt,2,password)
      ibm_db.execute(stmt)
      account = ibm_db.fetch_assoc(stmt)

      if account:
          msg = 'Logged in successfully !'
          return render_template('skill.html', msg = msg)
      else:
          msg = 'Incorrect email / password !'
  return render_template('login.html', msg = msg)




