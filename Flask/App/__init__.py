from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from App.dashApp.isotope_analysis.app import create_isotope_analysis_app
from App.dashApp.aquifer_hydrograph.app import create_aquifer_hydrograph_app

app = Flask(import_name=__name__, static_folder='static')
app.config['SECRET_KEY'] = 'd3946e1cf4b2b53d4dcf5d9e3b126498ac2876892270735eddbb7e3aca8a7bbe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
db = SQLAlchemy(app=app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app=app)
login_manager.login_view = 'login'
login_manager.login_message = 'لطفاً ابتدا وارد بشوید!'
login_manager.login_message_category = "info"


create_isotope_analysis_app(server=app)
create_aquifer_hydrograph_app(server=app)

from App import routes