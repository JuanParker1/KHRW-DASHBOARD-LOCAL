from logging import info
import os
import sqlite3
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px

from server import app
from callbacks.initial_settings import *
from callbacks.database_config import *


# # -----------------------------------------------------------------------------
# # DEBUG SECTION
# # -----------------------------------------------------------------------------
# @app.callback(
#     Output("DEBUG_OUTPUT-TAB1_SIDEBAR_CARD3", "children"),
#     Output("DEBUG_BUTTON-TAB1_SIDEBAR_CARD3", "n_clicks"),
#     Input("DEBUG_CONTENT-TAB1_SIDEBAR_LEFT_CARD3", "value"),
#     Input("DEBUG_BUTTON-TAB1_SIDEBAR_CARD3", "n_clicks"),
# )
# def FUNCTION_DEBUG_TAB_SIDEBAR_LEFT_CARD3(value, n):
#     if n != 0 and value is not None:
#         print("-" * 80)
#         print(value)
#         print("-" * 30)
#         print(eval(value))
#         return "OK", 0
#     else:
#         return "No Value", 0


# CASE-DEPENDENT
TABLE_HEADER_NAME = {    
    "mahdodeh_name": "نام محدوده",
    "mahdodeh_code": "کد محدوده",
    "mahdodeh_area": "مساحت محدوده",
    "mahal": "محل",
    "mahal_area": "مساحت محل",
    "utm_easting": "طول جغرافیایی - UTM",
    "utm_northing": "عرض جغرافیایی - UTM",
    "decimal_degrees_long": "طول جغرافیایی",
    "decimal_degrees_lat": "عرض جغرافیایی",
    "year": "سال",
    "month": "ماه",
    "day": "روز",
    "ca": "Ca{}{} (Calcium)".format(superscript_map["+"], superscript_map["2"]),
    "mg": "Mg{}{} (Magnesium)".format(superscript_map["+"], superscript_map["2"]),
    "na": "Na{} (Sodium)".format(superscript_map["+"]),
    "k": "	K{} (Potassium)".format(superscript_map["+"]),
    "cl": "Cl{} (Chloride)".format(superscript_map["-"]),
    "so4": "SO{}{}{} (Sulfate)".format(subscript_map["4"], superscript_map["2"], superscript_map["-"]),
    "co3": "CO{}{}{} (Carbonate)".format(subscript_map["3"], superscript_map["2"], superscript_map["-"]),
    "hco3": "HCO{}{} (Bicarbonate)".format(subscript_map["3"], superscript_map["-"]),
    "no3": "NO{}{} (Nitrate)".format(subscript_map["3"], superscript_map["-"]),
    "ec": "EC (Electrical Conductivity)",
    "ph": "pH (Potential of Hydrogen)"
}


# -----------------------------------------------------------------------------
# CONNECT TO SPREADSHEET FILE AND CREATE DATABASE
# -----------------------------------------------------------------------------
@app.callback(
    Output("CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2", "n_clicks"),
    Output("FILENAME_SPREADSHEET-TAB1_SIDEBAR_CARD2", "children"),
    Output("FILENAME_SPREADSHEET-TAB1_SIDEBAR_CARD2", "className"),
    Output("POPUP_CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2", "is_open"),
    Output("POPUP_CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2", "icon"),
    Output("POPUP_CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2", "header"),
    Output("POPUP_CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2", "children"),
    Output("POPUP_CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2", "headerClassName"),
    Input('CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2', 'n_clicks'),    
    Input('CHOOSE_SPREADSHEET-TAB1_SIDEBAR_CARD2', 'contents'), 
    State('CHOOSE_SPREADSHEET-TAB1_SIDEBAR_CARD2', 'filename')
)
def FUNCTION_CONNECT_TO_SPREADSHEET_TAB1_SIDEBAR_CARD(n, content, filename):
    global table_name
    if n != 0 and content is None:
        result = [
            0,
            "فایلی انتخاب نشده است!",
            "text-danger",
            True,
            None,
            "هشدار",
            "فایل صفحه گسترده‌ای انتخاب نشده است.",
            "popup-notification-header-warning"            
        ]
        return result
    elif n == 0 and content is not None:
        result = [
            0,
            "فایل انتخابی شما: " + filename,
            "text-success",
            False,
            None,
            None,
            None,
            None           
        ]
        return result
    elif n != 0 and content is not None:
        raw_data = read_spreadsheet(contents=content, filename=filename)
        raw_data.sort_values(['mahdodeh_name', 'mahal', 'year', 'month', 'day'], inplace=True)
        raw_data["date"] = raw_data["year"].astype(str) + "-" + raw_data["month"].astype(str) + "-" + raw_data["day"].astype(str)
        raw_data.to_sql(name="RawDATA", con=db, if_exists="replace")
        geoinformation = extract_geoinformation(raw_data).reset_index(drop = True)
        geoinformation.to_sql(name="GeoinformationDATA", con=db, if_exists="replace")
        table_name = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", db)
        result = [
            1,
            "فایل انتخابی شما: " + filename,
            "text-success",
            True,
            None,
            "موفقیت آمیز",
            "پایگاه داده با موفقیت ایجاد شد.",
            "popup-notification-header-success"            
        ]
        return result    
    else:
        result = [
            0,
            "فایلی انتخاب نشده است!",
            "text-danger",
            False,
            None,
            None,
            None,
            None           
        ]
        return result


