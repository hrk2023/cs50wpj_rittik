from flask import Flask, render_template,request


app = Flask(__name__)


@app.route('/index.html')
def index():
    return render_template("project 1 cs50/html/index.html")
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
        return render_template('project 1 cs50/html/home.html', uname=usr)
    else:
        return render_template('project 1 cs50/html/index.html')

if __name__ == '__main__':
    app.run(debug=True)
