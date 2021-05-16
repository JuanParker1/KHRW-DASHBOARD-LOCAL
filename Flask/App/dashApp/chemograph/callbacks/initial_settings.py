import base64
import io
import pandas as pd
import numpy as np
import geopandas as gpd
from itertools import compress
import json
import plotly.graph_objects as go
import plotly.express as px



# -----------------------------------------------------------------------------
# SHAPEFILES LOCATION
# -----------------------------------------------------------------------------
AQUIFERS = "./App/static/shapefiles/Aquifers/Aquifers.shp"
AREASTUDIES = "./App/static/shapefiles/AreaStudies/AreaStudies.shp"



# -----------------------------------------------------------------------------
# MAPBOX CONFIG
# -----------------------------------------------------------------------------
TOKEN_PATH = "./App/static/.mapbox_token"
token = open(TOKEN_PATH).read()


# -----------------------------------------------------------------------------
# SUPER AND SUB SCRIPT CHARECHTER
# -----------------------------------------------------------------------------
superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹", "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ",
    "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ᶦ", "j": "ʲ", "k": "ᵏ",
    "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "q": "۹", "r": "ʳ",
    "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ",
    "z": "ᶻ", "A": "ᴬ", "B": "ᴮ", "C": "ᶜ", "D": "ᴰ", "E": "ᴱ", "F": "ᶠ",
    "G": "ᴳ", "H": "ᴴ", "I": "ᴵ", "J": "ᴶ", "K": "ᴷ", "L": "ᴸ", "M": "ᴹ",
    "N": "ᴺ", "O": "ᴼ", "P": "ᴾ", "Q": "Q", "R": "ᴿ", "S": "ˢ", "T": "ᵀ",
    "U": "ᵁ", "V": "ⱽ", "W": "ᵂ", "X": "ˣ", "Y": "ʸ", "Z": "ᶻ", "+": "⁺",
    "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾"}


subscript_map = {
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆",
    "7": "₇", "8": "₈", "9": "₉", "a": "ₐ", "b": "♭", "c": "꜀", "d": "ᑯ",
    "e": "ₑ", "f": "բ", "g": "₉", "h": "ₕ", "i": "ᵢ", "j": "ⱼ", "k": "ₖ",
    "l": "ₗ", "m": "ₘ", "n": "ₙ", "o": "ₒ", "p": "ₚ", "q": "૧", "r": "ᵣ",
    "s": "ₛ", "t": "ₜ", "u": "ᵤ", "v": "ᵥ", "w": "w", "x": "ₓ", "y": "ᵧ",
    "z": "₂", "A": "ₐ", "B": "₈", "C": "C", "D": "D", "E": "ₑ", "F": "բ",
    "G": "G", "H": "ₕ", "I": "ᵢ", "J": "ⱼ", "K": "ₖ", "L": "ₗ", "M": "ₘ",
    "N": "ₙ", "O": "ₒ", "P": "ₚ", "Q": "Q", "R": "ᵣ", "S": "ₛ", "T": "ₜ",
    "U": "ᵤ", "V": "ᵥ", "W": "w", "X": "ₓ", "Y": "ᵧ", "Z": "Z", "+": "₊",
    "-": "₋", "=": "₌", "(": "₍", ")": "₎"}


# -----------------------------------------------------------------------------
# READ CONNECTED SPREADSHEET File
# -----------------------------------------------------------------------------
# CASE-DEPENDENT
# WARNING : EXCEL FILE WITH SEVERAL SHEET
def read_spreadsheet(contents, filename, sheet_name="Sheet1"):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'xlsx' in filename:
            data = pd.read_excel(io.BytesIO(decoded), sheet_name=sheet_name)
            return data
        if 'csv' in filename:
            data = pd.read_csv(io.StringIO(decoded.decode('utf-8')), sheet_name=sheet_name)
            return data
    except Exception as e:
        print(e)
        return "There Was An Error Processing This File."


# -----------------------------------------------------------------------------
# EXTRACT GEOGRAPHICAL INFORMATION FROM DATASET
# -----------------------------------------------------------------------------
# CASE-DEPENDENT
def extract_geoinformation(data):
    columns = [
        "mahdodeh_name",
        "mahdodeh_code",
        "mahdodeh_area",
        "mahal",
        "mahal_area",
        "decimal_degrees_long",
        "decimal_degrees_lat",
        "utm_easting",
        "utm_northing",
    ]
    data = data[columns]
    data.drop_duplicates(keep="first", inplace=True)
    return data


