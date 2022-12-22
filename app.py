from flask import Flask,render_template,url_for
from flask import *
from datetime import datetime


app = Flask(__name__)
@app.route('/index/<user>')
def index(user):
    return render_template('index.html',name=user)

@app.route('/admin')
def hello_admin():
    return "Hello Admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello %s"%guest

@app.route('/user/<name>')
def hello_user(name):
    if name =="admin":
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

@app.route('/success/<name>')
def success(name):
    return "Welcome %s"%name

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))

@app.route('/getResult/<int:score>')
def getResult(score):
    return render_template('m.html',marks=score)



@app.route('/')
def student():
    return render_template('student.html')


@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        result=request.form
        return render_template('result.html',result=result)

if __name__ == "__main__":
    app.run(debug=True)