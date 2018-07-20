from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Employee:
    def __init__(self, name, lastname, age):
        pass

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        if request.form["username"] == 'user' and request.form["password"] == "secret":
            return  redirect("/table/20&20")


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/user")
def user():
    return render_template('index.html')

@app.route("/greeting/<username>&<int:rep>")
def greeter(username, rep):
    name = username
    return ("<h1>hello {name}</h1>".format(name=name))*rep


@app.route("/table/<int:w>&<int:h>")
def show_table(w, h):
    return  render_template('table.html', width=w, height=h)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)