from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail,Message
from linkedin_api import Linkedin
import requests
import pandas as pd
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail as mls
## email.mime subclasses
# Default dictionary: store a list with each key
import pandas as pd 
import csv
import os
import json
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=vtw87306;PWD=7Ekg9bFtTZv9f9XV",'','')
print(conn)
print("success")
var_list = []
PROXYCURL_API_KEY = 'lIlwGU7otjlj1tbuyMfhlQ'  # todo - fill this field up


app = Flask(__name__)
app.secret_key='a'
mail = Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kanthimathiiyyappan01@gmail.com'
app.config['MAIL_PASSWORD'] = 'djjeadqqalirhtqo'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def home():
  return render_template('login.html')

@app.route('/linkpass')
def linkpass():
  return render_template('linked.html')

@app.route('/MyProfile')
def MyProfile():
  return render_template('My Profile.html')

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
@app.route('/MyProfile',methods=["POST", "GET"])
def profile():
  return render_template('My Profile.html',data=dict)

@app.route('/prev',methods=["POST", "GET"])
def prev():
  return render_template('skill.html')


@app.route('/gojob',methods=["POST", "GET"])
def gojob():
    print("job")
    search_term=request.form['job']
    locations:request.form['loc']

    url = "https://indeed11.p.rapidapi.com/"

    payload = {
      "search_terms": "Marketing",
      "location": "United States",
      "page": "1"
    }
    headers = {
      "content-type": "application/json",
      "X-RapidAPI-Key": "be7fd5b032msh2de06b9e53f0850p1ce4b9jsna154c022de5a",
      "X-RapidAPI-Host": "indeed11.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    html=response.text
    print(response.text)
    dict=json.loads(html)
    print(dict)
    return render_template('dashboard.html',data=dict)
@app.route('/register',methods=["POST", "GET"])
def register():
  return render_template('register.html')


@app.route('/linkedlogin',methods=["POST", "GET"])
def linkedlogin():
  username = request.form['username']
  # password= request.form['password']
  # email = request.form['email']
  # api=Linkedin("bhuvanameenakshinathan@gmail.com","bhuvaneswari18#M")
  # print("sdf")
  # print(api.get_profile_skills("www.linkedin.com/in/bhuvaneswari-m-a24a431a2"))
  api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
  header_dic = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
  params = {
      'url': f'https://www.linkedin.com/in/{username}',
  }
  response = requests.get(api_endpoint,
                          params=params,
                          headers=header_dic)
  print(response.json())
  return render_template('skill.html')


@app.route('/confirm',methods=["POST", "GET"])
def confirm():
  print("hi")
  msg = Message('Registration successfully completed', sender = 'kanthimathiiyyappan01@gmail.com', recipients = [var_list[0]])
  msg.body = "Thank You for registering in Skill/Job recommendation application and Submit your resume in your profile section and Can apply for your desired jobs"
  mail.send(msg)
  print("hj")
  return render_template('Application form.html')

@app.route('/subapp',methods=["POST", "GET"])
def subapp():
  insert_sql = "INSERT INTO DETAILSB (NAME,FNAME,GENDER,EID,ADDRESS,TENTHMARK,TWELTHMARK,DEG_CGPA,AADHAR,DOMAIN)  VALUES (?,?,?,?,?,?,?,?,?,?)"
  prep_stmt = ibm_db.prepare(conn, insert_sql)
  name = request.form['yourname']
  fname = request.form['fname']
  GD = request.form['GD']
  EID = request.form['EID']
  add = request.form['AL1']
  mark1 = request.form['s5']
  mark2 = request.form['h5']
  cgpa = request.form['b5']
  AADHAR = request.form['Aadhar']
  DOMAIN = request.form['domain']

  ibm_db.bind_param(prep_stmt, 1, name)
  ibm_db.bind_param(prep_stmt, 2, fname)
  ibm_db.bind_param(prep_stmt, 3, GD)
  ibm_db.bind_param(prep_stmt, 4, EID)
  ibm_db.bind_param(prep_stmt, 5, add)
  ibm_db.bind_param(prep_stmt,6, mark1)
  ibm_db.bind_param(prep_stmt,7, mark2)
  ibm_db.bind_param(prep_stmt, 8, cgpa)
  ibm_db.bind_param(prep_stmt, 9, AADHAR)
  ibm_db.bind_param(prep_stmt, 10, DOMAIN)

  print("giun")
  ibm_db.execute(prep_stmt)
  # message = mls(
  # from_email='kanthimathiiyyappan01@gmail.com',
  # to_emails='1912005@nec.edu.in',
  # subject='Your Application has been Saved',
  # html_content='<strong>Further you can edit the application form in your profile section and continue your job searching and apply to it</strong>')
  # try:
  #   sg = SendGridAPIClient(os.environ.get('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'))
  #   response = sg.send(message)
  #   print(response.status_code)
  #   print(response.body)
  #   print(response.headers)
  # except Exception as e:
  #   print(e.message)
  msg = Message('Your Application has been Saved', sender = 'kanthimathiiyyappan01@gmail.com', recipients = [EID])
  msg.body = "Further you can edit the application form in your profile section and continue your job searching and apply to it"
  mail.send(msg)
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

