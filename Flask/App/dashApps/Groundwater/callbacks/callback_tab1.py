import os
import sqlite3
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px

from App.dashApps.Groundwater.callbacks.data_analysis import *



def groundwater_callback_tab1(app):
    pass


#     # CASE-DEPENDENT
#     TABLE_HEADER_NAME = {    
#         "Mahdodeh_Name" : "نام محدوده",
#         "Mahdodeh_Code" : "کد محدوده",
#         "Aquifer_Name" : "نام آبخوان",
#         "Well_Type" : "نوع چاه",
#         "Well_Type_Sign" : "علامت نوع چاه",
#         "Well_Name" : "نام چاه",
#         "Well_ID" : "شناسه چاه",
#         "ID" : "شناسه",
#         "Zone_UTM" : "منطقه UTM",
#         "X_UTM" : "طول جغرافیایی - UTM",
#         "Y_UTM" : "عرض جغرافیایی - UTM",
#         "UTM_Grid" : "شبکه UTM",
#         "X_Decimal" : "طول جغرافیایی",
#         "Y_Decimal" : "عرض جغرافیایی",
#         "G.S.L_M.S.L" : "ارتفاع - MSL",
#         "G.S.L_DGPS" : "ارتفاع - DGPS",
#         "G.S.L_DEM_SRTM" : "ارتفاع - SRTM",
#         "Final_Elevation" : "ارتفاع",
#         "Data_Typ" : "نوع داده",  
#     }


#     # -----------------------------------------------------------------------------
#     # CONNECT TO SPREADSHEET FILE AND CREATE DATABASE
#     # -----------------------------------------------------------------------------
#     @app.callback(
#         Output("CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2", "n_clicks"),
#         Output("FILENAME_SPREADSHEET-TAB1_SIDEBAR_CARD2", "children"),
#         Output("FILENAME_SPREADSHEET-TAB1_SIDEBAR_CARD2", "className"),
#         Output("POPUP_CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2", "is_open"),
#         Output("POPUP_CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2", "icon"),
#         Output("POPUP_CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2", "header"),
#         Output("POPUP_CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2", "children"),
#         Output("POPUP_CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2", "headerClassName"),
#         Input('CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2', 'n_clicks'),    
#         Input('CHOOSE_SPREADSHEET-TAB1_SIDEBAR_CARD2', 'contents'), 
#         State('CHOOSE_SPREADSHEET-TAB1_SIDEBAR_CARD2', 'filename')
#     )
#     def FUNCTION_CONNECT_TO_SPREADSHEET_TAB1_SIDEBAR_CARD(n, content, filename):
#         if n != 0 and content is None:
#             result = [
#                 0,
#                 "فایلی انتخاب نشده است!",
#                 "text-danger",
#                 True,
#                 None,
#                 "هشدار",
#                 "فایل صفحه گسترده‌ای انتخاب نشده است.",
#                 "popup-notification-header-warning"            
#             ]
#             return result
#         elif n == 0 and content is not None:
#             result = [
#                 0,
#                 "فایل انتخابی شما: " + filename,
#                 "text-success",
#                 False,
#                 None,
#                 None,
#                 None,
#                 None           
#             ]
#             return result
#         elif n != 0 and content is not None:
#             raw_data = read_multiple_worksheets(contents=content, filename=filename)
#             data, data_aquifer = data_cleansing(
#                 well_info_data_all=raw_data['Info'],
#                 dtw_data_all=raw_data['Depth_To_Water'],
#                 thiessen_data_all=raw_data['Thiessen'],
#                 sc_data_all=raw_data['Storage_Coefficient']
#             )
#             db = sqlite3.connect(database="aquifer_hydrograph.sqlite")
#             data.to_sql(name="RawDATA", con=db, if_exists="replace")
#             data_aquifer.to_sql(name="AquiferDATA", con=db, if_exists="replace")
#             result = [
#                 1,
#                 "فایل انتخابی شما: " + filename,
#                 "text-success",
#                 True,
#                 None,
#                 "موفقیت آمیز",
#                 "پایگاه داده با موفقیت ایجاد شد.",
#                 "popup-notification-header-success"            
#             ]
#             return result    
#         else:
#             result = [
#                 0,
#                 "فایلی انتخاب نشده است!",
#                 "text-danger",
#                 False,
#                 None,
#                 None,
#                 None,
#                 None           
#             ]
#             return result


