from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=vtw87306;PWD=7Ekg9bFtTZv9f9XV",'','')
print(conn)
print("success")

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('skill.html')


