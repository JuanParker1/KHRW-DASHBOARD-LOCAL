from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from flask_googlemaps import GoogleMaps
# from flask_bootstrap import Bootstrap
# from flask_datepicker import datepicker

# from App.dashApp.isotope_analysis.app import create_isotope_analysis_app
from App.dashApp.hydrograph.app import create_hydrograph_app
from App.dashApp.chemograph.app import create_chemograph_app

app = Flask(import_name=__name__, static_folder='static')

app.config["DEBUG"] = True
# app.config['GOOGLEMAPS_KEY'] = "AIzaSyAHzR-Pu6GlvFtxS6Xz813bdGqUjUjM1w8"
# Bootstrap(app)
# datepicker(app)
# GoogleMaps(app)

# Upload folder
UPLOAD_FOLDER = 'App/static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SECRET_KEY'] = 'd3946e1cf4b2b53d4dcf5d9e3b126498ac2876892270735eddbb7e3aca8a7bbe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
app.config['SQLALCHEMY_BINDS'] = {
    'precipitation': 'sqlite:///dashApp/precipitation/precipitation.sqlite'
}



db = SQLAlchemy(app=app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app=app)
login_manager.login_view = 'login'
login_manager.login_message = 'لطفاً ابتدا وارد بشوید!'
login_manager.login_message_category = "info"


# create_isotope_analysis_app(server=app)
create_hydrograph_app(server=app)
create_chemograph_app(server=app)


from App import routes