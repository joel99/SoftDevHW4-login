from flask import Flask, render_template, request

app = Flask(__name__)

user = {"userName" : "Joel", "password" : "password"}

@app.route("/")
def home():
    return render_template('form.html')

@app.route("/authen/", methods = ['POST'])
def auth():
    d = request.form #works like dictionary
    if d["userName"] == user["userName"] and d["password"] == user["password"]:
        return "COOL"#return render_template('validate.html', success = True)
    return "NOT COOL"#return render_template('validate.html', success = False)

if __name__ == "__main__":
    app.debug = True
    app.run()
