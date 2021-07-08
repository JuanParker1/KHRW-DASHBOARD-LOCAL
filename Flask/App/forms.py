import itertools
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, FloatField, SelectField, SubmitField, FormField, FieldList, DateTimeField, DateField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from App.models import User, Station
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




info = pd.read_csv("App/dashApps/precipitation/assets/database/Info.csv")
info_khorasan_razavi = info[info["OstanMotevali"] == "خراسان رضوی"]

Hoze6Name = list(info_khorasan_razavi["Hoze6Name"].unique())
Hoze6Name.append(" ")

Hoze30Name = list(info_khorasan_razavi["Hoze30Name"].unique())
Hoze30Name.append(" ")

MahdodehName = list(info_khorasan_razavi["MahdodehName"].unique())
MahdodehName.append(" ")

Shahrestan = [
    'باخرز',
    'بجستان',
    'بردسکن',
    'بینالود',
    'تایباد',
    'تربت جام',
    'تربت حیدریه',
    'جغتای',
    'جوین',
    'چناران',
    'خلیل آباد',
    'خواف',
    'خوشاب',
    'داورزن',
    'درگز',
    'رشتخوار',
    'زاوه',
    'زبرخان',
    'سبزوار',
    'سرخس',
    'ششتمد',
    'صالح آباد',
    'فریمان',
    'فیروزه',
    'قوچان',
    'کاشمر',
    'کلات',
    'کوهسرخ',
    'گلبهار',
    'گناباد',
    'مشهد',
    'مه ولات',
    'نیشابور'
]
Shahrestan.append(" ")

startYear = [str(y) for y in list(range(1330, 1426))]
startYear.append(" ")


class StationForm(FlaskForm):
    
    stationName = StringField(
        label="نام ایستگاه",
        validators=[
            DataRequired(message="وارد کردن نام ایستگاه ضروری میباشد."),
        ]
    )
    
    stationCode = IntegerField(
        label="کد ایستگاه",
        validators=[
            DataRequired(message="وارد کردن کد ایستگاه ضروری میباشد.")
        ]
    )
    
    stationOldCode = StringField(
        label="کد قدیمی ایستگاه"
    )
    
    drainageArea6 = SelectField(
        label="حوضه آبریز شش‌گانه (درجه 1)",
        choices=sorted(Hoze6Name),
    )
    
    drainageArea30 = SelectField(
        label="حوضه آبریز سی‌گانه (درجه 2)",
        choices=sorted(Hoze30Name),
    )
    
    areaStudyName = SelectField(
        label="محدوده مطالعاتی",
        choices=sorted(MahdodehName),
    )
    
    areaStudyCode = IntegerField(
        label="کد محدوده مطالعاتی",
        validators=[
            DataRequired(message="وارد کردن کد محدوده مطالعلتی ضروری میباشد.")
        ]
    )
    
    omor = StringField(
        label="امور",
        validators=[
            DataRequired(message="وارد کردن امور ضروری میباشد.")
        ]
    )
    
    county = SelectField(
        label="شهرستان",
        choices=sorted(Shahrestan),
    )
    
    startYear = SelectField(
        label="سال تاسیس",
        choices=sorted(startYear),
    )
    
    longDecimalDegrees = FloatField(
        label="طول جغرافیایی (بر حسب صدم اعشار)",
        validators=[
            DataRequired(message="وارد کردن طول جغرافیای بر حسب صدم اعشار ضروری میباشد."),
        ]
    )
    
    latDecimalDegrees = FloatField(
        label="عرض جغرافیایی (بر حسب صدم اعشار)",
        validators=[
            DataRequired(message="وارد کردن عرض جغرافیای بر حسب صدم ضروری میباشد."),
        ]
    )
    
    elevation = FloatField(
        label="ارتفاع (بر حسب متر)",
        validators=[
            DataRequired(message="وارد کردن ارتفاع ضروری میباشد."),
        ]
    )
    
    submit = SubmitField(label='ثبت ایستگاه جدید')
   
    def validate_drainageArea6(self, drainageArea6):
        if drainageArea6.data == " ":
            raise ValidationError(message="انتخاب حوضه آبریز شش‌گانه الزامی می‌باشد.")
        
    def validate_drainageArea30(self, drainageArea30):
        if drainageArea30.data == " ":
            raise ValidationError(message="انتخاب حوضه آبریز سی‌گانه الزامی می‌باشد.")
        
    def validate_areaStudyName(self, areaStudyName):
        if areaStudyName.data == " ":
            raise ValidationError(message="انتخاب محدوده مطالعاتی الزامی می‌باشد.")
        
    def validate_county(self, county):
        if county.data == " ":
            raise ValidationError(message="انتخاب شهرستان الزامی می‌باشد.")
        
    def validate_startYear(self, startYear):
        if startYear.data == " ":
            raise ValidationError(message="انتخاب سال تاسیس الزامی می‌باشد.")
        
    def validate_longDecimalDegrees(self, longDecimalDegrees):
        if longDecimalDegrees.data > 64.00 or longDecimalDegrees.data < 44.00:
            raise ValidationError(message="طول جغرافیای باید بین 44 تا 64 درجه عرض شمالی باشد.")
        
    def validate_latDecimalDegrees(self, latDecimalDegrees):
        if latDecimalDegrees.data > 40.00 or latDecimalDegrees.data < 25.00:
            raise ValidationError(message="عرض جغرافیای باید بین 25 تا 40 درجه طول شرقی باشد.")
 
    def validate_stationCode(self, stationCode):
        stCode = Station.query.filter_by(stationCode=stationCode.data).first()
        if stCode:
            raise ValidationError(message="این کد ایستگاه موجود میباشد.")