#     # -----------------------------------------------------------------------------
#     # CONNECT TO SERVER DATABASE
#     # -----------------------------------------------------------------------------
#     @app.callback(
#         Output("CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "n_clicks"),    
#         Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "is_open"),
#         Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "icon"),
#         Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "header"),    
#         Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "children"),
#         Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "headerClassName"),
#         Input("CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1", "n_clicks")
#     )
#     def FUNCTION_CONNECT_TO_SERVER_DATABASE_TAB1_SIDEBAR_CARD1(n):
#         if n != 0:
#             result = [
#                 0,
#                 True,
#                 None,
#                 "اطلاعات",
#                 "این بخش در حال تکمیل می‌باشد.",
#                 "popup-notification-header-info"            
#             ]
#             return result
#         else:
#             result = [
#                 0,
#                 False,
#                 None,
#                 None,
#                 None,
#                 None          
#             ]
#             return result



#     # -----------------------------------------------------------------------------
#     # CONNECT TO EXIST DATABASE
#     # -----------------------------------------------------------------------------
#     @app.callback(
#         Output("TABLE_RAWDATA-TAB1_SIDEBAR", "children"),
#         Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "is_open"),
#         Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "icon"),
#         Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "header"),
#         Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "children"),
#         Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "headerClassName"),
#         Output('CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1', 'n_clicks'),
#         Input('CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1', 'n_clicks'),
#     )
#     def CONNECT_TO_EXIST_DATABASE_TAB1_SIDEBAR_CARD1(n):
#         if n != 0 and not os.path.exists(db_path):
#             result = [
#                 "NO",
#                 True,
#                 None,
#                 "خطا",
#                 "هیچ پایگاه داده‌ای موجود نمی‌باشد.",
#                 "popup-notification-header-danger",
#                 0
#             ]
#             return result
#         elif n != 0 and os.path.exists(db_path):        
#             global db
#             global table_name
#             global RawDATA
#             global GeoInfoData
#             global AquiferDATA
#             db = sqlite3.connect(db_path)
#             table_name = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", db)
#             try:
#                 RawDATA = pd.read_sql_query(sql="SELECT * FROM RawDATA", con=db)
#                 GeoInfoData = extract_geo_info_dataset(RawDATA)
#                 AquiferDATA = pd.read_sql_query(sql="SELECT * FROM AquiferDATA", con=db)
#                 result = [
#                     "OK",
#                     True,
#                     None,
#                     "موفقیت آمیز",
#                     "پایگاه داده با موفقیت بارگذاری شد.",
#                     "popup-notification-header-success",
#                     1
#                 ]
#                 return result
#             except:
#                 result = [
#                     "NO",
#                     True,
#                     None,
#                     "خطا",
#                     "هیچ جدولی در پایگاه داده‌ای موجود نمی‌باشد.",
#                     "popup-notification-header-danger",
#                     0
#                 ]
#                 return result
                        
#         else:
#             result = [            
#                 "NO",
#                 False,
#                 None,
#                 None,
#                 None,
#                 None,
#                 0
#             ]
#             return result


#     # -----------------------------------------------------------------------------
#     # NO MATCHING DATA FOUND TEMPLATE
#     # -----------------------------------------------------------------------------
#     NO_DATABASE_CONNECTION = {
#         "layout": {
#             "xaxis": {"visible": False},
#             "yaxis": {"visible": False},
#             "annotations": [
#                 {
#                     "text": "No Database Connection ...",
#                     "xref": "paper",
#                     "yref": "paper",
#                     "showarrow": False,
#                     "font": {"size": 36}
#                 }
#             ]
#         }
#     }


#     # -----------------------------------------------------------------------------
#     # CREATE MAP - TAB1 BODY CONTENT1
#     # -----------------------------------------------------------------------------
#     @app.callback(
#         Output('MAP-TAB1_BODY_CONTENT1', 'figure'),
#         Input("TABLE_RAWDATA-TAB1_SIDEBAR", "children")
#     )
#     def FUNCTION_CREATE_MAP_TAB1_BODY_CONTENT1(RAWDATA_TABLE):
#         if RAWDATA_TABLE == "NO":        
#             return NO_DATABASE_CONNECTION
#         elif RAWDATA_TABLE == "OK":
#             try:           
#                 mah_code = list(GeoInfoData['Mahdodeh_Code'].unique())
#                 geodf, j_file = read_shapfile(mah_code=mah_code)
                            
