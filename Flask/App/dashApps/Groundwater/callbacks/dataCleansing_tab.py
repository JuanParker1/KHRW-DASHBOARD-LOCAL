import os
import sqlite3
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash.exceptions import PreventUpdate


from App.dashApps.Groundwater.callbacks.config import *



def groundwater_callback_dataCleansing_tab(app):

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


#     # -----------------------------------------------------------------------------
#     # BASE MAP
#     # -----------------------------------------------------------------------------
#     BASE_MAP = go.Figure(
#         go.Scattermapbox(
#             lat=[36.25],
#             lon=[59.55],
#             mode='markers',
#             marker=go.scattermapbox.Marker(size=9),
#             text="شهر مشهد"
#         )
#     )

#     BASE_MAP.update_layout(
#         mapbox={
#             'style': "stamen-terrain",
#             'center': {
#                 'lon': 59.55,
#                 'lat': 36.25
#             },
#             'zoom': 5.5
#         },
#         showlegend=False,
#         hovermode='closest',
#         margin={'l':0, 'r':0, 'b':0, 't':0},
#         autosize=False
#     )



    # -----------------------------------------------------------------------------
    # CHECK DATABASE EXIST
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("DATABASE_STATE-DATA_CLEANSING_TAB", "children"),
        Input('INTERVAL_COMPONENT-DATA_CLEANSING_TAB', 'n_intervals'),
    )
    def FUNCTION_CHECK_DATABASE_EXIST_DATA_CLEANSING_TAB(n):
        if os.path.exists(PATH_DB_GROUNDWATER_RAW_DATA):
            return "OK"                        
        else:
            return "NO"

    # -----------------------------------------------------------------------------
    # SELECT STUDY AREA - DATA CLEANSING TAB - SIDEBAR CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("STUDY_AREA_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1", 'options'),
        Input("DATABASE_STATE-DATA_CLEANSING_TAB", "children")
    )
    def FUNCTION_SELECT_STUDY_AREA_DATA_CLEANSING_TAB_SIDEBAR_CARD_1(DATABASE_STATE):        
        if DATABASE_STATE == "OK":         
            data = pd.read_sql_query(
                sql="SELECT * FROM GROUNDWATER_DATA",
                con=DB_GROUNDWATER_RAW_DATA
            )            
            return [{"label": col, "value": col} for col in data['MAHDOUDE_NAME'].unique()]        
        else:
            return []

    # -----------------------------------------------------------------------------
    # SELECT AQUIFER - DATA CLEANSING TAB - SIDEBAR CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("AQUIFER_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1", 'options'),
        Input("STUDY_AREA_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1", 'value'),
    )
    def FUNCTION_SELECT_AQUIFER_DATA_CLEANSING_TAB_SIDEBAR_CARD_1(STUDY_AREA):
        if STUDY_AREA is not None and len(STUDY_AREA) != 0:
            data = pd.read_sql_query(
                sql="SELECT * FROM GROUNDWATER_DATA",
                con=DB_GROUNDWATER_RAW_DATA
            )
            data = data[data["MAHDOUDE_NAME"].isin(STUDY_AREA)]
            return [{"label": col, "value": col} for col in data['AQUIFER_NAME'].unique()]            
        else:
            return []


    # -----------------------------------------------------------------------------
    # SELECT WELL - DATA CLEANSING TAB - SIDEBAR CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('WELL_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1', 'options'),
        Input('STUDY_AREA_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1', 'value'),
        Input('AQUIFER_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1', 'value')
    )
    def FUNCTION_SELECT_WELL_CLEANSING_TAB_SIDEBAR_CARD_1(STUDY_AREA, AQUIFER):
        if STUDY_AREA is not None and len(STUDY_AREA) != 0 and AQUIFER is not None and len(AQUIFER) != 0:
            data = pd.read_sql_query(
                sql="SELECT * FROM GROUNDWATER_DATA",
                con=DB_GROUNDWATER_RAW_DATA
            )
            data = data[data["MAHDOUDE_NAME"].isin(STUDY_AREA)]
            data = data[data["AQUIFER_NAME"].isin(AQUIFER)]
            return [{"label": col, "value": col} for col in data['LOCATION_NAME'].unique()]            
        else:
            return []


    # # -----------------------------------------------------------------------------
    # # SELECT END YEAR - DATA CLEANSING TAB - SIDEBAR CARD1
    # # -----------------------------------------------------------------------------
    # # FIXME : Problem Duration Of Date
    # @app.callback(
    #     Output('END_YEAR_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1', 'options'),
    #     Input('START_YEAR_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1', 'value')
    # )
    # def FUNCTION_SELECT_END_YEAR_CLEANSING_TAB_SIDEBAR_CARD_1(START):
    #     if START is not None:
    #         return [{'label': '{}'.format(i), 'value': i, 'disabled': False if i >= START else True} for i in range(1370, 1426)]
    #     else:
    #         return []


