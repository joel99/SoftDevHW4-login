from flask import Flask, render_template, request
import hashlib, csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('form.html')

@app.route("/makeAccount/", methods = ['POST'])
def newAccount():
    d = request.form
    if (validateAccount(d)):
        makeAccount(d["userName"], hashlib.sha512(d["pass1"]).hexdigest())
    return render_template('makeAccount.html', success = validateAccount(request.form))

@app.route("/authen/", methods = ['POST'])
def auth():
    d = request.form #works like dictionary
    return render_template("loggedin.html", success = accountCheck(d["userName"], d["pass"]))
#login

def accountCheck(userName, password):
    reader = csv.reader(open("data/users.csv", "r"))
    if userName == "CLEAR" and password == "CLEAR":
        clearAllAccounts()
    d = {}
    for row in reader:
        k, v = row
        d[k] = v
    if not userName in d.keys():
        return False
    else:
        return hashlib.sha512(password).hexdigest() == d[userName] 


#making new account
def validateAccount(d):
    return d["pass1"] == d["pass2"] and len(d["userName"]) > 0 and len(d["pass1"]) > 0

def makeAccount(name, hashed):
    print "we're making it"
    data = open("data/users.csv", "a")
    data.write(name + "," + hashed + "\n")
    data.close()

def clearAllAccounts():
    data = open("data/users.csv", "w")
    data.write("")
    data.close()
    
if __name__ == "__main__":
    app.debug = True
    app.run()