#                 fig = px.choropleth_mapbox(
#                     data_frame=geodf,
#                     geojson=j_file,
#                     locations='Mah_Code',
#                     opacity=0.3
#                 )
                
#                 fig.update_layout(clickmode='event+select')

#                 for mc in mah_code:
#                     df = GeoInfoData[GeoInfoData['Mahdodeh_Code'] == mc]

#                     fig.add_trace(
#                         go.Scattermapbox(
#                             lat=df.Y_Decimal,
#                             lon=df.X_Decimal,
#                             mode='markers',
#                             marker=go.scattermapbox.Marker(size=10),
#                             text=df['Well_Name']
#                         )
#                     )

#                     fig.update_layout(
#                         mapbox={'style': "stamen-terrain",
#                                 'center': {'lon': 58.8,
#                                         'lat': 35.9},
#                                 'zoom': 6},
#                         showlegend=False,
#                         hovermode='closest',
#                         margin={'l': 0, 'r': 0, 'b': 0, 't': 0},
#                         mapbox_accesstoken=token
#                     )
#                 return fig        
#             except:
#                 return NO_DATABASE_CONNECTION
#         else:
#             return NO_DATABASE_CONNECTION


#     # -----------------------------------------------------------------------------
#     # CREATE TABLE - TAB1 BODY CONTENT2
#     # -----------------------------------------------------------------------------
#     @app.callback(
#         Output('TABLE-TAB1_BODY_CONTENT2', 'data'),
#         Output('TABLE-TAB1_BODY_CONTENT2', 'columns'),
#         Output('TABLE-TAB1_BODY_CONTENT2', 'tooltip_header'),
#         Output('TABLE-TAB1_BODY_CONTENT2', 'tooltip_data'),
#         Input("TABLE_RAWDATA-TAB1_SIDEBAR", "children")
#     )

#     def FUNCTION_CREATE_TABLE_TAB1_BODY_CONTENT2(RAWDATA_TABLE):
#         if RAWDATA_TABLE == "NO":
#             result = [
#                 [{}],
#                 [],
#                 {},
#                 [{}]
#             ]
#             return result
#         elif RAWDATA_TABLE == "OK":
#             try:
#                 GeoInfoDataTable = GeoInfoData.copy()
#                 GeoInfoDataTable.columns = [ TABLE_HEADER_NAME.get(item, item) for item in GeoInfoDataTable.columns ]
#                 GeoInfoDataTable["طول جغرافیایی"] = GeoInfoDataTable["طول جغرافیایی"].round(2)  
#                 GeoInfoDataTable["عرض جغرافیایی"] = GeoInfoDataTable["عرض جغرافیایی"].round(2)  
                
#                 result = [
#                     GeoInfoDataTable.to_dict('records'),
#                     [{"name": i, "id": i} for i in GeoInfoDataTable.columns],
#                     {j: j for j in GeoInfoDataTable.columns},
#                     [
#                         {
#                             column: {'value': str(value), 'type': 'markdown'} for column, value in row.items()
#                         } for row in GeoInfoDataTable.to_dict('records')
#                     ]
#                 ]
#                 return result        
#             except:
#                 result = [
#                     [{}],
#                     [],
#                     {},
#                     [{}]
#                 ]
#                 return result
#         else:
#             result = [
#                 [{}],
#                 [],
#                 {},
#                 [{}]
#             ]
#             return result



#     # -----------------------------------------------------------------------------
#     # UPDATE INFO CARD
#     # -----------------------------------------------------------------------------
#     @app.callback(
#         Output("INFO_CARD_NUMBER_AQUIFER-TAB1_SIDEBAR_RIGHT_CARD1", "children"),
#         Output("INFO_CARD_NUMBER_WELL-TAB1_SIDEBAR_RIGHT_CARD1", "children"),
#         Input("TABLE_RAWDATA-TAB1_SIDEBAR", "children")
#     )
#     def FUNCTION_UPDATE_INFO_CARD_TAB1_SIDEBAR_RIGHT_CARD1(RAWDATA_TABLE):
#         if RAWDATA_TABLE == "OK":
#             number_aquifers = list(RawDATA["Mahdodeh_Name"].unique())
#             number_wells = list(RawDATA["Well_Name"].unique())            
#             return f'{len(number_aquifers)} عدد', f'{len(number_wells)} عدد'
#         else:
#             return "-", "-"