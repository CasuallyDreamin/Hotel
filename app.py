from flask import Flask, render_template, url_for, request, redirect
from main import hotel_sys
from admin import admin
from hotel import hotel

app = Flask(__name__)
h_sys = hotel_sys()
adm = admin()

@app.route("/", methods = ['POST', 'GET'])
def index():
    if h_sys.hotel == None:
        if h_sys.curr_user != adm:
            return redirect('/admin_login')
        else:
            return redirect('/admin_panel')
        
    if request.method == 'POST':
        if "create-account" in request.form:
            return redirect("/sign_up")
        elif "log-in" in request.form:
            return redirect("/login")
    else:
        return render_template('index.html')

@app.route("/sign_up", methods = ['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        sign_up_result = h_sys.sign_up(request.form['username'], request.form['password'])
        
        if sign_up_result == True:
            return redirect("/login")
        else:
            return render_template('sign_up.html', error = sign_up_result)
        
    return render_template('sign_up.html')

@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = h_sys.login(username, password)
        if result == True:
            return redirect('/user_panel')
        else:
            return render_template('login.html', error = result)
        
    return render_template('login.html')

@app.route("/admin_login", methods = ['POST', 'GET'])
def admin_login():
    if request.method == 'POST':
        if request.form['username'] == adm.username and request.form['password']:
            h_sys.admin_is_logged = True
            return redirect('/admin_panel')
        else:
            return render_template('admin_login.html', error = "Wrong Username or Password") 

    return render_template('admin_login.html', error = "")

@app.route("/user_panel", methods = ['POST', 'GET'])
def user_panel():
    return render_template('user_panel.html')

@app.route("/admin_panel", methods = ['POST', 'GET'])
def admin_panel():
    if h_sys.admin_is_logged == False:
        return redirect("/admin_login")
    
    if h_sys.hotel == None:
        return redirect("/make_hotel")
         
    return render_template('admin_panel.html')

@app.route("/make_hotel", methods = ['POST', 'GET'])
def make_hotel():
    if request.method == 'POST':
        try:
            h_sys.hotel = hotel(int(request.form['floor_number']))
            return redirect("/admin_panel")
        except:
            return render_template('make_hotel.html', error = "Invalid floor value")
    else:
        return render_template('make_hotel.html', error = '')

if __name__ == "__main__":
    app.run()
