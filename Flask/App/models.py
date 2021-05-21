from App import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.username}, {self.email})"


class Station(db.Model):
    __bind_key__ = 'precipitation'
    stationName = db.Column(db.String(50), nullable=False)
    stationCode = db.Column(db.Integer, nullable=False, primary_key=True)
    stationOldCode = db.Column(db.String(50), nullable=False)
    drainageArea6 = db.Column(db.String(50), nullable=False)
    drainageArea30 = db.Column(db.String(50), nullable=False)
    areaStudyName = db.Column(db.String(50), nullable=False)
    omor = db.Column(db.String(50), nullable=False)
    county = db.Column(db.String(50), nullable=False)
    startYear = db.Column(db.String(4), nullable=False)
    longDecimalDegrees = db.Column(db.Float, nullable=False)
    latDecimalDegrees = db.Column(db.Float, nullable=False)
    elevation = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.stationCode}, {self.stationName}, {self.areaStudyName})"


class Precipitation(db.Model):
    __bind_key__ = 'precipitation'
    id = db.Column(db.Integer, primary_key=True)
    stationCode = db.Column(db.Integer, nullable=False)
    YEAR = db.Column(db.Integer, nullable=False)
    MONTH = db.Column(db.Integer, nullable=False)
    DAY = db.Column(db.Integer, nullable=False)
    HOURE = db.Column(db.Integer, nullable=False)
    MINUTE = db.Column(db.Integer, nullable=False)
    SECOND = db.Column(db.Integer, nullable=False)
    BARAN = db.Column(db.Float, nullable=True)
    BARF = db.Column(db.Float, nullable=True)
    AB_BARF = db.Column(db.Float, nullable=True)
    JAM_BARAN = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.stationCode}, {self.YEAR}, {self.MONTH}, {self.DAY})"
    
    