# -----------------------------------------------------------------------------
# CONNECT TO SERVER DATABASE
# -----------------------------------------------------------------------------
@app.callback(
    Output("CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "n_clicks"),    
    Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "is_open"),
    Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "icon"),
    Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "header"),    
    Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "children"),
    Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "headerClassName"),
    Input("CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "n_clicks")
)
def FUNCTION_CONNECT_TO_SERVER_DATABASE_TAB1_SIDEBAR_CARD1(n):
    if n != 0:
        result = [
            0,
            True,
            None,
            "اطلاعات",
            "این بخش در حال تکمیل می‌باشد.",
            "popup-notification-header-info"            
        ]
        return result
    else:
        result = [
            0,
            False,
            None,
            None,
            None,
            None          
        ]
        return result



# -----------------------------------------------------------------------------
# CONNECT TO EXIST DATABASE
# -----------------------------------------------------------------------------
@app.callback(
    Output("TABLE_RAWDATA-TAB1_SIDEBAR", "children"),
    Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "is_open"),
    Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "icon"),
    Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "header"),
    Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "children"),
    Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "headerClassName"),
    Output('CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1', 'n_clicks'),
    Input('CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1', 'n_clicks'),
)
def CONNECT_TO_EXIST_DATABASE_TAB1_SIDEBAR_CARD1(n):
    if n != 0 and not os.path.exists(db_path):
        result = [
            "NO",
            True,
            None,
            "خطا",
            "هیچ پایگاه داده‌ای موجود نمی‌باشد.",
            "popup-notification-header-danger",
            0
        ]
        return result
    elif n != 0 and os.path.exists(db_path):
        if table_name['name'].str.contains('RawDATA').any() \
            and table_name['name'].str.contains('GeoinformationDATA').any():
                
            result = [
                "OK",
                True,
                None,
                "موفقیت آمیز",
                "پایگاه داده با موفقیت بارگذاری شد.",
                "popup-notification-header-success",
                1
            ]
            return result
        
        else:
            result = [
                "NO",
                True,
                None,
                "خطا",
                "هیچ جدولی در پایگاه داده‌ای موجود نمی‌باشد.",
                "popup-notification-header-danger",
                0
            ]
            return result
                    
    else:
        result = [            
            "NO",
            False,
            None,
            None,
            None,
            None,
            0
        ]
        return result





