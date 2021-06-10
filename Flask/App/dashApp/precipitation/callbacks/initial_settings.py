# --------------------------------------------------------------------------- #
#                                                                             #
#                         IMPORT REQUIREMENT MODULE                           #
#                                                                             #
# --------------------------------------------------------------------------- #

import os
import sqlite3
import base64
import pandas as pd
import geopandas as gpd
import json
import plotly.graph_objects as go
import plotly.express as px


# --------------------------------------------------------------------------- #
#                                                                             #
#                                 FUNCTIONS                                   #
#                                                                             #
# --------------------------------------------------------------------------- #

# READ SHAPEFILES FUNCTION
# --------------------------------------------------------------------------- #

def read_shapfile(
    shapefile=None,
    column=None,
    target="all"
):
    # geodf = gpd.read_file(shapefile, encoding='windows-1256')
    geodf = gpd.read_file(shapefile, encoding='utf-8')

    if target == "all":
        j_file = json.loads(geodf.to_json())
    else:
        geodf = geodf[geodf[column].isin(target)]
        j_file = json.loads(geodf.to_json())

    for feature in j_file["features"]:
        feature['id'] = feature['properties'][column]

    return geodf, j_file


# CHECK LEAP YEAR
# --------------------------------------------------------------------------- #

def check_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                True
            else:
                False
        else:
            True
    else:
        False


# WATER YEAR EXTRACT FUNCTION
# --------------------------------------------------------------------------- #

def water_year(
    year,
    month,
    day
):
    # YEAR AND MONTH
    if month >= 7 and month <= 12:
        WY = str(int(year)) + "-" + str(int(year) + 1)[2:4]
        WM = int(month) - 6
    elif month >= 1 and month <= 6:
        WY = str(int(year) - 1) + "-" + str(int(year))[2:4]
        WM = int(month) + 6
    else:
        WY = None
        WM = None

    # DAY
    if WM <= 6:
        WD = int(((WM - 1) * 30) + day)
    elif WM >= 7 and check_leap_year(year - 1):
        WD = int((6 * 30) + ((WM - 7) * 31) + day)
    elif WM >= 7 and not check_leap_year(year - 1):
        WD = int((5 * 30) + (1 * 29) + ((WM - 7) * 31) + day)
    else:
        WD = None

    return [WY, WM, WD]


# --------------------------------------------------------------------------- #
#                                                                             #
#                     VARIABLES, CONSTANTS AND PARAMETERS                     #
#                                                                             #
# --------------------------------------------------------------------------- #

# IMAGES
# --------------------------------------------------------------------------- #

IMAGES_FOLDER_PATH = "./App/static/precipitation/images/"  # EDITPATH


DATABASE_LOGO = base64.b64encode(
    open(IMAGES_FOLDER_PATH + 'DATABASE_LOGO.png', 'rb').read()
).decode()


DRAINAGE_BASIN_LOGO = base64.b64encode(
    open(IMAGES_FOLDER_PATH + 'DRAINAGE_BASIN_LOGO.png', 'rb').read()
).decode()


STUDY_AREA_LOGO = base64.b64encode(
    open(IMAGES_FOLDER_PATH + 'STUDY_AREA_LOGO.png', 'rb').read()
).decode()


DROP_WATER_LOGO = base64.b64encode(
    open(IMAGES_FOLDER_PATH + 'DROP_WATER_LOGO.png', 'rb').read()
).decode()


ALTITUDE_LOGO = base64.b64encode(
    open(IMAGES_FOLDER_PATH + 'ALTITUDE_LOGO.png', 'rb').read()
).decode()


CALENDAR_LOGO = base64.b64encode(
    open(IMAGES_FOLDER_PATH + 'CALENDAR_LOGO.png', 'rb').read()
).decode()


# SHAPEFILES
# --------------------------------------------------------------------------- #

SHAPEFILES_FOLDER_PATH = "./App/static/shapefiles/"  # EDITPATH

# Hoze6: Hoze6Code, Hoze6Name, Hoze6Full, Area, Perimeter
HOZE6 = SHAPEFILES_FOLDER_PATH + "Hoze6/Hoze6.shp"


# Hoze30: Hoze30Code, Hoze30Name, Hoze30Full, Area, Perimeter
HOZE30 = SHAPEFILES_FOLDER_PATH + "Hoze30/Hoze30.shp"