class UpdateStationForm(FlaskForm):
    
    stationName = StringField(
        label="نام ایستگاه",
        validators=[
            DataRequired(message="وارد کردن نام ایستگاه ضروری میباشد."),
        ]
    )
    
    stationCode = IntegerField(
        label="کد ایستگاه",
        validators=[
            DataRequired(message="وارد کردن کد ایستگاه ضروری میباشد.")
        ]
    )
    
    stationOldCode = StringField(
        label="کد قدیمی ایستگاه"
    )
    
    drainageArea6 = SelectField(
        label="حوضه آبریز شش‌گانه (درجه 1)",
        choices=sorted(Hoze6Name),
    )
    
    drainageArea30 = SelectField(
        label="حوضه آبریز سی‌گانه (درجه 2)",
        choices=sorted(Hoze30Name),
    )
    
    areaStudyName = SelectField(
        label="محدوده مطالعاتی",
        choices=sorted(MahdodehName),
    )
    
    areaStudyCode = IntegerField(
        label="کد محدوده مطالعاتی",
        validators=[
            DataRequired(message="وارد کردن کد محدوده مطالعلتی ضروری میباشد.")
        ]
    )
    
    omor = StringField(
        label="امور",
        validators=[
            DataRequired(message="وارد کردن امور ضروری میباشد.")
        ]
    )
    
    county = SelectField(
        label="شهرستان",
        choices=sorted(Shahrestan),
    )
    
    startYear = SelectField(
        label="سال تاسیس",
        choices=sorted(startYear),
    )
    
    longDecimalDegrees = FloatField(
        label="طول جغرافیایی (بر حسب صدم اعشار)",
        validators=[
            DataRequired(message="وارد کردن طول جغرافیای بر حسب صدم اعشار ضروری میباشد."),
        ]
    )
    
    latDecimalDegrees = FloatField(
        label="عرض جغرافیایی (بر حسب صدم اعشار)",
        validators=[
            DataRequired(message="وارد کردن عرض جغرافیای بر حسب صدم ضروری میباشد."),
        ]
    )
    
    elevation = FloatField(
        label="ارتفاع (بر حسب متر)",
        validators=[
            DataRequired(message="وارد کردن ارتفاع ضروری میباشد."),
        ]
    )
    
    submit = SubmitField(label='به روز رسانی ایستگاه')
        

    def validate_drainageArea6(self, drainageArea6):
        if drainageArea6.data == " ":
            raise ValidationError(message="انتخاب حوضه آبریز شش‌گانه الزامی می‌باشد.")
        
    def validate_drainageArea30(self, drainageArea30):
        if drainageArea30.data == " ":
            raise ValidationError(message="انتخاب حوضه آبریز سی‌گانه الزامی می‌باشد.")
        
    def validate_areaStudyName(self, areaStudyName):
        if areaStudyName.data == " ":
            raise ValidationError(message="انتخاب محدوده مطالعاتی الزامی می‌باشد.")
        
    def validate_county(self, county):
        if county.data == " ":
            raise ValidationError(message="انتخاب شهرستان الزامی می‌باشد.")
        
    def validate_startYear(self, startYear):
        if startYear.data == " ":
            raise ValidationError(message="انتخاب سال تاسیس الزامی می‌باشد.")
        
    def validate_longDecimalDegrees(self, longDecimalDegrees):
        if longDecimalDegrees.data > 64.00 or longDecimalDegrees.data < 44.00:
            raise ValidationError(message="طول جغرافیای باید بین 44 تا 64 درجه عرض شمالی باشد.")
        
    def validate_latDecimalDegrees(self, latDecimalDegrees):
        if latDecimalDegrees.data > 40.00 or latDecimalDegrees.data < 25.00:
            raise ValidationError(message="عرض جغرافیای باید بین 25 تا 40 درجه طول شرقی باشد.")
 
    def validate_stationCode(self, stationCode):
        stCode = Station.query.filter_by(stationCode=stationCode.data).first()
        if stCode:
            raise ValidationError(message="این کد ایستگاه موجود میباشد.")


class AddPrecipitationDataForm(FlaskForm):

    class Meta:
        csrf = False

    st_name = Station.query.order_by(Station.stationName).with_entities(Station.stationName).all()

    stationName = SelectField(
        label="نام ایستگاه",
        choices=sorted([" "] + [st[0] for st in st_name]),
        validators=[
            DataRequired(message="انتخاب نام ایستگاه الزامی می‌باشد.")
        ]
    )

    baran = FloatField(
        label="باران (میلیمتر)",
        default=0
    )

    barf = FloatField(
        label="برف (میلیمتر)",
        default=0
    )

    ab_barf = FloatField(
        label="آب برف (میلیمتر)",
        default=0
    )



class NumberStationAdd(FlaskForm):
    numberStation = IntegerField(
        label="تعداد ایستگاه مورد نظر",
        default=3,
        validators=[
            DataRequired(message="وارد کردن تعداد ایستگاه الزامی می‌باشد.")
        ]
    )
    
    submit = SubmitField(
        label='اضافه کردن'
    )


class PrecipitationDataForm(FlaskForm):
    time = SelectField(
        label="زمان", 
        choices=[" ", "06:30:00", "18:30:00"],
        validators=[
            DataRequired(message="انتخاب زمان الزامی می‌باشد.")
        ]
    )

    date = StringField(
        label="تاریخ",
        validators=[
            DataRequired(message="انتخاب تاریخ الزامی می‌باشد.")
        ]
    )

    addPrecipData = FieldList(
        FormField(AddPrecipitationDataForm),
        validators=[
            DataRequired()
        ]
    )

    # submit = SubmitField(
    #     label='اضافه کردن داده‌های بارندگی'
    # )