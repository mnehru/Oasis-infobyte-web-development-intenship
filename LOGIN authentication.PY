pip install Flask
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a random secret key

users = {}  # Store user data (username: password)

@app.route("/")
def index():
    return "Welcome to the login authentication system!"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users[username] = password
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.get(username) == password:
            session["username"] = username
            return redirect(url_for("secured_page"))
        else:
            return "Invalid username or password. Please try again."
    return render_template("login.html")

@app.route("/secured")
def secured_page():
    if "username" in session:
        return "Welcome to the secured page, " + session["username"] + "!"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
