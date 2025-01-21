from flask import Flask, render_template, url_for, request, redirect
from main import hotel_sys
from admin import admin
from hotel import hotel
from dll import dll
from hotel_time import hotel_date
app = Flask(__name__)
h_sys = hotel_sys()
adm = admin()

@app.route("/", methods = ['POST', 'GET'])
def index():
    time = h_sys.time.time.date()
    
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
        return render_template('index.html',
                               title = 'HOME',
                               time = time)

@app.route("/sign_up", methods = ['POST', 'GET'])
def sign_up():
    time = h_sys.time.time.date()
    
    if request.method == 'POST':
        sign_up_result = h_sys.sign_up(request.form['username'], request.form['password'])
        
        if sign_up_result == True:
            return redirect("/login")
        else:
            return render_template('sign_up.html',
                                title = 'Sign Up',
                                error = sign_up_result,
                                time = time)
        
    return render_template('sign_up.html',
                           title = 'SIGN UP',
                           time = time)

@app.route("/login", methods = ['POST', 'GET'])
def login():
    time = h_sys.time.time.date() 
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = h_sys.login(username, password)
        if result == True:
            return redirect('/user_panel')
        else:
            return render_template('login.html',
                                    error = result,
                                    title = 'LOGIN',
                                    time = time)
        
    return render_template('login.html')

@app.route("/admin_login", methods = ['POST', 'GET'])
def admin_login():
    time = h_sys.time.time.date()
    
    if request.method == 'POST':
        if request.form['username'] == adm.username and request.form['password']:
            h_sys.admin_is_logged = True
            return redirect('/admin_panel')
        else:
            return render_template('admin_login.html',
                                    error = "Wrong Username or Password",
                                    title = 'ADMIN LOGIN',
                                    time = time) 

    return render_template('admin_login.html',
                           title = 'ADMIN LOGIN',
                           time = time)

@app.route("/user_panel", methods = ['POST', 'GET'])
def user_panel():
    time = h_sys.time.time.date()
    res_error=''
    if request.method == 'POST':
        if 'res_by_id' in request.form:
            try:
                start_date = hotel_date(request.form["res_start_y"],
                                        request.form["res_start_m"],
                                        request.form["res_start_d"])
                
                end_date = hotel_date(request.form["res_start_y"],
                                        request.form["res_start_m"],
                                        request.form["res_start_d"])
                
                res_error = h_sys.res_by_id(request.form['reserve_id'],
                                            start_date,
                                            end_date)
            except:
                res_error = 'Room ID cannot be empty or invalid date(s)'

    return render_template('user_panel.html',
                           reserve_error = res_error,
                            time = time)

@app.route("/admin_panel", methods = ['POST', 'GET'])
def admin_panel():
    time = h_sys.time.time.date()    

    if h_sys.admin_is_logged == False:
        return redirect("/admin_login")
    
    if h_sys.hotel == None:
        return redirect("/make_hotel")
    
    make_room_error = ''
    filter_error = ''

    if request.method == "POST":
        if 'make_room' in request.form:
            try:   
                make_room_error = h_sys.hotel.add_room(int(request.form['floor']),
                                int(request.form['number']),
                                int(request.form['beds']))
            except:
                make_room_error = 'Please fill all 3 Fields'
        
        if 'change_day' in request.form:
            h_sys.go_next_day()
            return redirect("/admin_panel")
    
            
    rooms = h_sys.hotel.get_all_rooms().data
    temp_rooms = dll()

    if request.method == "POST":
        if 'filter_by_floor' in request.form:
            if request.form['filter_by_floor'] == '':
                pass
            else:
                try:
                    filter_floor = int(request.form['filter_by_floor'])
                    if filter_floor < 0 or filter_floor > h_sys.hotel.floors:
                        filter_error = 'Invalid Floor value'
                    else:    
                        rooms = h_sys.hotel.rooms.get_row(filter_floor).data
                except:
                    filter_error = 'Invalid Floor value'

            
        if 'filter_by_bed_c' in request.form:
            if request.form['filter_by_bed_c'] == '':
                pass
            else:
                try:
                    filter_bed_c = int(request.form['filter_by_bed_c'])
                    if filter_bed_c < 0 or filter_bed_c > 5:
                        filter_error = 'Invalid bed value'
                    else:
                        for room in rooms:
                            if room != None:
                                if room.beds == filter_bed_c:
                                    temp_rooms.add_first(room)
                        rooms = temp_rooms.get_as_list().data
                except:
                    filter_error = 'Invalid bed value'

        

    return render_template('admin_panel.html',
                            title = 'ADMIN PANEL',
                            time = time,
                            rooms = rooms,
                            make_room_error = make_room_error,
                            filter_error = filter_error)

@app.route("/make_hotel", methods = ['POST', 'GET'])
def make_hotel():
    time = h_sys.time.time.date() 
    
    if request.method == 'POST':
        try:
            h_sys.hotel = hotel(int(request.form['floor_number']))
            return redirect("/admin_panel")
        except:
            return render_template('make_hotel.html',
                                    error = "Invalid floor value",
                                    title = 'MAKE HOTEL',
                                    time = time)
    else:
        return render_template('make_hotel.html',
                                title = 'MAKE HOTEL',
                                time = time)

if __name__ == "__main__":
    app.run()