#     # -----------------------------------------------------------------------------
#     # CREATE MAP - TAB2 SIDEBAR LEFT CARD1
#     # -----------------------------------------------------------------------------
#     # FIXME : Problem With Same Well Name
#     @app.callback(
#         Output('MAP-TAB2_SIDEBAR_LEFT_CARD1', 'figure'),
#         Input('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
#         Input('SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1', 'value')
#     )
#     def FUNCTION_MAP_TAB2_SIDEBAR_LEFT_CARD1(aquifers, wells):
#         if (aquifers is not None) and (len(aquifers) != 0) and (wells is not None) and (len(wells) != 0):
        
#             # Load Required Data
#             data = GeoInfoData[GeoInfoData["Aquifer_Name"].isin(aquifers)]
#             selected_wells = data[data['Well_Name'].isin(wells)]
#             mah_code = list(data["Mahdodeh_Code"].unique())
            
#             # Load Shapefile
#             geodf, j_file = read_shapfile(mah_code=mah_code)
            
#             # Create Map
#             fig = px.choropleth_mapbox(
#                 data_frame=geodf,
#                 geojson=j_file,
#                 locations='Mah_Code',
#                 opacity=0.4
#             )
            
#             fig.add_trace(
#                 go.Scattermapbox(
#                     lat=data.Y_Decimal,
#                     lon=data.X_Decimal,
#                     mode='markers',
#                     marker=go.scattermapbox.Marker(size=8),
#                     text=data["Well_Name"],
#                     hoverinfo='text',
#                     hovertemplate='<span style="color:white;">%{text}</span><extra></extra>'
#                 )
#             )
            
#             fig.add_trace(
#                 go.Scattermapbox(
#                     lat=selected_wells.Y_Decimal,
#                     lon=selected_wells.X_Decimal,
#                     mode='markers',
#                     marker=go.scattermapbox.Marker(
#                         size=10,
#                         color='green'
#                     ),
#                     text=selected_wells["Well_Name"],
#                     hoverinfo='text',
#                     hovertemplate='<b>%{text}</b><extra></extra>'
#                 ), 
#             )
                
#             fig.update_layout(
#                 mapbox = {
#                     'style': "stamen-terrain",
#                     'zoom': 5,
#                     'center': {
#                         'lon': selected_wells.X_Decimal.mean(),
#                         'lat': selected_wells.Y_Decimal.mean()
#                     },
#                 },
#                 showlegend = False,
#                 hovermode='closest',
#                 margin = {'l':0, 'r':0, 'b':0, 't':0}
#             )
                    
