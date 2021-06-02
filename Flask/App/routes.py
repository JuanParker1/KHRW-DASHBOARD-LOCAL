from itertools import zip_longest
import os
from flask_wtf.recaptcha import validators
import pandas as pd
import sqlite3
from werkzeug.utils import secure_filename
from wtforms.validators import DataRequired
from wtforms import FormField, FieldList
from flask import render_template, redirect, url_for, flash, request
from App import app, db, bcrypt
from flask import send_file

from App.forms import AddPrecipitationDataForm

# from flask_googlemaps import GoogleMaps
# from flask_googlemaps import Map
import folium 
import altair as alt

from App.data_cleansing import *


from App.forms import RegistrationForm, LoginForm, UpdateProfileForm, UserManagementForm, StationForm, UpdateStationForm, PrecipitationDataForm, AddPrecipitationDataForm, NumberStationAdd
from App.models import User, Station, Precipitation
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




@app.route('/precipitation/dashboard/station_managment', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/precipitation/dashboard/station_managment/<int:page>', methods=['GET', 'POST'])
@login_required
def precipitation_dashboard_station_management(page):
    page = page
    pages = 10
    stations = Station.query.order_by(Station.stationCode.asc()).paginate(page, pages, error_out=False)
    if request.method == 'POST' and 'tag' in request.form and request.form["tag"] != "":
        pages = 100
        tag = request.form["tag"]
        search = "%{}%".format(tag)
        stations = Station.query.filter(Station.stationName.like(search) | Station.stationCode.like(search) | Station.areaStudyName.like(search)).paginate(per_page=pages, error_out=False)  
        return render_template('precipitation_flask/station_managment.html', stations=stations, tag=tag)       
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
            areaStudyCode = form.areaStudyCode.data,
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
        station.areaStudyCode = form.areaStudyCode.data
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
        form.areaStudyCode.data = station.areaStudyCode
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
    



# -----------------------------------------------------------------------------
# ADD PRECIPITATION DATA - IMPORT CSV
# -----------------------------------------------------------------------------
@app.route('/precipitation/dashboard/add_precipitation_data_csv', methods=['POST', 'GET'])
@login_required
def precipitation_dashboard_add_precipitation_data_csv():
    if request.method == "POST":
        # SAVE FILE
        try:
            file = request.files['file']
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
        except:
            flash(message=f"یک فایل انتخاب کنید", category='danger')
            return redirect(url_for('precipitation_dashboard_add_precipitation_data_csv'))


        # CONECT TO DATABASE
        try:
            db_path = 'App/dashApp/precipitation/precipitation.sqlite'
            db_new = sqlite3.connect(db_path, check_same_thread=False)
            exist_precipitation_data = pd.read_sql_query(sql="SELECT * FROM precipitation", con=db_new)
            exist_precipitation_data_columns = list(exist_precipitation_data.columns)
            exist_precipitation_data['DATE'] = exist_precipitation_data['YEAR'].astype(str) + "-" + exist_precipitation_data['MONTH'].astype(str).str.zfill(2) + "-" + exist_precipitation_data['DAY'].astype(str).str.zfill(2) + " " + exist_precipitation_data['HOURE'].astype(str).str.zfill(2) + ":" + exist_precipitation_data['MINUTE'].astype(str).str.zfill(2) + ":" + exist_precipitation_data['SECOND'].astype(str).str.zfill(2)
            exist_precipitation_data["uniqueCode"] = exist_precipitation_data["stationCode"].astype(str) + "-" + exist_precipitation_data["DATE"]
        except:
            flash(message=f"مشکل در بارگذاری دیتابیس", category='danger')
            return redirect(url_for('precipitation_dashboard_add_precipitation_data_csv'))

        
        # READ CSV FILE
        try:
            import_precipitation_data = pd.read_csv(file_path)
            import_precipitation_data_columns = list(import_precipitation_data.columns)
            import_precipitation_data['DATE'] = import_precipitation_data['YEAR'].astype(str) + "-" + import_precipitation_data['MONTH'].astype(str).str.zfill(2) + "-" + import_precipitation_data['DAY'].astype(str).str.zfill(2) + " " + import_precipitation_data['HOURE'].astype(str).str.zfill(2) + ":" + import_precipitation_data['MINUTE'].astype(str).str.zfill(2) + ":" + import_precipitation_data['SECOND'].astype(str).str.zfill(2)
            import_precipitation_data["uniqueCode"] = import_precipitation_data["stationCode"].astype(str) + "-" + import_precipitation_data["DATE"]
            import_precipitation_data.drop_duplicates(inplace=True)
            import_precipitation_data.reset_index(inplace=True, drop=True)
        except:
            flash(message=f"فرمت فایل وارد شده صحیح نمی‌باشد، فرمت مجاز csv می‌باشد", category='danger')
            return redirect(url_for('precipitation_dashboard_add_precipitation_data_csv'))


        # CHECK COLUMNS
        if not (exist_precipitation_data_columns[1:] == import_precipitation_data_columns):
            flash(message=f"ستون‌های فایل ورودی با ستون‌های دیتابیس مطابقت ندارد!", category='danger')
            return redirect(url_for('precipitation_dashboard_add_precipitation_data_csv'))


        # CHECK EMPTY CSV
        if len(import_precipitation_data) == 0:
            flash(message=f"فایل ورودی خالی می‌باشد!", category='danger')
            return redirect(url_for('precipitation_dashboard_add_precipitation_data_csv'))
        

        # # CHECK NONE VALUE IN CSV
        # if import_precipitation_data.iloc[:, 0:8].isna().any().any():
        #     flash(message=f"فایل ورودی چک گردد. فایل دارای سلول‌های خالی می‌باشد!", category='danger')
        #     return redirect(url_for('precipitation_dashboard_add_precipitation_data_csv'))
        

        # CHECK DUPLICATE DATE IN CSV
        for st in import_precipitation_data.stationCode.unique():
            df = import_precipitation_data[import_precipitation_data['stationCode'] == st] 
            if df.DATE.duplicated().any():
                flash(message=f"در فایل ورودی برای ایستگاه {st} رکورد تکراری وجود دارد!", category='warning')                
                # return redirect(url_for('precipitation_dashboard_add_precipitation_data_csv'))
        import_precipitation_data = import_precipitation_data.drop_duplicates(subset=['uniqueCode'], keep='last')

        
        # CHECK DUPLICATE STATIONCODE IN DATABASE AND CSV
        if len(list(set(exist_precipitation_data['uniqueCode'].tolist()).intersection(import_precipitation_data['uniqueCode'].tolist()))) == 0:
            import_precipitation_data = import_precipitation_data.drop('uniqueCode', axis=1)
            import_precipitation_data = import_precipitation_data.drop('DATE', axis=1)
            import_precipitation_data.to_sql(name="precipitation", con=db_new, if_exists="append", index=False)
            flash(message=f"داده‌های بارندگی با موفقیت به دیتابیس اضافه گردید.", category='success')
            return redirect(url_for('precipitation_dashboard_precipitation_data_management'))
        else:
            data_duplicate = list(set(exist_precipitation_data['uniqueCode'].tolist()).intersection(import_precipitation_data['uniqueCode'].tolist()))
            import_precipitation_data = import_precipitation_data[import_precipitation_data['uniqueCode'].isin(data_duplicate) == False]
            if len(import_precipitation_data) != 0:
                import_precipitation_data = import_precipitation_data.drop('uniqueCode', axis=1)
                import_precipitation_data = import_precipitation_data.drop('DATE', axis=1)
                import_precipitation_data.to_sql(name="precipitation", con=db_new, if_exists="append", index=False)
                flash(message=f"داده‌های بارندگی با موفقیت به دیتابیس اضافه گردید و ورودی‌های با کد { data_duplicate } به دلیل موجود بودن در دیتابس از فایل ورودی حذف گردید.", category='success')
                return redirect(url_for('precipitation_dashboard_precipitation_data_management'))
            else:
                flash(message=f"همه داده‌های بارندگی ورودی در دیتابیس موجود می‌باشند!", category='info')
                return redirect(url_for('precipitation_dashboard_add_precipitation_data_csv'))
             
    return render_template(
        template_name_or_list='precipitation_flask/add_precipitation_data_csv.html'
    )


@app.route('/precipitation/dashboard/precipitation_data_managment', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/precipitation/dashboard/precipitation_data_managment/<int:page>', methods=['GET', 'POST'])
@login_required
def precipitation_dashboard_precipitation_data_management(page):
    page = page
    pages = 25
    data = Precipitation.query.order_by(Precipitation.stationCode.asc()).paginate(page, pages, error_out=False)
    if request.method == 'POST' and 'tag-code' in request.form and request.form["tag-code"] != "":
        pages = 100
        tag = request.form["tag-code"]
        search = "%{}%".format(tag)
        data = Precipitation.query.filter(Precipitation.stationCode.like(search)).paginate(per_page=pages, error_out=False)  
        return render_template('precipitation_flask/precipitation_data_management.html', data=data, tag=tag)       
    return render_template(template_name_or_list='precipitation_flask/precipitation_data_management.html', data=data)



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




@app.route('/precipitation/dashboard/add_precipitation_data', methods=['GET', 'POST'])
@login_required
def precipitation_dashboard_add_precipitation_data():
    form = PrecipitationDataForm()
    form2 = NumberStationAdd()
    print(request.form)
    if "form-numberStation" in request.form:
        
        if request.form["tag"][0:] == '':
            return render_template(
                template_name_or_list='precipitation_flask/add_precipitation_data.html',
                form=form
            )            

        for i in range(int(request.form["tag"][0:])):
            form.addPrecipData.append_entry()
        
        return render_template(
            template_name_or_list='precipitation_flask/add_precipitation_data.html',
            form=form
        )
    
    
    if "form-addPrecipData" in request.form and form.validate_on_submit():
        db_precipitation = sqlite3.connect(db_path_precipitation, check_same_thread=False)       
        exist_precipitation_data = pd.read_sql_query(sql="SELECT * FROM precipitation", con=db_precipitation)
        exist_precipitation_data_columns = list(exist_precipitation_data.columns)
        exist_precipitation_data['DATE'] = exist_precipitation_data['YEAR'].astype(str) + "-" + exist_precipitation_data['MONTH'].astype(str).str.zfill(2) + "-" + exist_precipitation_data['DAY'].astype(str).str.zfill(2) + " " + exist_precipitation_data['HOURE'].astype(str).str.zfill(2) + ":" + exist_precipitation_data['MINUTE'].astype(str).str.zfill(2) + ":" + exist_precipitation_data['SECOND'].astype(str).str.zfill(2)
        exist_precipitation_data["uniqueCode"] = exist_precipitation_data["stationCode"].astype(str) + "-" + exist_precipitation_data["DATE"]
        exist_station = pd.read_sql_query(sql="SELECT * FROM station", con=db_precipitation)
        
        df = pd.DataFrame(columns=exist_precipitation_data_columns[1:] + ["stationName"])

        date = form.date.data.split("/")
        time = form.time.data.split(":")
        data = form.addPrecipData.data

        for i in range(len(data)):
            df.loc[i,"stationCode"] = exist_station[exist_station['stationName'] == data[i]["stationName"]].iloc[0,1]
            df.loc[i,"YEAR"] = date[0]
            df.loc[i,"MONTH"] = date[1].zfill(2)
            df.loc[i,"DAY"] = date[2].zfill(2)
            df.loc[i,"HOURE"] = time[0].zfill(2)
            df.loc[i,"MINUTE"] = time[1].zfill(2)
            df.loc[i,"SECOND"] = time[2].zfill(2)
            df.loc[i,"BARAN"] = data[i]["baran"]
            df.loc[i,"BARF"] = data[i]["barf"]
            df.loc[i,"AB_BARF"] = data[i]["ab_barf"]
            df.loc[i,"JAM_BARAN"] = data[i]["baran"] + data[i]["ab_barf"]
            df.loc[i,"stationName"] = data[i]["stationName"]

        df['DATE'] = df['YEAR'].astype(str) + "-" + df['MONTH'].astype(str) + "-" + df['DAY'].astype(str) + " " + df['HOURE'].astype(str) + ":" + df['MINUTE'].astype(str) + ":" + df['SECOND'].astype(str)

        df["uniqueCode"] = df["stationCode"].astype(str) + "-" + df["DATE"]
        
        
        # DUPLICATE STATION ENTER
        if df.duplicated(subset=["stationName"]).any():
            st_duplicate_enter = df.loc[df.duplicated(subset=["stationName"]),:]["stationName"].unique().tolist()
            flash(message=f"ایستگاه‌های {st_duplicate_enter} تکراری وارد شده‌اند.", category='warning')
            return render_template(
                template_name_or_list='precipitation_flask/add_precipitation_data.html',
                form=form
            )
        
        
        # DUPLICATE STATION-DATE WITH DATABASE
        if df["uniqueCode"].isin(exist_precipitation_data["uniqueCode"]).any():
            st_date_duplicate = df.loc[df["uniqueCode"].isin(exist_precipitation_data["uniqueCode"]), :]
            st_date_duplicate['ERROR'] = st_date_duplicate['stationName'] + ': ' + st_date_duplicate['DATE']
            st_date_duplicate = st_date_duplicate['ERROR'].unique().tolist()
            flash(message=f"ایستگاه‌ها و تاریخ‌های {st_date_duplicate} در دیتابیس موجود می‌باشند.", category='warning')
            return render_template(
                template_name_or_list='precipitation_flask/add_precipitation_data.html',
                form=form
            )
        
        df = df.drop(['uniqueCode', 'DATE', 'stationName'], axis=1)
        df["stationCode"] = df["stationCode"].astype(int)
        df["YEAR"] = df["YEAR"].astype(int)
        df["MONTH"] = df["MONTH"].astype(int)
        df["DAY"] = df["DAY"].astype(int)
        df["HOURE"] = df["HOURE"].astype(int)
        df["MINUTE"] = df["MINUTE"].astype(int)
        df["SECOND"] = df["SECOND"].astype(int)
        df["BARAN"] = df["BARAN"].astype(float)
        df["BARF"] = df["BARF"].astype(float)
        df["AB_BARF"] = df["AB_BARF"].astype(float)
        df["JAM_BARAN"] = df["JAM_BARAN"].astype(float)
        df.to_sql(name="precipitation", con=db_precipitation, if_exists="append", index=False)
        
        flash(message=f"داده‌های بارندگی با موفقیت به دیتابیس اضافه گردید!", category='success')
        return redirect(url_for('precipitation_dashboard_precipitation_data_management'))
    print(300)
    return render_template(
        template_name_or_list='precipitation_flask/add_precipitation_data.html',
        form=form
    )


@app.route('/precipitation/dashboard')
@login_required
def precipitation_dashboard():  
    
    try:
        db_precipitation = sqlite3.connect(db_path_precipitation, check_same_thread=False)
        db_precipitation_precip_data = pd.read_sql_query(sql="SELECT * FROM precipitation", con=db_precipitation)
        db_precipitation_stations = pd.read_sql_query(sql="SELECT * FROM station", con=db_precipitation)
        
        db_precipitation_precip_data["wateryear"] = [extract_wateryear(month, year) for month, year in zip(db_precipitation_precip_data["MONTH"], db_precipitation_precip_data["YEAR"])]
        data = db_precipitation_precip_data
        data_water_year_baran = data[['stationCode', 'wateryear', 'JAM_BARAN']].groupby(['stationCode', 'wateryear']).sum().reset_index()
        
    except:
        print("ERROR LOAD DATA FROM DATABASE")

    map = folium.Map(
        location=[db_precipitation_stations["latDecimalDegrees"].mean(), db_precipitation_stations["longDecimalDegrees"].mean()],
        tiles='Stamen Terrain',
        zoom_start=7
    )
    
    
    for i in range(len(db_precipitation_stations)):       
        
        
        data_st = data_water_year_baran[data_water_year_baran["stationCode"] == db_precipitation_stations.stationCode[i]]
        
        # create an altair chart, then convert to JSON
        bar = alt.Chart(data_st, width=600).mark_bar().encode(
            x=alt.X('wateryear:O', axis=alt.Axis(title='سال آبی')),
            y=alt.Y('JAM_BARAN:Q', axis=alt.Axis(title='بارندگی - میلیمتر'))
        )
        
        
        rule = alt.Chart(data_st).mark_rule(color='red').encode(
            y='mean(JAM_BARAN):Q'
        )
        
        chart = (bar + rule).properties(title=db_precipitation_stations.stationName[i]).configure_axisY(
            labelFontSize=16,
            labelFont="B Zar",
            titleFont="B Zar",
            titleFontSize=16
        ).configure_axisX(
            labelFontSize=16,
            labelFont="B Zar",
            titleFont="B Zar",
            titleFontSize=16
        ).configure_title(
            fontSize=20,
            font="B Titr",
        )
        
        chart.configure_title(
            align="left"
        )
        
        vis = chart.to_json()                

        folium.Marker(
            location=[db_precipitation_stations["latDecimalDegrees"][i], db_precipitation_stations["longDecimalDegrees"][i]],
            popup=folium.Popup(max_width=700).add_child(folium.features.VegaLite(vis, width=700, height=300)),
            tooltip="کلیک کنید"
        ).add_to(map)

    return render_template(
        template_name_or_list='precipitation_flask/precipitation_dashboard.html',
        map=map._repr_html_()
    )
    
@app.route('/downloadSampleDataFile')
def downloadSampleDataFile ():
    path = "dashApp/precipitation/assets/database/data.csv"
    return send_file(path, as_attachment=True)

@app.route('/downloadSampleStationFile')
def downloadSampleStationFile ():
    path = "dashApp/precipitation/assets/database/station.csv"
    return send_file(path, as_attachment=True)