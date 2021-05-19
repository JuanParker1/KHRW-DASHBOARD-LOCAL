import os
import pandas as pd
import sqlite3
from werkzeug.utils import secure_filename

from flask import render_template, redirect, url_for, flash, request
from App import app, db, bcrypt


from App.forms import RegistrationForm, LoginForm, UpdateProfileForm, UserManagementForm, StationForm, UpdateStationForm
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


# -----------------------------------------------------------------------------
# ADD STATION MANUALY
# -----------------------------------------------------------------------------
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
            startYear = int(form.startYear.data),
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


# -----------------------------------------------------------------------------
# UPDATE STATION MANUALY
# -----------------------------------------------------------------------------
@app.route('/precipitation/dashboard/station_managment/<int:stationCode>/update', methods=['GET', 'POST'])
@login_required
def precipitation_dashboard_station_managment_update(stationCode):
    station = Station.query.get_or_404(stationCode)    
    form = UpdateStationForm()
    if form.validate_on_submit():
        station.stationName = form.stationName.data
        station.stationCode = form.stationCode.data
        station.stationOldCode = form.stationOldCode.data
        station.drainageArea6 = form.drainageArea6.data
        station.drainageArea30 = form.drainageArea30.data
        station.areaStudyName = form.areaStudyName.data
        station.omor = form.omor.data
        station.county = form.county.data
        station.startYear = form.startYear.data
        station.longDecimalDegrees = form.longDecimalDegrees.data
        station.latDecimalDegrees = form.latDecimalDegrees.data
        station.elevation = form.elevation.data
        db.session.commit()
        flash(message=f"ایستگاه با کد {station.stationCode} به روز رسانی شد.", category='success')
        return redirect(url_for('precipitation_dashboard_station_management'))
    elif request.method == 'GET':
        form.stationName.data = station.stationName
        form.stationCode.data = station.stationCode
        form.stationOldCode.data = station.stationOldCode
        form.drainageArea6.data = station.drainageArea6
        form.drainageArea30.data = station.drainageArea30
        form.areaStudyName.data = station.areaStudyName
        form.omor.data = station.omor
        form.county.data = station.county
        form.startYear.data = station.startYear
        form.longDecimalDegrees.data = station.longDecimalDegrees
        form.latDecimalDegrees.data = station.latDecimalDegrees
        form.elevation.data = station.elevation
    return render_template(
            template_name_or_list='precipitation_flask/update_station.html',
            form=form
    )



# -----------------------------------------------------------------------------
# ADD STATION - IMPORT CSV
# -----------------------------------------------------------------------------
@app.route('/precipitation/dashboard/add_station_csv', methods=['POST', 'GET'])
@login_required
def precipitation_dashboard_add_station_csv():
    if request.method == "POST":
        # SAVE FILE
        try:
            file = request.files['file']
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
        except:
            flash(message=f"یک فایل انتخاب کنید", category='danger')
            return redirect(url_for('precipitation_dashboard_add_station_csv'))


        # CONECT TO DATABASE
        try:
            db_path = 'App/dashApp/precipitation/precipitation.sqlite'
            db_new = sqlite3.connect(db_path, check_same_thread=False)
            exist_station_data = pd.read_sql_query(sql="SELECT * FROM station", con=db_new)
            exist_station_data_columns = list(exist_station_data.columns)
            stationCode_exist = exist_station_data["stationCode"].unique()
        except:
            flash(message=f"مشکل در بارگذاری دیتابیس", category='danger')
            return redirect(url_for('precipitation_dashboard_add_station_csv'))

        
        # READ CSV FILE
        try:
            import_station_data = pd.read_csv(file_path)
            import_station_data_columns = list(import_station_data.columns)
            stationCode_import = import_station_data["stationCode"].unique()
        except:
            flash(message=f"فرمت فایل وارد شده صحیح نمی‌باشد، فرمت مجاز csv می‌باشد", category='danger')
            return redirect(url_for('precipitation_dashboard_add_station_csv'))


        # CHECK COLUMNS
        if not (exist_station_data_columns == import_station_data_columns):
            flash(message=f"ستون‌های فایل ورودی با ستون‌های دیتابیس مطابقت ندارد!", category='danger')
            return redirect(url_for('precipitation_dashboard_add_station_csv'))


        # CHECK EMPTY CSV
        if len(import_station_data) == 0:
            flash(message=f"فایل ورودی خالی می‌باشد!", category='danger')
            return redirect(url_for('precipitation_dashboard_add_station_csv'))
        

        # CHECK NONE VALUE IN CSV
        if import_station_data.iloc[:,:].isna().any().any():
            flash(message=f"فایل ورودی چک گردد. فایل دارای سلول‌های خالی می‌باشد!", category='danger')
            return redirect(url_for('precipitation_dashboard_add_station_csv'))
        

        # CHECK DUPLICATE STATIONCODE IN CSV
        if import_station_data.stationCode.duplicated().any():
            flash(message=f"در فایل ورودی ایستگاه‌هایی با کد مشابه وجود دارد!", category='danger')
            return redirect(url_for('precipitation_dashboard_add_station_csv'))


        # CHECK DUPLICATE STATIONCODE IN DATABASE AND CSV
        if len(list(set(stationCode_exist).intersection(stationCode_import))) == 0:
            import_station_data.to_sql(name="station", con=db_new, if_exists="append", index=False)
            flash(message=f"ایستگاه‌های انتخابی با موفقیت به دیتابیس اضافه گردید.", category='success')
            return redirect(url_for('precipitation_dashboard_station_management'))
        else:
            stationCode_duplicate = list(set(stationCode_exist).intersection(stationCode_import))
            import_station_data = import_station_data[import_station_data['stationCode'].isin(stationCode_duplicate) == False]
            if len(import_station_data) != 0:
                import_station_data.to_sql(name="station", con=db_new, if_exists="append", index=False)
                flash(message=f"ایستگاه‌های انتخابی با موفقیت به دیتابیس اضافه گردید و ایستگاه‌ها با کد { stationCode_duplicate } به دلیل موجود بودن در دیتابس از فایل ورودی حذف گردید.", category='success')
                return redirect(url_for('precipitation_dashboard_station_management'))
            else:
                flash(message=f"همه ایستگاه‌های ورودی در دیتابیس موجود می‌باشند!", category='info')
                return redirect(url_for('precipitation_dashboard_station_management'))
    
    
    return render_template(
        template_name_or_list='precipitation_flask/add_station_csv.html'
    )






# -----------------------------------------------------------------------------
# DELETE STATION
# -----------------------------------------------------------------------------
@app.route('/precipitation/dashboard/station_managment/<int:stationCode>/delete', methods=['GET', 'POST'])
@login_required
def precipitation_dashboard_station_managment_delete(stationCode):
    station = Station.query.get_or_404(stationCode)    
    try:
        db.session.delete(station)
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
