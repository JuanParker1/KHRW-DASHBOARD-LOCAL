import base64
import io
import re
import pandas as pd
import numpy as np
import geopandas as gpd
from itertools import compress
from srtm import Srtm1HeightMapCollection
import statistics
import assets.jalali as jalali
import json
import sqlite3


# -----------------------------------------------------------------------------
# READ CONNECTED SPREADSHEET File
# -----------------------------------------------------------------------------
# CASE-DEPENDENT
# WARNING : EXCEL FILE WITH SEVERAL SHEET
def read_spreadsheet(contents, filename):
    if 'xlsx' in filename:
        data = {}
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        spreadsheet_file = pd.ExcelFile(io.BytesIO(decoded))
        for sheet_name in spreadsheet_file.sheet_names:
            data[sheet_name] = spreadsheet_file.parse(sheet_name)
        return data


# -----------------------------------------------------------------------------
# EXTRACT GEOGRAPHICAL INFORMATION DATASET
# -----------------------------------------------------------------------------
# CASE-DEPENDENT
def extract_geo_info_dataset(data):
    columns = [
        "ID", "Mahdodeh_Name", "Mahdodeh_Code", "Aquifer_Name", "Well_Name",
        "X_Decimal", "Y_Decimal", "Final_Elevation"
    ]
    data = data[columns]
    data.drop_duplicates(keep="first", inplace=True)
    return data