#             return fig        
#         else:
#             return BASE_MAP.update_layout(
#                 width=250,
#                 height=250
#             )




    # -----------------------------------------------------------------------------
    # CREATE GRAPH - DATA CLEANSING TAB - SIDEBAR CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GRAPH-DATA_CLEANSING_TAB-BODY', 'figure'),   
        Input('INTERVAL_COMPONENT-DATA_CLEANSING_TAB', 'n_intervals'),
        Input('STUDY_AREA_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1', 'value'),
        Input('AQUIFER_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1', 'value'),
        Input('WELL_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1', 'value'),
        State('TABLE-DATA_CLEANSING_TAB-BODY', 'data')
    )
    def FUNCTION_GRAPH_CLEANSING_TAB_SIDEBAR_CARD_1(N, STUDY_AREA, AQUIFER, WELL, TABLE_DATA):        
        if STUDY_AREA is not None and len(STUDY_AREA) != 0 and\
            AQUIFER is not None and len(AQUIFER) != 0 and\
                WELL is not None and len(WELL) != 0:               
                    print("1", TABLE_DATA)
                    data = pd.read_sql_query(
                        sql="SELECT * FROM GROUNDWATER_DATA",
                        con=DB_GROUNDWATER_RAW_DATA
                    )
                    data = data[data["MAHDOUDE_NAME"].isin(STUDY_AREA)]
                    data = data[data["AQUIFER_NAME"].isin(AQUIFER)]
                    data = data[data["LOCATION_NAME"].isin(WELL)]
                    data = data.sort_values(by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_RAW"]).reset_index(drop=True)

                                
                    # PLOT
                    fig = go.Figure()
                                    
                    for w in WELL:                    
                        df_w = data[data["LOCATION_NAME"] == w]
                                        
                        fig.add_trace(
                            go.Scatter(
                                x=df_w['DATE_PERSIAN_RAW'],
                                y=df_w['WATER_TABLE_RAW'],
                                mode='lines+markers',
                                name=w,
                                showlegend=False
                            )
                        )

                    fig.update_layout(
                        yaxis_title="ارتفاع سطح آب ایستابی - متر",
                        autosize=False,
                        font=dict(
                            family="Tanha-FD",
                            size=16,
                            color="RebeccaPurple"
                        ),
                        xaxis=dict(
                            tickformat="%Y-%m-%d"
                        ),

                        title=dict(
                            text='تراز ماهانه سطح آب زیرزمینی',
                            yanchor="top",
                            y=0.9,
                            xanchor="center",
                            x=0.500
                        )
                    )
                    
                    fig.update_layout(clickmode='event+select')
                    
                    return fig
        else:
            return NO_MATCHING_DATA_FOUND
    
    
    # -----------------------------------------------------------------------------
    # TABLE - DATA CLEANSING TAB - BODY
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('TABLE-DATA_CLEANSING_TAB-BODY', 'data'),
        Output('TABLE-DATA_CLEANSING_TAB-BODY', 'columns'),
        Input('GRAPH-DATA_CLEANSING_TAB-BODY', 'selectedData'),
        Input('INTERVAL_COMPONENT-DATA_CLEANSING_TAB', 'n_intervals'),
        Input('STUDY_AREA_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1', 'value'),
        Input('AQUIFER_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1', 'value'),
        Input('WELL_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1', 'value'),
    )
    def FUNCTION_TABLE_CLEANSING_TAB_SIDEBAR_CARD_1(selectedData, N, STUDY_AREA, AQUIFER, WELL):        
        if STUDY_AREA is not None and len(STUDY_AREA) != 0 and\
            AQUIFER is not None and len(AQUIFER) != 0 and\
                WELL is not None and len(WELL) == 1 and\
                    selectedData is not None:
                                        
                        data = pd.read_sql_query(
                            sql="SELECT * FROM GROUNDWATER_DATA",
                            con=DB_GROUNDWATER_RAW_DATA
                        )
                        
                        data = data[data["MAHDOUDE_NAME"].isin(STUDY_AREA)]
                        data = data[data["AQUIFER_NAME"].isin(AQUIFER)]
                        data = data[data["LOCATION_NAME"].isin(WELL)]
                        data = data.sort_values(by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_RAW"]).reset_index(drop=True).drop(['index'], axis=1)
                                                            
                        x = []
                        curveNumber = []
                        
                        for i in selectedData["points"]:
                            x.append(i['x'])
                            curveNumber.append(i['curveNumber'])

                        df = data[data["DATE_PERSIAN_RAW"].isin(x)]
                                                
                        return [
                            df.to_dict('records'),
                            [{"name": i, "id": i} for i in df.columns]
                        ]
        else:
            return [
                {[]},
                []
            ]


    @app.callback(
        Output('Placeholder', 'children'),
        Output('Update', 'n_clicks'),
        Input('Update', 'n_clicks'),
        Input("Interval", "n_intervals"),
        State('TABLE-DATA_CLEANSING_TAB-BODY', 'data'),
    )
    def FUNCTION_UPDATE_DATABASE(n_clicks, n_intervals, data):
        if n_clicks != 0:
            df = pd.DataFrame(data)
            print(1)
            print(df)
            return [
                "The Database Has Been Updated!",
                0
            ]
        else:
            return [
                "",
                0
            ]
            