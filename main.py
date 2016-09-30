from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

user = {"userName" : "Joel", "password" : "password"}

@app.route("/")
def home():
    return render_template('form.html')

@app.route("/makeAccount/" methods = ['POST'])
def newAccount():
    d = request.form
    if (validateAccount(d)):
        makeAccount(d["userName"], hashlib.sha512(d["password"]).hexdigest())
    render_template('makeAccount.html', success = validateAccount(request.form))

@app.route("/authen/", methods = ['POST'])
def auth():
    d = request.form #works like dictionary
    if accountCheck(d["userName"], d["password"]):
        return "COOL"#return render_template('validate.html', success = True)
    return "NOT COOL"#return render_template('validate.html', success = False)

def accountCheck(userName, password):
    return userName == user["userName"] and password == user["password"] 

def validateAccount(d):
    return d["pass1"] == d["pass2"] and len(d["userName"]) > 0 and len(d["pass1"]) > 0

def makeAccount(name, hashed):
    object = open("data/users.csv", "w")
    object.write(name + "," + hashed + "\n")
    object.close()

if __name__ == "__main__":
    app.debug = True
    app.run()