# -----------------------------------------------------------------------------
# DATA CLEANSING
# -----------------------------------------------------------------------------
# CASE-DEPENDENT
def data_cleansing(well_info_data_all, dtw_data_all, thiessen_data_all, sc_data_all, threshold=0.5):
    result = pd.DataFrame()
    result_aquifer = pd.DataFrame()

    for aquifer in well_info_data_all['Aquifer_Name'].unique():
        well_info_data = well_info_data_all[well_info_data_all['Aquifer_Name'] == aquifer]
        dtw_data = dtw_data_all[dtw_data_all['Aquifer_Name'] == aquifer]
        thiessen_data = thiessen_data_all[thiessen_data_all['Aquifer_Name'] == aquifer]
        sc_data = sc_data_all[sc_data_all['Aquifer_Name'] == aquifer]

        # Well Info Data:------------------------------------------------------
        Columns_Info = list(compress(well_info_data.columns.tolist(),
                                     list(map(lambda x: isinstance(x, str),
                                              well_info_data.columns.tolist()))))

        Well_Info = well_info_data[Columns_Info]

        Well_Info['Aquifer_Name'] = Well_Info['Aquifer_Name'].apply(lambda x: x.rstrip())
        Well_Info['Aquifer_Name'] = Well_Info['Aquifer_Name'].apply(lambda x: x.lstrip())
        Well_Info['Well_Name'] = Well_Info['Well_Name'].apply(lambda x: x.rstrip())
        Well_Info['Well_Name'] = Well_Info['Well_Name'].apply(lambda x: x.lstrip())

        # Depth to Water (DTW) Data:--------------------------------------------

        # Extract Dates From Columns Name
        id_vars = list(compress(dtw_data.columns.tolist(),
                                list(map(lambda x: isinstance(x, str),
                                         dtw_data.columns.tolist()))))

        dtw_data['Aquifer_Name'] = dtw_data['Aquifer_Name'].apply(lambda x: x.rstrip())
        dtw_data['Aquifer_Name'] = dtw_data['Aquifer_Name'].apply(lambda x: x.lstrip())
        dtw_data['Well_Name'] = dtw_data['Well_Name'].apply(lambda x: x.rstrip())
        dtw_data['Well_Name'] = dtw_data['Well_Name'].apply(lambda x: x.lstrip())

        # Convert DTW Data to Wide Format
        DTW_Wide = pd.melt(frame=dtw_data,
                           id_vars=id_vars,
                           var_name="Date",
                           value_name="Depth_To_Water").pivot(index='Date',
                                                              columns='ID',
                                                              values='Depth_To_Water').reset_index()

        # Modify Columns Name
        DTW_Wide.columns = [col for col in DTW_Wide.columns]

        # Modified Date - Add Gregorian Date
        DTW_Wide["Date_Gregorian"] = list(map(lambda i: pd.to_datetime(i - 2, unit='D', origin='1900-01-01').date(),
                                              DTW_Wide["Date"]))

        # Modified Date - Add Persian Date
        DTW_Wide["Date_Persian"] = list(map(lambda i: jalali.Gregorian(i).persian_string(),
                                            DTW_Wide["Date_Gregorian"]))

        # Reorder Columns
        DTW_Wide = DTW_Wide.reindex(columns=(['Date', 'Date_Gregorian', 'Date_Persian'] + list(
            [a for a in DTW_Wide.columns if a not in ['Date', 'Date_Gregorian', 'Date_Persian']])))

        # Convert DTW_Wide Data Into A Tidy Format
        DTW = pd.melt(frame=DTW_Wide,
                      id_vars=['Date_Gregorian', 'Date', 'Date_Persian'],
                      value_name='Depth_To_Water',
                      var_name='ID').sort_values(['ID', 'Date_Gregorian']).drop('Date', axis=1)
        DTW = DTW[['ID', 'Date_Gregorian', 'Date_Persian', 'Depth_To_Water']]

        # Thiessen Weights Data:----------------------------------------------

        # Extract Dates From Columns Name
        id_vars = list(compress(thiessen_data.columns.tolist(),
                                list(map(lambda x: isinstance(x, str),
                                         thiessen_data.columns.tolist()))))

        thiessen_data['Aquifer_Name'] = thiessen_data['Aquifer_Name'].apply(lambda x: x.rstrip())
        thiessen_data['Aquifer_Name'] = thiessen_data['Aquifer_Name'].apply(lambda x: x.lstrip())
        thiessen_data['Well_Name'] = thiessen_data['Well_Name'].apply(lambda x: x.rstrip())
        thiessen_data['Well_Name'] = thiessen_data['Well_Name'].apply(lambda x: x.lstrip())

        # Convert Thiessen Data to Wide Format
        Thiessen_Wide = pd.melt(frame=thiessen_data,
                                id_vars=id_vars,
                                var_name="Date",
                                value_name="Area").pivot(index='Date',
                                                         columns='ID',
                                                         values='Area').reset_index()

        # Modify Columns Name
        Thiessen_Wide.columns = [col for col in Thiessen_Wide.columns]

        # Modified Date - Add Gregorian Date
        Thiessen_Wide["Date_Gregorian"] = list(map(lambda i: pd.to_datetime(i - 2, unit='D', origin='1900-01-01').date(),
                                                   Thiessen_Wide["Date"]))

        # Modified Date - Add Persian Date
        Thiessen_Wide["Date_Persian"] = list(map(lambda i: jalali.Gregorian(i).persian_string(),
                                                 Thiessen_Wide["Date_Gregorian"]))

        # Reorder Columns
        Thiessen_Wide = Thiessen_Wide.reindex(columns=(['Date', 'Date_Gregorian', 'Date_Persian'] + list(
            [a for a in Thiessen_Wide.columns if a not in ['Date', 'Date_Gregorian', 'Date_Persian']])))

        # Convert DTW_Wide Data Into A Tidy Format
        Thiessen = pd.melt(frame=Thiessen_Wide,
                           id_vars=['Date_Gregorian', 'Date', 'Date_Persian'],
                           value_name='Area',
                           var_name='ID').sort_values(['ID', 'Date_Gregorian']).drop('Date', axis=1)
        Thiessen = Thiessen[['ID', 'Date_Gregorian', 'Date_Persian', 'Area']]

        # Sum Thiessen for Each Month (Area Aquifer)
        Thiessen = pd.merge(left=Thiessen,
                            right=Thiessen.groupby(by='Date_Gregorian').sum().reset_index().rename(
                                columns={'Area': 'Aquifer_Area'}),
                            how='outer',
                            on='Date_Gregorian').sort_values(['ID', 'Date_Gregorian'])

        # Storage Coefficient Data:------------------------------------------

        # Extract Dates From Columns Name
        id_vars = list(compress(sc_data.columns.tolist(),
                                list(map(lambda x: isinstance(x, str),
                                         sc_data.columns.tolist()))))

        sc_data['Aquifer_Name'] = sc_data['Aquifer_Name'].apply(lambda x: x.rstrip())
        sc_data['Aquifer_Name'] = sc_data['Aquifer_Name'].apply(lambda x: x.lstrip())
        sc_data['Well_Name'] = sc_data['Well_Name'].apply(lambda x: x.rstrip())
        sc_data['Well_Name'] = sc_data['Well_Name'].apply(lambda x: x.lstrip())

        # Convert Storage Coefficient Data to Wide Format
        Storage_Coefficient_Wide = pd.melt(frame=sc_data,
                                           id_vars=id_vars,
                                           var_name="Date",
                                           value_name="Storage_Coefficient").pivot(index='Date',
                                                                                   columns='ID',
                                                                                   values='Storage_Coefficient').reset_index()

        # Modify Columns Name
        Storage_Coefficient_Wide.columns = [col for col in Storage_Coefficient_Wide.columns]

        # Modified Date - Add Gregorian Date
        Storage_Coefficient_Wide["Date_Gregorian"] = list(
            map(lambda i: pd.to_datetime(i - 2, unit='D', origin='1900-01-01').date(),
                Storage_Coefficient_Wide["Date"]))

        # Modified Date - Add Persian Date
        Storage_Coefficient_Wide["Date_Persian"] = list(map(lambda i: jalali.Gregorian(i).persian_string(),
                                                            Storage_Coefficient_Wide["Date_Gregorian"]))

        # Reorder Columns
        Storage_Coefficient_Wide = Storage_Coefficient_Wide.reindex(columns=(
                    ['Date', 'Date_Gregorian', 'Date_Persian'] + list(
                [a for a in Storage_Coefficient_Wide.columns if a not in ['Date', 'Date_Gregorian', 'Date_Persian']])))

        # Convert Storage_Coefficient_Wide Data Into A Tidy Format
        Storage_Coefficient = pd.melt(frame=Storage_Coefficient_Wide,
                                      id_vars=['Date_Gregorian', 'Date', 'Date_Persian'],
                                      value_name='Storage_Coefficient',
                                      var_name='ID').sort_values(['ID', 'Date_Gregorian']).drop('Date', axis=1)
        Storage_Coefficient = Storage_Coefficient[['ID', 'Date_Gregorian', 'Date_Persian', 'Storage_Coefficient']]

        # Surface Elevation of Observation Well:----------------------------
        # Extract Surface Elevation of Observation Well From NASA Shuttle Radar Topography Mission (SRTM) Version 3.0
        # srtm1_data = Srtm1HeightMapCollection()

        # Well_Info["G.S.L_DEM_SRTM1"] = list(
        #     map(lambda LonLat: srtm1_data.get_altitude(longitude=LonLat[0], latitude=LonLat[1]),
        #         zip(Well_Info.X_Decimal, Well_Info.Y_Decimal)))

        Well_Info["G.S.L_DEM_SRTM1"] = Well_Info["Final_Elevation"]

        Elevation = Well_Info[['ID', 'G.S.L_M.S.L', 'Final_Elevation', 'G.S.L_DEM_SRTM1']]
        # Elevation = Well_Info[['ID', 'G.S.L_M.S.L', 'Final_Elevation']]

        Elevation.columns = ['ID', 'MSL_Elevation', 'Final_Elevation', 'Elevation']
        # Elevation.columns = ['ID', 'MSL_Elevation', 'Final_Elevation']

        # Combine Data:-----------------------------------------------------
        data = pd.merge(left=DTW,
                        right=Elevation,
                        how='outer',
                        on=['ID']).merge(right=Thiessen,
                                         how='outer',
                                         on=['ID', 'Date_Gregorian', 'Date_Persian']).merge(right=Storage_Coefficient,
                                                                                            how='outer',
                                                                                            on=['ID', 'Date_Gregorian',
                                                                                                'Date_Persian']).sort_values(
            ['ID', 'Date_Gregorian'])

        # Calculate Aquifer Storage Coefficient:------------------------------------
        data['Unit_Aquifer_Storage_Coefficient'] = (data['Storage_Coefficient'] * data['Area']) / data['Aquifer_Area']

        # Sum Aquifer Storage Coefficient for Each Month (Aquifer Storage Coefficient)
        df = data.groupby(by=['Date_Gregorian', 'Date_Persian']).sum().reset_index()[
            ['Date_Gregorian', 'Date_Persian', 'Unit_Aquifer_Storage_Coefficient']].rename(
            columns={'Unit_Aquifer_Storage_Coefficient': 'Aquifer_Storage_Coefficient'})

        data = data.merge(right=df,
                          how='outer',
                          on=['Date_Gregorian', 'Date_Persian']).sort_values(['ID', 'Date_Gregorian'])

        #  Calculate Well Head:----------------------------------------------
        data['Well_Head'] = data['Final_Elevation'] - data['Depth_To_Water']

        # Calculate Aquifer Head:--------------------------------------------
        data['Unit_Aquifer_Head'] = (data['Well_Head'] * data['Area']) / data['Aquifer_Area']

        # Sum Units Aquifer Head for Each Month (Aquifer_Head)
        df = data.groupby(by=['Date_Gregorian', 'Date_Persian']).sum().reset_index()[
            ['Date_Gregorian', 'Date_Persian', 'Unit_Aquifer_Head']].rename(columns={'Unit_Aquifer_Head': 'Aquifer_Head'})

        data = data.merge(right=df,
                          how='outer',
                          on=['Date_Gregorian', 'Date_Persian']).sort_values(['ID', 'Date_Gregorian'])

        df = data[['Date_Gregorian', 'Date_Persian', 'Well_Head']].groupby(by=['Date_Gregorian', 'Date_Persian']).agg({
            'Well_Head': [statistics.mean, statistics.geometric_mean, statistics.harmonic_mean]
        }).reset_index()

        df.columns = [col for col in df.columns]

        df.columns = ['Date_Gregorian', 'Date_Persian', 'Aquifer_Head_Arithmetic_Mean', 'Aquifer_Head_Geometric_Mean', 'Aquifer_Head_Harmonic_Mean']

        data = data.merge(right=df,
                          how='outer',
                          on=['Date_Gregorian', 'Date_Persian']).sort_values(['ID', 'Date_Gregorian'])
        
        

        # Add Name Well
        data = data.merge(right=Well_Info[
            ['Mahdodeh_Name', 'Mahdodeh_Code', 'Aquifer_Name', 'Well_Name', 'ID', 'X_UTM', 'Y_UTM', 'X_Decimal',
             'Y_Decimal']],
                          how='outer',
                          left_on=['ID'],
                          right_on=['ID']).sort_values(['ID', 'Date_Gregorian'])
        
        result = result.append(data)
        


        # ADJUSMENT AQUIFER HEAD
        data_aquifer = data.drop_duplicates(subset=['Date_Gregorian', 'Date_Persian'], keep='last').reset_index()
        
        data_aquifer = data_aquifer[[
            "Date_Gregorian", "Date_Persian",
            "Aquifer_Area", "Aquifer_Storage_Coefficient", "Aquifer_Head",
            "Aquifer_Head_Arithmetic_Mean", "Aquifer_Head_Geometric_Mean", "Aquifer_Head_Harmonic_Mean",
            "Mahdodeh_Name", 'Mahdodeh_Code', "Aquifer_Name"
        ]]

        data_aquifer.replace(0, np.nan, inplace=True)
        data_aquifer['Delta'] = data_aquifer['Aquifer_Head'].diff().fillna(0)
        data_aquifer['Index'] = abs(data_aquifer['Delta']).apply(lambda x: 1 if x >= threshold else 0)
        data_aquifer['Adjusted_Aquifer_Head'] = data_aquifer['Aquifer_Head']
        

        n = data_aquifer.index[data_aquifer['Index'] == True].tolist()
        
        
        if len(n) > 0:
            while len(n) != 0:
                delta = data_aquifer['Delta'][n[0]]
                data_aquifer['Temp_Aquifer_Head'] = data_aquifer['Adjusted_Aquifer_Head']
                for i in range(n[0]):
                    data_aquifer['Temp_Aquifer_Head'][i] = data_aquifer['Adjusted_Aquifer_Head'][i] + delta
                    data_aquifer['Adjusted_Aquifer_Head'] = data_aquifer['Temp_Aquifer_Head']
                    data_aquifer['Delta'] = data_aquifer['Adjusted_Aquifer_Head'].diff().fillna(0)
                    data_aquifer['Index'] = abs(data_aquifer['Delta']).apply(lambda x: 1 if x >= threshold else 0)
                    n = data_aquifer.index[data_aquifer['Index'] == True].tolist()
                    
        
        if 'Temp_Aquifer_Head' in data_aquifer.columns:
            data_aquifer = data_aquifer.drop(['Temp_Aquifer_Head'], axis=1)

        if 'Delta' in data_aquifer.columns:
            data_aquifer = data_aquifer.drop(['Delta'], axis=1)

        if 'Index' in data_aquifer.columns:
            data_aquifer = data_aquifer.drop(['Index'], axis=1)

                
        result_aquifer = result_aquifer.append(data_aquifer)

        
    result['Aquifer_Name'] = result['Aquifer_Name'].apply(lambda x: x.rstrip())
    result['Aquifer_Name'] = result['Aquifer_Name'].apply(lambda x: x.lstrip())
    result['Well_Name'] = result['Well_Name'].apply(lambda x: x.rstrip())
    result['Well_Name'] = result['Well_Name'].apply(lambda x: x.lstrip())
    result_aquifer['Aquifer_Name'] = result_aquifer['Aquifer_Name'].apply(lambda x: x.rstrip())
    result_aquifer['Aquifer_Name'] = result_aquifer['Aquifer_Name'].apply(lambda x: x.lstrip())
    
    result[['year_Date_Persian', 'month_Date_Persian', 'day_Date_Persian']] = result.Date_Persian.str.split('-', expand=True)
    result['year_Date_Persian'] = result['year_Date_Persian'].astype(int)
    result['month_Date_Persian'] = result['month_Date_Persian'].astype(int)
    result['day_Date_Persian'] = result['day_Date_Persian'].astype(int)
    result['Date_Gregorian'] = pd.to_datetime(result['Date_Gregorian'])
    
    result_aquifer[['year_Date_Persian', 'month_Date_Persian', 'day_Date_Persian']] = result_aquifer.Date_Persian.str.split('-', expand=True)
    result_aquifer['year_Date_Persian'] = result_aquifer['year_Date_Persian'].astype(int)
    result_aquifer['month_Date_Persian'] = result_aquifer['month_Date_Persian'].astype(int)
    result_aquifer['day_Date_Persian'] = result_aquifer['day_Date_Persian'].astype(int)
    result_aquifer['Date_Gregorian'] = pd.to_datetime(result_aquifer['Date_Gregorian'])
    
    
    
    
    return result, result_aquifer