# Mahdoude: MahCode, MahName, OsMoteval, Hoze30Code, Hoze30Name, Hoze6Code, Hoze6Name, Area, Perimeter
MAHDOUDE = SHAPEFILES_FOLDER_PATH + "Mahdoude/Mahdoude.shp"


# Shahrestan: Shahrestan, Ostan, Area, Perimeter
SHAHRESTAN = SHAPEFILES_FOLDER_PATH + "Shahrestan/Shahrestan.shp"


# MAPBOX ACCESS TOKEN
# --------------------------------------------------------------------------- #

TOKEN_PATH = "./App/static/.mapbox_token"
token = open(TOKEN_PATH).read()


# DATABASE
# --------------------------------------------------------------------------- #

# TABLES:

#   precipitation:
#       id, stationCode, YEAR, MONTH, DAY, HOURE, MINUTE, SECOND,
#       BARAN, BARF, AB_BARF, JAM_BARAN

#   station:
#       stationName, stationCode, stationOldCode, drainageArea6,
#       drainageArea30, areaStudyName, areaStudyCode, omor, county,
#       startYear, longDecimalDegrees, latDecimalDegrees, elevation

precipitation_db_path = './App/dashApp/precipitation/precipitation.sqlite'

if os.path.exists(precipitation_db_path):
    try:
        global precipitation_db
        global data
        global station

        precipitation_db = sqlite3.connect(
            precipitation_db_path, check_same_thread=False
        )

        data = pd.read_sql_query(
            sql="SELECT * FROM precipitation", con=precipitation_db
        )

        station = pd.read_sql_query(
            sql="SELECT * FROM station", con=precipitation_db
        )

        data[['WATERYEAR', 'WATERMONTH', 'WATREDAY']] = pd.DataFrame(data.apply(lambda row: water_year(row.YEAR, row.MONTH, row.DAY),
                                                                                axis=1).to_list(), columns=['WATERYEAR', 'WATERMONTH', 'WATREDAY'])

    except print("NO DATABASE EXIST!"):
        pass


# NO DATABASE CONNECTINO TEMPLATE
# --------------------------------------------------------------------------- #

NO_DATABASE_CONNECTION = {
    "layout": {
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "annotations": [
            {
                "text": "No Database Connection ...",
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {"size": 36}
            }
        ]
    }
}


# NO MATCHING DATA FOUND TEMPLATE
# --------------------------------------------------------------------------- #

NO_MATCHING_DATA_FOUND = {
    "layout": {
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "annotations": [
            {
                "text": "No Data Found ...",
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {"size": 36}
            }
        ]
    }
}


# BASE MAP - EMPTY
# --------------------------------------------------------------------------- #

BASE_MAP_EMPTY = go.Figure(
    go.Scattermapbox(
        lat=[36.25],
        lon=[59.55],
        mode='markers',
        marker=go.scattermapbox.Marker(size=9),
        text="شهر مشهد"
    )
)

BASE_MAP_EMPTY.update_layout(
    mapbox={
        'style': "stamen-terrain",
        'center': {
            'lon': 59.55,
            'lat': 36.25
        },
        'zoom': 5.5
    },
    showlegend=False,
    hovermode='closest',
    margin={'l': 0, 'r': 0, 'b': 0, 't': 0},
    autosize=False
)


# STATION TABLE - FARSI HEADER
# --------------------------------------------------------------------------- #

# CASE-DEPENDENT
STATION_TABLE_FARSI_HEADER_NAME = {
    "stationName": "نام ایستگاه",
    "stationCode": "کد ایستگاه",
    "stationOldCode": "کد قدیم ایستگاه",
    "drainageArea6": "حوضه آبریز درجه یک",
    "drainageArea30": "حوضه آبریز درجه دو",
    "areaStudyName": "نام محدوده",
    "areaStudyCode": "کد محدوده",
    "omor": "امور",
    "county": "شهرستان",
    "startYear": "سال شروع",
    "longDecimalDegrees": "طول جغرافیایی",
    "latDecimalDegrees": "عرض جغرافیایی",
    "elevation": "ارتفاع"
}


# MONTH NAME
# --------------------------------------------------------------------------- #
M_WATERYEAR = ["مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]
M_SHAMSIYEAR = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]