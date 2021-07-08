import pandas as pd
import datetime
import sqlite3

db_path_precipitation = 'App/dashApps/precipitation/precipitation.sqlite'
dateBankPath = "App/static/assets/myDate.parquet.gzip"


def extract_wateryear(month, year):
    if month in [7, 8, 9, 10, 11, 12]:
        y_1 = year
        y_2 = year + 1
        return str(y_1) + "-" + str(y_2)[2:4]
    elif month in [1, 2, 3, 4, 5, 6]:
        y_1 = year - 1
        y_2 = year
        return str(y_1) + "-" + str(y_2)[2:4]
    else:
        return None


def addDateBanke(data, dateBank):    
    data['DATE'] = data['YEAR'].astype(str) + "-" + data['MONTH'].astype(str).str.zfill(2) + "-" + data['DAY'].astype(str).str.zfill(2) + " " + data['HOURE'].astype(str).str.zfill(2) + ":" + data['MINUTE'].astype(str).str.zfill(2) + ":" + data['SECOND'].astype(str).str.zfill(2)
    data["uniqueCode"] = data["stationCode"].astype(str) + "-" + data["DATE"]
    data = pd.merge(
        left=data,
        right=dateBank,
        how="left",
        left_on="DATE",
        right_on="date_time_persian"
    )
    return data

# db_precipitation_precip_data = addDateBanke(data=db_precipitation_precip_data, dateBank=pd.read_parquet(path=dateBankPath))