# -----------------------------------------------------------------------------
# READ SHAPEFILES
# -----------------------------------------------------------------------------
# EDITPATH
def read_shapfile(
        file_path = "./assets/ShapeFiles/AreaStudy/AreaStudy.shp",
        mah_code = None
):
    if mah_code is not None:
        geodf = gpd.read_file(file_path, encoding='windows-1256')
        geodf = geodf[geodf['Mah_code'].isin(mah_code)]
        j_file = json.loads(geodf.to_json())

        for feature in j_file["features"]:
            feature['id'] = feature['properties']['Mah_code']

        return geodf, j_file





# -----------------------------------------------------------------------------
# LOAD DATA
# -----------------------------------------------------------------------------
db_path = 'aquifer_hydrograph.sqlite'
token_path = "assets/.mapbox_token"

token = open(token_path).read()

db = sqlite3.connect(db_path)
table_name = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", db)


try:
    if table_name['name'].str.contains('RawDATA').any():
        RawDATA = pd.read_sql_query(sql="SELECT * FROM RawDATA", con=db)
        GeoInfoData = extract_geo_info_dataset(RawDATA)
    else:
        print("ERROR: RawDATA TABLE NOT EXIST")
except:
    print("ERROR: DATABASE NOT EXIST")

try:
    if table_name['name'].str.contains('AquiferDATA').any():
        AquiferDATA = pd.read_sql_query(sql="SELECT * FROM AquiferDATA", con=db)
    else:
        print("ERROR: AquiferDATA TABLE NOT EXIST")
