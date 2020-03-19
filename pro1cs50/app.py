from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/phpmyadmin/flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class USERS(db.Model):
    id=db.Column(db.INTEGER, primary_key=True)
    user=db.Column(db.String,unique=True)

    def __init__(self,id,user):
        self.id=id
        self.user=user

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/login.html')
def login():
    return render_template("project 1 cs50/html/login.html")
@app.route('/signup.html')
def signup():
    return render_template("project 1 cs50/html/signup.html")
@app.route('/settings.html')
def settings():
    return render_template("project 1 cs50/html/settings.html")
@app.route('/validate',methods=['GET','POST'])
def validate():
    if request.form=='POST':
        usr=request.form['username']
        db.session.add(USERS(user=usr))
        db.commit()
    else:
        return render_template('project 1 cs50/html/index.html')

if __name__ == '__main__':
    app.run(debug=True)
