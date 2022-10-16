import sqlite3
from flask import Flask, redirect, url_for, render_template, request, session


def register_user_to_db(username, password):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('INSERT INTO users(username,password) values (?,?)', (username, password))
    con.commit()
    con.close()


def check_user(username, password):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('Select username,password FROM users WHERE username=? and password=?', (username, password))

    result = cur.fetchone()
    if result:
        return True
    else:
        return False


app = Flask(__name__)
app.secret_key = "r@nd0mSk_1"


@app.route("/")
def index(): 
    return render_template('log.html')


@app.route('/registers', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        register_user_to_db(username, password)
        return redirect(url_for('index'))

    else:
        return render_template('registers.html')


@app.route('/log', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(check_user(username, password))
        if check_user(username, password):
            return "welcome here you go!!!"
    else:
        return "Check your password!"

  
if __name__ == '__main__':
    app.run(debug=True)
