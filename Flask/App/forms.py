from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from App.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    firstname = StringField(label='First Name',
                            validators=[DataRequired(message="وارد کردن نام ضروری میباشد."), Length(min=2, max=30, message="طول نام باید بین 2 تا 30 کارکتر باشد.")])
    lastname = StringField(label='Last Name',
                           validators=[DataRequired(message="وارد کردن نام خانوادگی ضروری میباشد."), Length(min=2, max=30, message="طول نام خانوادگی باید بین 2 تا 30 کارکتر باشد.")])
    username = StringField(label='Username',
                           validators=[DataRequired(message="وارد کردن نام کاربری ضروری میباشد."), Length(min=4, max=30, message="طول نام کاربری باید بین 8 تا 30 کارکتر باشد.")])
    email = StringField(label='Email',
                        validators=[DataRequired(message="وارد کردن ایمیل ضروری میباشد."), Email(message="ایمیل وارد شده صحیح نمیباشد.")])
    password = PasswordField(label='Password',
                             validators=[DataRequired(message="وارد کردن رمز عبور ضروری میباشد.")])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(message="این نام کاربری موجود میباشد.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(message="این ایمیل موجود میباشد.")


class LoginForm(FlaskForm):
    username = StringField(label='Username',
                           validators=[DataRequired(message="وارد کردن نام کاربری ضروری میباشد."), Length(min=8, max=30, message="طول نام کاربری باید بین 8 تا 30 کارکتر باشد.")])
    password = PasswordField(label='Password',
                             validators=[DataRequired(message="وارد کردن رمز عبور ضروری میباشد.")])
    remember = BooleanField(label='Remember Me')


class UpdateProfileForm(FlaskForm):
    firstname = StringField(label='First Name',
                            validators=[DataRequired(message="وارد کردن نام ضروری میباشد."), Length(min=2, max=30, message="طول نام باید بین 2 تا 30 کارکتر باشد.")])
    lastname = StringField(label='Last Name',
                           validators=[DataRequired(message="وارد کردن نام خانوادگی ضروری میباشد."), Length(min=2, max=30, message="طول نام خانوادگی باید بین 2 تا 30 کارکتر باشد.")])
    username = StringField(label='Username',
                           validators=[DataRequired(message="وارد کردن نام کاربری ضروری میباشد."), Length(min=4, max=30, message="طول نام کاربری باید بین 8 تا 30 کارکتر باشد.")])
    email = StringField(label='Email',
                        validators=[DataRequired(message="وارد کردن ایمیل ضروری میباشد."), Email(message="ایمیل وارد شده صحیح نمیباشد.")])
    password = PasswordField(label='Password',
                             validators=[DataRequired(message="وارد کردن رمز عبور ضروری میباشد.")])

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(message="این نام کاربری موجود میباشد.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(message="این ایمیل موجود میباشد.")


class UserManagementForm(FlaskForm):
    firstname = StringField(label='First Name',
                            validators=[DataRequired(message="وارد کردن نام ضروری میباشد."), Length(min=2, max=30, message="طول نام باید بین 2 تا 30 کارکتر باشد.")])
    lastname = StringField(label='Last Name',
                           validators=[DataRequired(message="وارد کردن نام خانوادگی ضروری میباشد."), Length(min=2, max=30, message="طول نام خانوادگی باید بین 2 تا 30 کارکتر باشد.")])
    username = StringField(label='Username',
                           validators=[DataRequired(message="وارد کردن نام کاربری ضروری میباشد."), Length(min=4, max=30, message="طول نام کاربری باید بین 8 تا 30 کارکتر باشد.")])
    email = StringField(label='Email',
                        validators=[DataRequired(message="وارد کردن ایمیل ضروری میباشد."), Email(message="ایمیل وارد شده صحیح نمیباشد.")])