# -----------------------------------------------------------------------------
# CREATE MAP - TAB1 BODY CONTENT1
# -----------------------------------------------------------------------------
@app.callback(
    Output('MAP-TAB1_BODY_CONTENT1', 'figure'),
    Input("TABLE_RAWDATA-TAB1_SIDEBAR", "children")
)
def FUNCTION_CREATE_MAP_TAB1_BODY_CONTENT1(RAWDATA_TABLE):
    if RAWDATA_TABLE == "NO":        
        return base_map_area_studies(state="NO")
    elif RAWDATA_TABLE == "OK":
        try: 
            data = pd.read_sql_query(sql="SELECT * FROM GeoinformationDATA", con=db)
            mah_code = list(data['mahdodeh_code'].unique())
            geodf, j_file = read_shapfile(
                file_path = AQUIFERS, 
                code_column_name = 'mah_code', 
                selected_code = mah_code
            )
                                    
            fig = px.choropleth_mapbox(
                data_frame=geodf,
                geojson=j_file,
                locations='mah_code',
                opacity=0.3
            )
            
            fig.update_layout(clickmode='event+select')

            for mc in mah_code:
                df = data[data['mahdodeh_code'] == mc]

                fig.add_trace(
                    go.Scattermapbox(
                        lat=df.decimal_degrees_lat,
                        lon=df.decimal_degrees_long,
                        mode='markers',
                        marker=go.scattermapbox.Marker(size=10),
                        text=df['mahal'],
                        hoverinfo='text',
                        hovertemplate='<b>%{text}</b><extra></extra>'
                    )
                )

                fig.update_layout(
                    mapbox={'style': "stamen-terrain",
                            'center': {'lon': 58.8,
                                    'lat': 35.9},
                            'zoom': 6},
                    showlegend=False,
                    hovermode='closest',
                    margin={'l': 0, 'r': 0, 'b': 0, 't': 0},
                    mapbox_accesstoken=token
                )
            return fig        
        except:
            return base_map_area_studies(state="NO")
    else:
        return base_map_area_studies(state="NO")


# -----------------------------------------------------------------------------
# CREATE TABLE - TAB1 BODY CONTENT2
# -----------------------------------------------------------------------------
@app.callback(
    Output('TABLE-TAB1_BODY_CONTENT2', 'data'),
    Output('TABLE-TAB1_BODY_CONTENT2', 'columns'),
    Output('TABLE-TAB1_BODY_CONTENT2', 'tooltip_header'),
    Output('TABLE-TAB1_BODY_CONTENT2', 'tooltip_data'),
    Input("TABLE_RAWDATA-TAB1_SIDEBAR", "children")
)
def FUNCTION_CREATE_TABLE_TAB1_BODY_CONTENT2(RAWDATA_TABLE):
    if RAWDATA_TABLE == "NO":
        result = [
            [{}],
            [],
            {},
            [{}]
        ]
        return result
    elif RAWDATA_TABLE == "OK":
        try:
            df = pd.read_sql_query(sql="SELECT * FROM GeoinformationDATA", con=db)
            df.columns = [TABLE_HEADER_NAME.get(item, item) for item in df.columns]
            df["مساحت محدوده"] = df["مساحت محدوده"].round(2)
            df["مساحت محل"] = df["مساحت محل"].round(2)
            df["طول جغرافیایی"] = df["طول جغرافیایی"].round(2)
            df["عرض جغرافیایی"] = df["عرض جغرافیایی"].round(2)
            df = df.iloc[:,1:]
            
            
            result = [
                df.to_dict('records'),
                [{"name": i, "id": i} for i in df.columns],
                {j: j for j in df.columns},
                [
                    {
                        column: {'value': str(value), 'type': 'markdown'} for column, value in row.items()
                    } for row in df.to_dict('records')
                ]
            ]
            return result        
        except:
            result = [
                [{}],
                [],
                {},
                [{}]
            ]
            return result
    else:
        result = [
            [{}],
            [],
            {},
            [{}]
        ]
        return result



# -----------------------------------------------------------------------------
# UPDATE INFO CARD
# -----------------------------------------------------------------------------
@app.callback(
    Output("INFO_CARD_NUMBER_AQUIFER-TAB1_SIDEBAR_RIGHT_CARD1", "children"),
    Output("INFO_CARD_NUMBER_WELL-TAB1_SIDEBAR_RIGHT_CARD1", "children"),
    Input("TABLE_RAWDATA-TAB1_SIDEBAR", "children")
)
def FUNCTION_UPDATE_INFO_CARD_TAB1_SIDEBAR_RIGHT_CARD1(RAWDATA_TABLE):
    if RAWDATA_TABLE == "OK":
        df = pd.read_sql_query(sql="SELECT * FROM GeoinformationDATA", con=db)
        number_aquifers = list(df["mahdodeh_name"].unique())
        number_mahal = list(df["mahal"].unique())            
        return f'{len(number_aquifers)} عدد', f'{len(number_mahal)} عدد'
    else:
        return "-", "-"