# --------------------------------------------------------------------------- #
#                                                                             #
#                         IMPORT REQUIREMENT MODULE                           #
#                                                                             #
# --------------------------------------------------------------------------- #

import os
import sqlite3
from attr import dataclass
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px

from App.dashApp.precipitation.callbacks.initial_settings import *


# --------------------------------------------------------------------------- #
#                                                                             #
#                         PRECIPITATION - CALLBACK TAB1                       #
#                                                                             #
# --------------------------------------------------------------------------- #

def precipitation_callback_tab1(app):

    # --------------------------------------------------------------------------- #
    #                                                                             #
    #                         TAB1 - SIDEBAR - LEFT                               #
    #                                                                             #
    # --------------------------------------------------------------------------- #

    # CONNECT TO IP SERVER DATABASE
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
    def FUNCTION_CONNECT_TO_SERVER_DATABASE_TAB1_SIDEBAR_LEFT_CARD1(n):
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

    # CONNECT TO EXIST DATABASE
    # -----------------------------------------------------------------------------

    @app.callback(
        Output("DATABASE_STATE-TAB1", "children"),
        Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "is_open"),
        Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "icon"),
        Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "header"),
        Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "children"),
        Output("POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1", "headerClassName"),
        Output('CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1', 'n_clicks'),
        Input('CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1', 'n_clicks'),
    )
    def CONNECT_TO_EXIST_DATABASE_TAB1_SIDEBAR_LEFT_CARD1(n):
        if n != 0 and not os.path.exists(precipitation_db_path):
            result = [
                "DATABASE NOT EXIST",
                True,
                None,
                "خطا",
                "هیچ پایگاه داده‌ای موجود نمی‌باشد.",
                "popup-notification-header-danger",
                0
            ]
            return result
        elif n != 0 and os.path.exists(precipitation_db_path):
            tables_name = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", precipitation_db)
            if tables_name['name'].str.contains('station').any() \
                and tables_name['name'].str.contains('precipitation').any():
                result = [
                    "DATABASE EXIST",
                    True,
                    None,
                    "موفقیت آمیز",
                    "پایگاه داده با موفقیت بارگذاری شد.",
                    "popup-notification-header-success",
                    0
                ]
                return result
            else:
                result = [
                    "DATABASE EXIST - TABLES NOT EXIST",
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
                "NOT CLICK",
                False,
                None,
                None,
                None,
                None,
                0
            ]
            return result


    # --------------------------------------------------------------------------- #
    #                                                                             #
    #                         TAB1 - SIDEBAR - RIGHT                              #
    #                                                                             #
    # --------------------------------------------------------------------------- #

    # UPDATE INFO CARD
    # -----------------------------------------------------------------------------

    @app.callback(
        Output("INFO_CARD_NUMBER_HOZE6-TAB1_SIDEBAR_RIGHT_CARD1", "children"),
        Output("INFO_CARD_NUMBER_HOZE30-TAB1_SIDEBAR_RIGHT_CARD1", "children"),
        Output("INFO_CARD_NUMBER_MAHDOUDE-TAB1_SIDEBAR_RIGHT_CARD1", "children"),
        Output("INFO_CARD_NUMBER_STATION-TAB1_SIDEBAR_RIGHT_CARD1", "children"),
        Output("INFO_CARD_HIGH_ELEV_STATION-TAB1_SIDEBAR_RIGHT_CARD1", "children"),
        Output("INFO_CARD_LOW_ELEV_STATION-TAB1_SIDEBAR_RIGHT_CARD1", "children"),
        Output("INFO_CARD_OLD_STATION-TAB1_SIDEBAR_RIGHT_CARD1", "children"),
        Output("INFO_CARD_NEW_STATION-TAB1_SIDEBAR_RIGHT_CARD1", "children"),
        Input("DATABASE_STATE-TAB1", "children")
    )
    def FUNCTION_UPDATE_INFO_CARD_TAB1_SIDEBAR_RIGHT_CARD1(DATABASE_STATE):
        if DATABASE_STATE == "DATABASE EXIST":
            selected_station = station[station["stationCode"].isin(data["stationCode"].unique())]
            selected_station["startYear"] = selected_station["startYear"].astype(int)
            number_hoze6 = list(selected_station["drainageArea6"].unique())
            number_hoze30 = list(selected_station["drainageArea30"].unique())
            number_mahdoude = list(selected_station["areaStudyCode"].unique())
            number_station = list(selected_station["stationCode"].unique())
            high_elev_station = selected_station.loc[selected_station["elevation"].idxmax(), :]
            low_elev_station = selected_station.loc[selected_station["elevation"].idxmin(), :]
            old_station = selected_station.loc[selected_station["startYear"].idxmin(), :]
            new_station = selected_station.loc[selected_station["startYear"].idxmax(), :]
            return f'{len(number_hoze6)} عدد', f'{len(number_hoze30)} عدد', f'{len(number_mahdoude)} عدد', f'{len(number_station)} عدد',\
                f'{high_elev_station["stationName"]} - {int(high_elev_station["elevation"])} متر',\
                    f'{low_elev_station["stationName"]} - {int(low_elev_station["elevation"])} متر',\
                        f'{old_station["stationName"]} - {int(old_station["startYear"])}',\
                            f'{new_station["stationName"]} - {int(new_station["startYear"])}'
                
        else:
            return "-", "-", "-", "-", "-", "-", "-", "-"


    # --------------------------------------------------------------------------- #
    #                                                                             #
    #                                  TAB1 - BODY                                #
    #                                                                             #
    # --------------------------------------------------------------------------- #

    # CREATE MAP - TAB1 BODY CONTENT1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('MAP-TAB1_BODY_CONTENT1', 'figure'),
        Input("DATABASE_STATE-TAB1", "children")
    )
    def FUNCTION_CREATE_MAP_TAB1_BODY_CONTENT1(DATABASE_STATE):
        if DATABASE_STATE == "DATABASE EXIST":
            try:
                selected_station = station[station["stationCode"].isin(data["stationCode"].unique())]

                geodf, j_file = read_shapfile(
                    shapefile=MAHDOUDE,
                    column="MahCode",
                    # target=selected_station['areaStudyCode'].unique(),
                    target="all"
                )

                fig = px.choropleth_mapbox(
                    data_frame=geodf,
                    geojson=j_file,
                    locations='MahCode',
                    opacity=0.3,
                    color='Hoze30Name'
                )

                for mc in selected_station['drainageArea30'].unique():
                    df = selected_station[selected_station['drainageArea30'] == mc]
                    fig.add_trace(
                        go.Scattermapbox(
                            lat=df.latDecimalDegrees,
                            lon=df.longDecimalDegrees,
                            mode='markers',
                            marker=go.scattermapbox.Marker(size=10),
                            text=df['stationName'],
                            hoverinfo='text',
                            hovertemplate='<b>%{text}</b><extra></extra>'
                        )
                    )

                fig.update_layout(
                    mapbox={'style': "stamen-terrain",
                            'center': {'lon': 58.8,
                                    'lat': 35.9},
                            'zoom': 5.5},
                    showlegend=False,
                    hovermode='closest',
                    margin={'l': 0, 'r': 0, 'b': 0, 't': 0},
                    mapbox_accesstoken=token,
                    clickmode='event+select'
                )
                return fig
            except:
                return NO_DATABASE_CONNECTION
        else:
            return NO_DATABASE_CONNECTION


    # -----------------------------------------------------------------------------
    # CREATE TABLE - TAB1 BODY CONTENT2
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('TABLE-TAB1_BODY_CONTENT2', 'data'),
        Output('TABLE-TAB1_BODY_CONTENT2', 'columns'),
        Input("DATABASE_STATE-TAB1", "children")
    )
    def FUNCTION_CREATE_TABLE_TAB1_BODY_CONTENT2(DATABASE_STATE):
        if DATABASE_STATE != "DATABASE EXIST":
            result = [
                [{}],
                [],
            ]
            return result
        elif DATABASE_STATE == "DATABASE EXIST":
            try:
                selected_station = station[station["stationCode"].isin(data["stationCode"].unique())]
                selected_station.columns = [STATION_TABLE_FARSI_HEADER_NAME.get(item, item) for item in selected_station.columns]
                selected_station["ارتفاع"] = selected_station["ارتفاع"].round(2)
                selected_station["طول جغرافیایی"] = selected_station["طول جغرافیایی"].round(2)
                selected_station["عرض جغرافیایی"] = selected_station["عرض جغرافیایی"].round(2)
                selected_station = selected_station.iloc[:, [0, 1, 4, 5, 6, 8, 10, 11, 12]]
                result = [
                    selected_station.to_dict('records'),
                    [{"name": i, "id": i} for i in selected_station.columns],
                ]
                return result
            except:
                result = [
                    [{}],
                    []
                ]
                return result
        else:
            result = [
                [{}],
                []
            ]
            return result
