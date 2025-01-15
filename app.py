from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sign_up")
def sign_up():
    return render_template('sign_up.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/user_panel")
def user_panel():
    return render_template('user_panel.html')

@app.route("/admin_panel")
def admin_panel():
    return render_template('admin_panel.html')

if __name__ == "__main__":
    app.run()