# -----------------------------------------------------------------------------
# READ SHAPEFILES
# -----------------------------------------------------------------------------
# EDITPATH
def read_shapfile(
    file_path = None,
    code_column_name = None,
    selected_code = None        
):
    if selected_code is not None:
        geodf = gpd.read_file(file_path, encoding='windows-1256')
        if selected_code == "all":
            j_file = json.loads(geodf.to_json())
        else:
            geodf = geodf[geodf[code_column_name].isin(selected_code)]
            j_file = json.loads(geodf.to_json())
            
        for feature in j_file["features"]:
            feature['id'] = feature['properties'][code_column_name]
            
        return geodf, j_file


# -----------------------------------------------------------------------------
# NO DATABASE CONNECTINO TEMPLATE
# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
# NO MATCHING DATA FOUND TEMPLATE
# -----------------------------------------------------------------------------
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



# -----------------------------------------------------------------------------
# BASE MAP - EMPTY
# -----------------------------------------------------------------------------
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
    margin={'l':0, 'r':0, 'b':0, 't':0},
    autosize=False
)



# -----------------------------------------------------------------------------
# BASE MAP - AREA STUDIES
# -----------------------------------------------------------------------------
def base_map_area_studies(state):
    if state == "OK":
        geodf, j_file = read_shapfile(
            file_path = AREASTUDIES,
            code_column_name = "Mah_Code",
            selected_code = 'all'
        )
        
        fig = px.choropleth_mapbox(
            data_frame=geodf,
            geojson=j_file,
            locations='Mah_Code',
            opacity=0.3,
        )
            
        fig.update_layout(clickmode='event+select')
        
        fig.update_layout(
            mapbox={
                # 'style': "stamen-terrain",
                'style': "light",
                'center': {'lon': 58.8,
                           'lat': 35.9},
                'zoom': 5.5},
            showlegend=False,
            hovermode='closest',
            margin={'l': 0, 'r': 0, 'b': 0, 't': 0},
            mapbox_accesstoken=token
        )
        
        return fig
    else:
        return BASE_MAP_EMPTY



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


# -----------------------------------------------------------------------------
# MAP - AREA STUDIES & WELLS & SELLECTED WELLS
# -----------------------------------------------------------------------------
def map_area_studies_wells(
    state="NO",
    data=None,
    shapefile_path=None,
    shapefile_mahdodeh_code_column=None,
    selected_mahdodeh=None,
    selected_wells=None
):    
    if state == "OK":
        
        data = data[data['mahdodeh_name'].isin(selected_mahdodeh)]
        mah_code = list(data['mahdodeh_code'].unique())
        
        if selected_wells == "all":
            selected_wells = list(data['mahal'].unique())
            
        data_wells = data[data['mahal'].isin(selected_wells)]    

        geodf, j_file = read_shapfile(
            file_path = shapefile_path,
            code_column_name = shapefile_mahdodeh_code_column,
            selected_code = mah_code
        )
        
        fig = px.choropleth_mapbox(
            data_frame=geodf,
            geojson=j_file,
            locations=shapefile_mahdodeh_code_column,
            opacity=0.3,
        )
            
        fig.update_layout(clickmode='event+select')
        
        fig.add_trace(
            go.Scattermapbox(
                lat=data.decimal_degrees_lat,
                lon=data.decimal_degrees_long,
                mode='markers',
                marker=go.scattermapbox.Marker(size=10),
                text=data['mahal'],
                hoverinfo='text',
                hovertemplate='<b>%{text}</b><extra></extra>'
            )
        )
        
        fig.add_trace(
            go.Scattermapbox(
                lat=data_wells.decimal_degrees_lat,
                lon=data_wells.decimal_degrees_long,
                mode='markers',
                marker=go.scattermapbox.Marker(
                    size=10,
                    color='green'
                ),
                text=data_wells["mahal"],
                hoverinfo='text',
                hovertemplate='<b>%{text}</b><extra></extra>'
            ), 
        )
               
        fig.update_layout(
            mapbox = {
                'style': "stamen-terrain",
                'zoom': 5,
                'center': {
                    'lat': data_wells.decimal_degrees_lat.mean(),
                    'lon': data_wells.decimal_degrees_long.mean(),
                },
            },
            showlegend = False,
            hovermode='closest',
            margin = {'l':0, 'r':0, 'b':0, 't':0},
            width=250,
            height=250

        )
        
        return fig
    else:
        return BASE_MAP_EMPTY.update_layout(
                width=250,
                height=250
            )
