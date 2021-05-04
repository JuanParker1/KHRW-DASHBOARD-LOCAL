from flask import render_template, redirect, url_for, flash, request
from App import app, db, bcrypt

from App.forms import RegistrationForm, LoginForm, UpdateProfileForm
from App.models import User
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


@app.route('/dashApp1')
@login_required
def dashApp1():
    return app.index()


@app.route('/dashApp2')
@login_required
def dashApp2():
    return app.index()


@app.route('/myAppAQ')
def myAppAQ():
    return app.server()
