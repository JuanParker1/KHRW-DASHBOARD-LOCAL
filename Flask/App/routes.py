import os
import pandas as pd

from flask import render_template, redirect, url_for, flash, request
from App import app, db, bcrypt


from App.forms import RegistrationForm, LoginForm, UpdateProfileForm, UserManagementForm, StationForm
from App.models import User, Station
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@login_required
def home():
    return render_template(template_name_or_list="home.html")


@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            password=form.password.data).decode(encoding='utf-8')
        user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(message="ثبت نام شما با موفقیت انجام شد!", category='success')
        return redirect(location=url_for(endpoint='home'))

    return render_template(template_name_or_list='register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(location=url_for(endpoint='home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(pw_hash=user.password, password=form.password.data):
            login_user(user=user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(message="ورود شما با موفقیت انجام شد!", category='success')
            return redirect(location=next_page if next_page else url_for(endpoint='home'))
        else:
            flash(message="نام کاربری یا رمز عبور وارد شده صحیح نمیباشد!",
                  category='danger')
    return render_template(template_name_or_list='login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(message="شما با موفقیت از حساب کاربری خود خارج شده اید!",
                  category='success')
    return redirect(location=url_for(endpoint='login'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.password = hashed_password = bcrypt.generate_password_hash(
            password=form.password.data).decode(encoding='utf-8')
        db.session.commit()
        flash(message="حساب کاربری شما با موفقیت به روزرسانی شد!",
              category='success')
        return redirect(location=url_for(endpoint='home'))
    elif request.method == 'GET':
        pass
    return render_template(template_name_or_list='profile.html', form=form)


@app.route('/delete/<int:id>')
@login_required
def delete(id):
    user_to_delete = User.query.get_or_404(id)
    
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect(location=url_for(endpoint='user_management'))
    except:
        return "اوپسس ..."
    




@app.route('/user_management')
@login_required
def user_management():  
    users = User.query.all()
    return render_template(template_name_or_list='user_management.html', users=users)


@app.route('/precipitation')
@login_required
def precipitation():
    return render_template(template_name_or_list='precipitation_flask/precipitation.html')

@app.route('/precipitation/dashboard')
@login_required
def precipitation_dashboard():
    return render_template(template_name_or_list='precipitation_flask/base.html')



@app.route('/precipitation/dashboard/station_managment')
@login_required
def precipitation_dashboard_station_management():  
    stations = Station.query.all()
    return render_template(template_name_or_list='precipitation_flask/station_managment.html', stations=stations)



@app.route('/precipitation/dashboard/add_station', methods=["GET", "POST"])
@login_required
def precipitation_dashboard_add_station():
    form = StationForm()
    if form.validate_on_submit():
        station = Station(
            stationName = form.stationName.data,
            stationCode = form.stationCode.data,
            stationOldCode = form.stationOldCode.data,
            drainageArea6 = form.drainageArea6.data,
            drainageArea30 = form.drainageArea30.data,
            areaStudyName = form.areaStudyName.data,
            omor = form.omor.data,
            county = form.county.data,
            startYear = form.startYear.data,
            longDecimalDegrees = form.longDecimalDegrees.data,
            latDecimalDegrees = form.latDecimalDegrees.data,
            elevation = form.elevation.data,
        )
               
        db.session.add(station)
        db.session.commit()
        flash(message=f"ایستگاه جدید با نام {form.stationName.data} و کد {form.stationCode.data} به دیتابیس اضافه گردید!", category='success')
        return redirect(url_for('precipitation_dashboard_add_station'))
    return render_template(
        template_name_or_list='precipitation_flask/add_station.html', 
        form=form
    )
    
    
@app.route('/precipitation/dashboard/add_station_csv', methods=['POST', 'GET'])
@login_required
def precipitation_dashboard_add_station_csv():
    if request.method == "POST":
        file = request.files['file']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return render_template(
            template_name_or_list='precipitation_flask/add_station_csv.html'
        )
    return render_template(
        template_name_or_list='precipitation_flask/add_station_csv.html'
    )


@app.route('/delete_station/<int:stationCode>')
@login_required
def deleteStation(stationCode):
    station_to_delete = Station.query.get_or_404(stationCode)    
    try:
        db.session.delete(station_to_delete)
        db.session.commit()
        return redirect(location=url_for(endpoint='precipitation_dashboard_station_management'))
    except:
        return "اوپسس ..."
    


# @app.route('/isotope_analysis')
# @login_required
# def isotope_analysis_route():
#     return app.index()

@app.route('/hydrograph')
@login_required
def hydrograph_route():
    return app.index()


@app.route('/chemograph')
@login_required
def chemograph_route():
    return app.index()