except:
    print("ERROR: DATABASE NOT EXIST")



# -----------------------------------------------------------------------------
# WATER YEAR - DIFF - CUMSUM
# -----------------------------------------------------------------------------
# Column 1: Persian Year (YYYY) - سال
# Column 2: Persian Month (MM) - ماه
# Column 3: Value -پارامتر

def waterYear(df):
    if df["ماه"] >= 7 and df["ماه"] <= 12:
        WY = str(int(df["سال"])) + "-" + str(int(df["سال"]) + 1)[2:4]
        WM = int(df["ماه"]) - 6
    elif df["ماه"] >= 1 and df["ماه"] <= 6:
        WY = str(int(df["سال"]) - 1) + "-" + str(int(df["سال"]))[2:4]
        WM = int(df["ماه"]) + 6
    else:
        WY = None
        WM = None
    return [WY, WM]


def resultTable(df):
    df["پارامتر"] = df["پارامتر"].round(2)    
    df["WATER_YEAR"] = df.apply(waterYear, axis=1)
    df[['سال آبی','ماه آبی']] = pd.DataFrame(df.WATER_YEAR.tolist(), index= df.index)
    df.drop('WATER_YEAR', inplace=True, axis=1)
    df["اختلاف ماه"] = df["پارامتر"] - df["پارامتر"].shift(1)
    df["اختلاف ماه"] = df["اختلاف ماه"].round(2)
    df = df.sort_values(['ماه', 'سال'])
    result = pd.DataFrame()
    for m in range(1,13):
        d = df[df["ماه"] == m]
        d["اختلاف ماه سال"] = d["پارامتر"] - d["پارامتر"].shift(1)
        result = pd.concat([result, d])
    result = result.sort_values(['سال', 'ماه'])
    result["اختلاف ماه سال"] = result["اختلاف ماه سال"].round(2)
    
    return result

def resultTableAquifer(df):
    df["هد"] = df["هد"].round(2)   
    df["مساحت"] = df["مساحت"].round(2)   
    df["ضریب"] = df["ضریب"].round(2)
    df["WATER_YEAR"] = df.apply(waterYear, axis=1)
    df[['سال آبی','ماه آبی']] = pd.DataFrame(df.WATER_YEAR.tolist(), index= df.index)
    df.drop('WATER_YEAR', inplace=True, axis=1)
    df["اختلاف ماه"] = df["هد"] - df["هد"].shift(1)
    df["اختلاف ماه"] = df["اختلاف ماه"].round(2)
    
    df = df.sort_values(['ماه', 'سال'])
    result = pd.DataFrame()
    for m in range(1,13):
        d = df[df["ماه"] == m]
        d["اختلاف ماه سال"] = d["هد"] - d["هد"].shift(1)
        result = pd.concat([result, d])
    result = result.sort_values(['سال', 'ماه'])
    result["اختلاف ماه سال"] = result["اختلاف ماه سال"].round(2)
    
    return result