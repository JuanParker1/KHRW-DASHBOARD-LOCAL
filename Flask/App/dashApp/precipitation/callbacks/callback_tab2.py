# ----------------------------------------------------------------------------------------------- #
#                                                                                                 #
#                                    IMPORT REQUIREMENT MODULE                                    #
#                                                                                                 #
# ----------------------------------------------------------------------------------------------- #

import os
import sqlite3
import numpy as np
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash.exceptions import PreventUpdate
import dash_dangerously_set_inner_html


from App.dashApp.precipitation.callbacks.initial_settings import *
from App.dashApp.precipitation.layouts.sidebars.sidebar_tab1 import *


# ----------------------------------------------------------------------------------------------- #
#                                                                                                 #
#                                 PRECIPITATION - CALLBACK TAB2                                   #
#                                                                                                 #
# ----------------------------------------------------------------------------------------------- #

def precipitation_callback_tab2(app):

    # --------------------------------------------------------------------------- #
    #                                                                             #
    #                         TAB2 - SIDEBAR - LEFT                               #
    #                                                                             #
    # --------------------------------------------------------------------------- #

    # SELECT HOZE30 - TAB2 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------

    @app.callback(
        Output('SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Input("DATABASE_STATE-TAB1", "children")
    )
    def FUNCTION_SELECT_HOZE30_TAB2_SIDEBAR_LEFT_CARD1(DATABASE_STATE):
        if DATABASE_STATE == "DATABASE EXIST":
            selected_station = station[station["stationCode"].isin(
                data["stationCode"].unique())]
            return [
                {"label": i, "value": i} for i in list(selected_station["drainageArea30"].unique())
            ]
        else:
            return []

    # SELECT MAHDOUDE - TAB2 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------

    @app.callback(
        Output('SELECT_MAHDOUDE-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Input('SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1', 'value')
    )
    def FUNCTION_SELECT_MAHDOUDE_TAB2_SIDEBAR_LEFT_CARD1(HOZE30):
        if HOZE30 is not None and len(HOZE30) != 0:
            selected_station = station[station["stationCode"].isin(
                data["stationCode"].unique())]
            selected_station = selected_station[selected_station["drainageArea30"].isin(
                HOZE30)]
            return [
                {"label": i, "value": i} for i in list(selected_station["areaStudyName"].unique())
            ]
        else:
            return []


    # SELECT STATION - TAB2 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------

    @app.callback(
        Output('SELECT_STATION-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Input('SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_MAHDOUDE-TAB2_SIDEBAR_LEFT_CARD1', 'value')
    )
    def FUNCTION_SELECT_STATION_TAB2_SIDEBAR_LEFT_CARD1(HOZE30, MAHDOUDE):
        if MAHDOUDE is not None and len(MAHDOUDE) != 0 and HOZE30 is not None and len(HOZE30) != 0:
            selected_station = station[station["stationCode"].isin(
                data["stationCode"].unique())]
            selected_station = selected_station[selected_station["areaStudyName"].isin(
                MAHDOUDE)]
            return [
                {"label": i, "value": i} for i in list(selected_station["stationName"].unique())
            ]
        else:
            return []


    # SELECT START YEAR - TAB2 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------

    @app.callback(
        Output('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Output('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Output('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'disabled'),
        Output('SELECT_START_DURATION-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Output('SELECT_START_DURATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Output('SELECT_START_DURATION-TAB2_SIDEBAR_LEFT_CARD1', 'disabled'),
        Input('SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_MAHDOUDE-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_STATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_ANALYSIS-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    )
    def FUNCTION_SELECT_START_YEAR_TAB2_SIDEBAR_LEFT_CARD1(
        HOZE30_SELECTED,
        MAHDOUDE_SELECTED,
        STATION_SELECTED,
        TYPE_YEAR,
        TYPE_ANALYSIS
    ):
        if (STATION_SELECTED is not None) and (len(STATION_SELECTED) != 0) and\
            (MAHDOUDE_SELECTED is not None) and (len(MAHDOUDE_SELECTED) != 0) and\
                (HOZE30_SELECTED is not None) and (len(HOZE30_SELECTED) != 0):
            try:
                
                selected_station = station[
                    (station["drainageArea30"].isin(HOZE30_SELECTED)) &\
                        (station["areaStudyName"].isin(MAHDOUDE_SELECTED)) &\
                            (station["stationName"].isin(STATION_SELECTED))
                ]
                
                unique_st_code = list(selected_station["stationCode"].unique())                
                selected_data = data[data["stationCode"].isin(unique_st_code)]
                
                # DEFINED VARIABLE
                if TYPE_YEAR == "WATER_YEAR":
                    YEAR = "WATERYEAR"
                    MONTH = "WATERMONTH"
                    DAY = "DAY"
                    MONTH_NAME = M_WATERYEAR
                else:
                    YEAR = "YEAR"
                    MONTH = "MONTH"
                    DAY = "DAY"
                    MONTH_NAME = M_SHAMSIYEAR
                
                if TYPE_ANALYSIS == "CURRENTvsPREVIOUS":
                    MAX_YEAR = selected_data[YEAR].max()
                    MIN_YEAR = selected_data[YEAR].min()
                    START_YEAR_OPTIONS = [
                        {
                            'label': '{}'.format(i),
                            'value': i
                        } for i in [MAX_YEAR]
                    ]
                    START_YEAR_VALUE = MAX_YEAR
                    START_DURATION_OPTIONS = [
                        {
                            'label': '{}'.format(i),
                            'value': i
                        } for i in sorted(list(selected_data[YEAR].unique()))[:-1]
                    ]
                    START_DURATION_VALUE = MIN_YEAR
                    return START_YEAR_OPTIONS, START_YEAR_VALUE, True,\
                        START_DURATION_OPTIONS, START_DURATION_VALUE, False
                else:

                    return [], None, True,\
                        [], None, True

            except:
                return [], None, True,\
                    [], None, True
        else:
            return [], None, True,\
                [], None, True
    

    # SELECT END YEAR - TAB2 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Output('SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Output('SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'disabled'),
        Output('SELECT_END_DURATION-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Output('SELECT_END_DURATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Output('SELECT_END_DURATION-TAB2_SIDEBAR_LEFT_CARD1', 'disabled'),
        Input('SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_MAHDOUDE-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_STATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_ANALYSIS-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_DURATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    )
    def FUNCTION_SELECT_END_YEAR_TAB2_SIDEBAR_LEFT_CARD1(
        HOZE30_SELECTED,
        MAHDOUDE_SELECTED,
        STATION_SELECTED,
        TYPE_YEAR,
        START_YEAR,
        TYPE_ANALYSIS,
        START_DURATION
    ):
        if (STATION_SELECTED is not None) and (len(STATION_SELECTED) != 0) and\
            (MAHDOUDE_SELECTED is not None) and (len(MAHDOUDE_SELECTED) != 0) and\
                (HOZE30_SELECTED is not None) and (len(HOZE30_SELECTED) != 0) and\
                    START_YEAR is not None:
            try:
                
                selected_station = station[
                    (station["drainageArea30"].isin(HOZE30_SELECTED)) &\
                        (station["areaStudyName"].isin(MAHDOUDE_SELECTED)) &\
                            (station["stationName"].isin(STATION_SELECTED))
                ]
                
                unique_st_code = list(selected_station["stationCode"].unique())
                selected_data = data[data["stationCode"].isin(unique_st_code)]
                
                # DEFINED VARIABLE
                if TYPE_YEAR == "WATER_YEAR":
                    YEAR = "WATERYEAR"
                    MONTH = "WATERMONTH"
                    DAY = "DAY"
                    MONTH_NAME = M_WATERYEAR
                else:
                    YEAR = "YEAR"
                    MONTH = "MONTH"
                    DAY = "DAY"
                    MONTH_NAME = M_SHAMSIYEAR
                
                if TYPE_ANALYSIS == "CURRENTvsPREVIOUS":
                    MAX_YEAR = selected_data[YEAR].max()
                    END_YEAR_OPTIONS = [
                        {
                            'label': '{}'.format(i),
                            'value': i
                        } for i in [MAX_YEAR]
                    ]
                    END_YEAR_VALUE = MAX_YEAR
                    END_DURATION_OPTIONS = [
                        {
                            'label': '{}'.format(i),
                            'value': i,
                            'disabled': False if i >= START_DURATION else True
                        } for i in sorted(list(selected_data[YEAR].unique()))[:-1]
                    ]
                    END_DURATION_VALUE = sorted(list(selected_data[YEAR].unique()))[-2]
                    
                    return END_YEAR_OPTIONS, END_YEAR_VALUE, True,\
                        END_DURATION_OPTIONS, END_DURATION_VALUE, False
                        
                else:
                    
                    return [], None, True,\
                        [], None, True
            except:
                return [], None, True,\
                    [], None, True
        else:
            return [], None, True,\
                [], None, True


    # SELECT START MONTH - TAB2 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('SELECT_START_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Output('SELECT_START_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Output('SELECT_START_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'disabled'),
        Input('SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_MAHDOUDE-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_STATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    )
    def FUNCTION_SELECT_START_MONTH_TAB2_SIDEBAR_LEFT_CARD1(
        HOZE30_SELECTED, 
        MAHDOUDE_SELECTED, 
        STATION_SELECTED, 
        TYPE_YEAR, 
        START_YEAR
    ):
        if (STATION_SELECTED is not None) and (len(STATION_SELECTED) != 0) and\
            (MAHDOUDE_SELECTED is not None) and (len(MAHDOUDE_SELECTED) != 0) and\
                (HOZE30_SELECTED is not None) and (len(HOZE30_SELECTED) != 0) and\
                    START_YEAR is not None:
            try:
                
                selected_station = station[
                    (station["drainageArea30"].isin(HOZE30_SELECTED)) &\
                        (station["areaStudyName"].isin(MAHDOUDE_SELECTED)) &\
                            (station["stationName"].isin(STATION_SELECTED))
                ]
                
                unique_st_code = list(selected_station["stationCode"].unique())
                selected_data = data[data["stationCode"].isin(unique_st_code)]
                
                if TYPE_YEAR == "WATER_YEAR":
                    selected_data = selected_data[selected_data["WATERYEAR"] == START_YEAR]
                    all_existed_month = sorted(list(selected_data["WATERMONTH"].unique()))
                    all_existed_month = [
                        M_WATERYEAR[i] for i in [x - 1 for x in all_existed_month]
                    ]
                    
                    START_MONTH_OPTIONS = [
                        {
                            'label': '{}'.format(i),
                            'value': i,
                            'disabled': False if i in all_existed_month else True
                        } for i in M_WATERYEAR
                    ]
                    START_MONTH_VALUE = min(sorted(list(selected_data["WATERMONTH"].unique())))
                    
                    return START_MONTH_OPTIONS, M_WATERYEAR[START_MONTH_VALUE - 1], False
                
                else:
                    selected_data = selected_data[selected_data["YEAR"] == START_YEAR]
                    all_existed_month = sorted(list(selected_data["MONTH"].unique()))
                    all_existed_month = [
                        M_SHAMSIYEAR[i] for i in [x - 1 for x in all_existed_month]
                    ]
                    
                    START_MONTH_OPTIONS = [
                        {
                            'label': '{}'.format(i),
                            'value': i,
                            'disabled': False if i in all_existed_month else True
                        } for i in M_SHAMSIYEAR
                    ]
                    START_MONTH_VALUE = min(sorted(list(selected_data["MONTH"].unique())))
                    
                    return START_MONTH_OPTIONS, M_SHAMSIYEAR[START_MONTH_VALUE - 1], False
                
            except:
                return [], None, True
        else:
            return [], None, True
    

    # SELECT END MONTH - TAB2 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('SELECT_END_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Output('SELECT_END_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Output('SELECT_END_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'disabled'),
        Input('SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_MAHDOUDE-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_STATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    )
    def FUNCTION_SELECT_END_MONTH_TAB2_SIDEBAR_LEFT_CARD1(
        HOZE30_SELECTED,
        MAHDOUDE_SELECTED,
        STATION_SELECTED, 
        TYPE_YEAR, 
        START_YEAR, 
        START_MONTH, 
        END_YEAR
    ):
        if (STATION_SELECTED is not None) and (len(STATION_SELECTED) != 0) and\
            (MAHDOUDE_SELECTED is not None) and (len(MAHDOUDE_SELECTED) != 0) and\
                (HOZE30_SELECTED is not None) and (len(HOZE30_SELECTED) != 0) and\
                    START_YEAR is not None and START_MONTH is not None and END_YEAR is not None:
            try:
                selected_station = station[
                    (station["drainageArea30"].isin(HOZE30_SELECTED)) &\
                        (station["areaStudyName"].isin(MAHDOUDE_SELECTED)) &\
                            (station["stationName"].isin(STATION_SELECTED))
                ]
                
                unique_st_code = list(selected_station["stationCode"].unique())
                selected_data = data[data["stationCode"].isin(unique_st_code)]
                
                if TYPE_YEAR == "WATER_YEAR":
                    if END_YEAR == START_YEAR:
                        selected_data = selected_data[selected_data["WATERYEAR"] == END_YEAR]
                        all_existed_month = sorted(list(selected_data["WATERMONTH"].unique()))
                        all_existed_month = [
                            M_WATERYEAR[i] for i in [x - 1 for x in all_existed_month]
                        ]                        
                        all_existed_month = list(
                            set(all_existed_month).difference(
                                M_WATERYEAR[0:M_WATERYEAR.index(START_MONTH)]
                            )
                        )
                        
                        END_MONTH_OPTIONS = [
                            {
                                'label': '{}'.format(i),
                                'value': i,
                                'disabled': False if i in all_existed_month else True
                            } for i in M_WATERYEAR
                        ]
                        END_MONTH_VALUE = max(sorted(list(selected_data["WATERMONTH"].unique())))
                        
                        return END_MONTH_OPTIONS, M_WATERYEAR[END_MONTH_VALUE - 1], False
                    
                    else:
                        selected_data = selected_data[selected_data["WATERYEAR"] == END_YEAR]
                        all_existed_month = sorted(list(selected_data["WATERMONTH"].unique()))
                        all_existed_month = [
                            M_WATERYEAR[i] for i in [x - 1 for x in all_existed_month]
                        ]
                        
                        END_MONTH_OPTIONS = [
                            {
                                'label': '{}'.format(i),
                                'value': i,
                                'disabled': False if i in all_existed_month else True
                            } for i in M_WATERYEAR
                        ]
                        END_MONTH_VALUE = max(sorted(list(selected_data["WATERMONTH"].unique())))
                        return END_MONTH_OPTIONS, M_WATERYEAR[END_MONTH_VALUE - 1], False
                else:
                    if END_YEAR == START_YEAR:
                        selected_data = selected_data[selected_data["YEAR"] == END_YEAR]
                        all_existed_month = sorted(list(selected_data["MONTH"].unique()))
                        all_existed_month = [
                            M_SHAMSIYEAR[i] for i in [x - 1 for x in all_existed_month]
                        ]                        
                        all_existed_month = list(
                            set(all_existed_month).difference(
                                M_SHAMSIYEAR[0:M_SHAMSIYEAR.index(START_MONTH)]
                            )
                        )
                        
                        END_MONTH_OPTIONS = [
                            {
                                'label': '{}'.format(i),
                                'value': i,
                                'disabled': False if i in all_existed_month else True
                            } for i in M_SHAMSIYEAR
                        ]
                        END_MONTH_VALUE = max(sorted(list(selected_data["MONTH"].unique())))
                        
                        return END_MONTH_OPTIONS, M_SHAMSIYEAR[END_MONTH_VALUE - 1], False
                    
                    else:
                        selected_data = selected_data[selected_data["YEAR"] == END_YEAR]
                        all_existed_month = sorted(list(selected_data["MONTH"].unique()))
                        all_existed_month = [
                            M_SHAMSIYEAR[i] for i in [x - 1 for x in all_existed_month]
                        ]
                        
                        END_MONTH_OPTIONS = [
                            {
                                'label': '{}'.format(i),
                                'value': i,
                                'disabled': False if i in all_existed_month else True
                            } for i in M_SHAMSIYEAR
                        ]
                        END_MONTH_VALUE = max(sorted(list(selected_data["MONTH"].unique())))
                        
                        return END_MONTH_OPTIONS, M_SHAMSIYEAR[END_MONTH_VALUE - 1], False
                    
            except:
                return [], None, True
        else:
            return [], None, True



    # SELECT START DAY - TAB2 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('SELECT_START_DAY-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Output('SELECT_START_DAY-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Output('SELECT_START_DAY-TAB2_SIDEBAR_LEFT_CARD1', 'disabled'),
        Input('SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_MAHDOUDE-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_STATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    )
    def FUNCTION_SELECT_START_DAY_TAB2_SIDEBAR_LEFT_CARD1(
        HOZE30_SELECTED, 
        MAHDOUDE_SELECTED, 
        STATION_SELECTED,
        TYPE_YEAR,
        START_YEAR, 
        START_MONTH
    ):
        if (STATION_SELECTED is not None) and (len(STATION_SELECTED) != 0) and\
            (MAHDOUDE_SELECTED is not None) and (len(MAHDOUDE_SELECTED) != 0) and\
                (HOZE30_SELECTED is not None) and (len(HOZE30_SELECTED) != 0) and\
                    START_YEAR is not None and START_MONTH is not None:
            try:
                selected_station = station[
                    (station["drainageArea30"].isin(HOZE30_SELECTED)) &\
                        (station["areaStudyName"].isin(MAHDOUDE_SELECTED)) &\
                            (station["stationName"].isin(STATION_SELECTED))
                ]
                
                unique_st_code = list(selected_station["stationCode"].unique())
                selected_data = data[data["stationCode"].isin(unique_st_code)]
                
                if TYPE_YEAR == "WATER_YEAR":
                    selected_data = selected_data[
                        selected_data["WATERYEAR"] == START_YEAR
                    ]
                    selected_data = selected_data[
                        selected_data["WATERMONTH"] == (M_WATERYEAR.index(START_MONTH) + 1)
                    ]
                    all_existed_day = sorted(list(selected_data["DAY"].unique()))
                    
                    START_DAY_OPTIONS = [
                        {
                            'label': '{}'.format(i), 
                            'value': i, 
                            'disabled': False if i in all_existed_day else True
                        } for i in range(1,32)
                    ]
                    START_DAY_VALUE = min(sorted(list(selected_data["DAY"].unique())))
                    
                    return START_DAY_OPTIONS, START_DAY_VALUE, False
                
                else:
                    selected_data = selected_data[
                        selected_data["YEAR"] == START_YEAR
                    ]
                    selected_data = selected_data[
                        selected_data["MONTH"] == (M_SHAMSIYEAR.index(START_MONTH) + 1)
                    ]
                    all_existed_day = sorted(list(selected_data["DAY"].unique()))
                    
                    START_DAY_OPTIONS = [
                        {
                            'label': '{}'.format(i), 
                            'value': i, 
                            'disabled': False if i in all_existed_day else True
                        } for i in range(1,32)
                    ]
                    START_DAY_VALUE = min(sorted(list(selected_data["DAY"].unique())))
                    
                    return START_DAY_OPTIONS, START_DAY_VALUE, False
                
            except:
                return [], None, True
        else:
            return [], None, True


    # SELECT END DAY - TAB2 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('SELECT_END_DAY-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Output('SELECT_END_DAY-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Output('SELECT_END_DAY-TAB2_SIDEBAR_LEFT_CARD1', 'disabled'),
        Input('SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_MAHDOUDE-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_STATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_DAY-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    )
    def FUNCTION_SELECT_END_DAY_TAB2_SIDEBAR_LEFT_CARD1(
        HOZE30_SELECTED, 
        MAHDOUDE_SELECTED,
        STATION_SELECTED, 
        TYPE_YEAR, 
        START_YEAR,
        START_MONTH, 
        START_DAY, 
        END_YEAR, 
        END_MONTH
    ):
        if (STATION_SELECTED is not None) and (len(STATION_SELECTED) != 0) and\
            (MAHDOUDE_SELECTED is not None) and (len(MAHDOUDE_SELECTED) != 0) and\
                (HOZE30_SELECTED is not None) and (len(HOZE30_SELECTED) != 0) and\
                    START_YEAR is not None and START_MONTH is not None and START_DAY is not None and\
                        END_YEAR is not None and END_MONTH is not None:
            try:
                selected_station = station[
                    (station["drainageArea30"].isin(HOZE30_SELECTED)) &\
                        (station["areaStudyName"].isin(MAHDOUDE_SELECTED)) &\
                            (station["stationName"].isin(STATION_SELECTED))
                ]
                
                unique_st_code = list(selected_station["stationCode"].unique())
                selected_data = data[data["stationCode"].isin(unique_st_code)]
                
                if TYPE_YEAR == "WATER_YEAR":
                    if END_YEAR == START_YEAR and START_MONTH == END_MONTH:
                        selected_data = selected_data[
                            selected_data["WATERYEAR"] == END_YEAR
                        ]
                        selected_data = selected_data[
                            selected_data["WATERMONTH"] == (M_WATERYEAR.index(END_MONTH) + 1)
                        ]
                        all_existed_day = sorted(
                            list(selected_data["DAY"].unique())
                        )
                        all_existed_day = list(
                            set(all_existed_day).difference(list(range(1, START_DAY)))
                        )
                        
                        END_DAY_OPTIONS = [
                            {'label': '{}'.format(i),
                             'value': i, 
                             'disabled': False if i in all_existed_day else True
                            } for i in range(1, 32)
                        ]
                        END_DAY_VALUE = max(
                            all_existed_day
                        )
                        
                        return END_DAY_OPTIONS, END_DAY_VALUE, False
                    
                    else:
                        selected_data = selected_data[
                            selected_data["WATERYEAR"] == END_YEAR
                        ]
                        selected_data = selected_data[
                            selected_data["WATERMONTH"] == (M_WATERYEAR.index(END_MONTH) + 1)
                        ]
                        all_existed_day = sorted(
                            list(selected_data["DAY"].unique())
                        ) 
                        END_DAY_OPTIONS = [
                            {
                                'label': '{}'.format(i), 
                                'value': i, 
                                'disabled': False if i in all_existed_day else True
                            } for i in range(1, 32)
                        ]
                        END_DAY_VALUE = max(
                            all_existed_day
                        )
                        
                        return END_DAY_OPTIONS, END_DAY_VALUE, False
                    
                else:
                    if END_YEAR == START_YEAR and START_MONTH == END_MONTH:
                        selected_data = selected_data[
                            selected_data["YEAR"] == END_YEAR
                        ]
                        selected_data = selected_data[
                            selected_data["MONTH"] == (M_SHAMSIYEAR.index(END_MONTH) + 1)
                        ]
                        all_existed_day = sorted(
                            list(selected_data["DAY"].unique())
                        )
                        all_existed_day = list(
                            set(all_existed_day).difference(list(range(1, START_DAY)))
                        )
                        
                        END_DAY_OPTIONS = [
                            {
                                'label': '{}'.format(i),
                                'value': i,
                                'disabled': False if i in all_existed_day else True
                            } for i in range(1, 32)
                        ]
                        END_DAY_VALUE = max(
                            all_existed_day
                        )
                        
                        return END_DAY_OPTIONS, END_DAY_VALUE, False
                    
                    else:
                        selected_data = selected_data[
                            selected_data["YEAR"] == END_YEAR
                        ]
                        selected_data = selected_data[
                            selected_data["MONTH"] == (M_SHAMSIYEAR.index(END_MONTH) + 1)
                        ]
                        all_existed_day = sorted(
                            list(selected_data["DAY"].unique())
                        )
                        
                        END_DAY_OPTIONS = [
                            {
                                'label': '{}'.format(i),
                                'value': i, 
                                'disabled': False if i in all_existed_day else True
                            } for i in range(1, 32)
                        ]
                        END_DAY_VALUE = max(
                            all_existed_day
                        )
                        
                        return END_DAY_OPTIONS, END_DAY_VALUE, False
                    
            except:
                return [], None, True
        else:
            return [], None, True

    # CREATE MAP - TAB2 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------

    @app.callback(
        Output('MAP-TAB2_SIDEBAR_LEFT_CARD1', 'figure'),
        Input("DATABASE_STATE-TAB1", "children"),
        Input('SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_MAHDOUDE-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_STATION-TAB2_SIDEBAR_LEFT_CARD1', 'value')
    )
    def FUNCTION_MAP_TAB2_SIDEBAR_LEFT_CARD1(
        DATABASE_STATE, 
        HOZE30_SELECTED, 
        MAHDOUDE_SELECTED, 
        STATION_SELECTED
    ):
        if (DATABASE_STATE == "DATABASE EXIST") and\
            (STATION_SELECTED is not None) and (len(STATION_SELECTED) != 0) and\
                (MAHDOUDE_SELECTED is not None) and (len(MAHDOUDE_SELECTED) != 0) and\
                (HOZE30_SELECTED is not None) and (len(HOZE30_SELECTED) != 0):
            try:
                all_station = station[
                    station["stationCode"].isin(data["stationCode"].unique())
                ]
                selected_station = all_station[
                    all_station["stationName"].isin(STATION_SELECTED)
                ]
                selected_mahdoude = list(
                    selected_station["areaStudyCode"].unique()
                )

                geodf, j_file = read_shapfile(
                    shapefile=MAHDOUDE,
                    column="MahCode",
                    target=selected_mahdoude
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
                            'center': {
                                'lat': selected_station.latDecimalDegrees.mean(),
                                'lon': selected_station.longDecimalDegrees.mean()
                            },
                            'zoom': 5.5},
                    showlegend=False,
                    hovermode='closest',
                    margin={'l': 0, 'r': 0, 'b': 0, 't': 0},
                    mapbox_accesstoken=token,
                    clickmode='event+select'
                )
                return fig
            except:
                return BASE_MAP_EMPTY
        else:
            return BASE_MAP_EMPTY


# ----------------------------------------------------------------------------------------------- #
#                                                                                                 #
#                                            TAB2 - BODY                                          #
#                                                                                                 #
# ----------------------------------------------------------------------------------------------- #

    # CONTENT 1 - CARD INFO
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('INFO_CARD_CURRENT_YEAR_VALUE-TAB2_BODY_CONTENT1', 'children'),
        Output('INFO_CARD_PREVIOUS_YEAR_VALUE-TAB2_BODY_CONTENT1', 'children'),
        Output('INFO_CARD_MEAN_VALUE-TAB2_BODY_CONTENT1', 'children'),
        Output('INFO_CARD_MAX_VALUE-TAB2_BODY_CONTENT1', 'children'),
        Output('INFO_CARD_MIN_VALUE-TAB2_BODY_CONTENT1', 'children'),
        Input('SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_MAHDOUDE-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_STATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_ANALYSIS-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TIME_STEP-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_DURATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_DURATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_DAY-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_DAY-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    )
    def FUNCTION_UPDATE_INFO_CARD_TAB2_BODY_CONTENT1(
        HOZE30_SELECTED,
        MAHDOUDE_SELECTED,
        STATION_SELECTED,
        TYPE_ANALYSIS,
        TIME_STEP,
        TYPE_YEAR,
        START_DURATION, 
        END_DURATION,
        START_YEAR, 
        START_MONTH,
        START_DAY,
        END_YEAR,
        END_MONTH,
        END_DAY
    ):
        if (HOZE30_SELECTED is not None) and (len(HOZE30_SELECTED) != 0) and\
            (MAHDOUDE_SELECTED is not None) and (len(MAHDOUDE_SELECTED) != 0) and\
                (STATION_SELECTED is not None) and (len(STATION_SELECTED) != 0) and\
                    (START_DURATION is not None) and (END_DURATION is not None) and\
                        (START_YEAR is not None) and (START_MONTH is not None) and\
                            (START_DAY is not None) and (END_YEAR is not None) and\
                                (END_MONTH is not None) and (END_DAY is not None):
            try:
                # LOAD DATA: ----------------------------------------------------------------------
                
                # DEFINED VARIABLE
                if TYPE_YEAR == "WATER_YEAR":
                    YEAR = "WATERYEAR"
                    MONTH = "WATERMONTH"
                    DAY = "DAY"
                    MONTH_NAME = M_WATERYEAR
                else:
                    YEAR = "YEAR"
                    MONTH = "MONTH"
                    DAY = "DAY"
                    MONTH_NAME = M_SHAMSIYEAR

                # LOAD STATIONS
                selected_station = station[
                    (station["drainageArea30"].isin(HOZE30_SELECTED)) &\
                        (station["areaStudyName"].isin(MAHDOUDE_SELECTED)) &\
                            (station["stationName"].isin(STATION_SELECTED))
                ]
                
                # LOAD DATA
                unique_st_code = list(selected_station["stationCode"].unique())
                selected_data = data[data["stationCode"].isin(unique_st_code)]
                
                if "CURRENTvsPREVIOUS" in TYPE_ANALYSIS:
                    
                    PREVIOUS_YEAR = sorted(list(selected_data[YEAR].unique()))[-2]
                    
                    df_cp = selected_data.copy()
                    
                    df_cp = df_cp.loc[
                        ~((df_cp[MONTH] < (MONTH_NAME.index(START_MONTH) + 1)))
                    ]
                    df_cp = df_cp.loc[
                        ~((df_cp[MONTH] > (MONTH_NAME.index(END_MONTH) + 1)))
                    ]
                    df_cp = df_cp.loc[
                        ~((df_cp[MONTH] == (MONTH_NAME.index(START_MONTH) + 1)) &\
                            (df_cp[DAY] < START_DAY))
                    ]
                    df_cp = df_cp.loc[
                        ~((df_cp[MONTH] == (MONTH_NAME.index(END_MONTH) + 1)) &\
                            (df_cp[DAY] > END_DAY))
                    ]
                    
                    pc_txt = f"<p style='text-align:center; margin:0; color:blue;'>\
                        {START_YEAR}</p><table style='width:100%'>"
                    pp_txt = f"<p style='text-align:center; margin:0; color:blue;'>\
                        {PREVIOUS_YEAR}</p><table style='width:100%'>"
                    phm_txt = f"<p style='text-align:center; margin:0; color:blue;'>\
                        {END_DURATION}  -  {START_DURATION}</p><table style='width:100%'>"
                    phmx_txt = f"<p style='text-align:center; margin:0; color:blue;'>\
                        {END_DURATION}  -  {START_DURATION}</p><table style='width:100%'>"
                    phmn_txt = f"<p style='text-align:center; margin:0; color:blue;'>\
                        {END_DURATION}  -  {START_DURATION}</p><table style='width:100%'>"
                    
                    if TIME_STEP == "TIMESTEP_YEAR":
                        # YEARLY ANALYSIS
                        for st in df_cp["stationCode"].unique():
                            df = df_cp[df_cp["stationCode"] == st]
                            df.reset_index(inplace=True, drop=True)
                                                
                            df_year = pd.pivot_table(
                                df,
                                values=['JAM_BARAN'],
                                index=[YEAR],
                                aggfunc=np.sum
                            ).reset_index()
                            
                            st_name = selected_station.loc[
                                selected_station["stationCode"] == st, "stationName"
                            ].values[0]
                            
                            # CURRENT YEAR DATA
                            current_year_data = df_year[df_year[YEAR] == START_YEAR]
                            current_year_data.reset_index(inplace=True, drop=True)
                            
                            # PREVIOUS YEAR DATA
                            previous_year_data = df_year[df_year[YEAR] == PREVIOUS_YEAR]
                            previous_year_data.reset_index(inplace=True, drop=True)
                            
                            # HISTORICAL DATA 
                            historical_data = df_year[
                                (df_year[YEAR] >= START_DURATION) & (df_year[YEAR] <= END_DURATION)
                            ]
                            historical_data.reset_index(inplace=True, drop=True)
                            
                            # CURRENT YEAR
                            pc_value = round(current_year_data['JAM_BARAN'].mean(skipna = True), 1)
                            pc_txt = pc_txt + f'''
                                    <tr>
                                        <td style="text-align: right;">{st_name}</td>
                                        <td style="text-align: left; color: red">{pc_value} میلیمتر</td>
                                    </tr>
                            '''
                            # PREVIOUS YEAR
                            pp_value = round(previous_year_data['JAM_BARAN'].mean(skipna = True), 1)
                            pp_txt = pp_txt + f'''
                                    <tr>
                                        <td style="text-align: right;">{st_name}</td>
                                        <td style="text-align: left; color: red">{pp_value} میلیمتر</td>
                                    </tr>
                            '''
                            
                            # HISTORICAL MEAN
                            phm_value = round(historical_data['JAM_BARAN'].mean(skipna = True), 1)
                            phm_txt = phm_txt + f'''
                                    <tr>
                                        <td style="text-align: right;">{st_name}</td>
                                        <td style="text-align: left; color: red">{phm_value} میلیمتر</td>
                                    </tr>
                            '''
                             
                            # HISTORICAL MAX
                            phmx_index = historical_data["JAM_BARAN"].idxmax(axis=1, skipna=True)
                            phmx_value = round(historical_data.at[phmx_index, 'JAM_BARAN'], 1)
                            phmx_year = str(historical_data.at[phmx_index, YEAR])
                            phmx_txt = phmx_txt + f'''
                                    <tr>
                                        <td style="text-align: right;">{st_name}</td>
                                        <td style="text-align: left; color: red">{phmx_value} میلیمتر</td>
                                        <td style="text-align: left; color: green">{phmx_year}</td>
                                    </tr>
                            '''
                            
                            # HISTORICAL MIN
                            phmn_index = historical_data["JAM_BARAN"].idxmin(axis=1, skipna=True)
                            phmn_value = round(historical_data.at[phmn_index, 'JAM_BARAN'], 1)
                            phmn_year = str(historical_data.at[phmn_index, YEAR])
                            phmn_txt = phmn_txt + f'''
                                    <tr>
                                        <td style="text-align: right;">{st_name}</td>
                                        <td style="text-align: left; color: red">{phmn_value} میلیمتر</td>
                                        <td style="text-align: left; color: green">{phmn_year}</td>
                                    </tr>
                            '''

                        pc_txt = pc_txt + "</table>"
                        pp_txt = pp_txt + "</table>"
                        phm_txt = phm_txt + "</table>"
                        phmx_txt = phmx_txt + "</table>"
                        phmn_txt = phmn_txt + "</table>"
                        
                        result = [
                            dash_dangerously_set_inner_html.DangerouslySetInnerHTML(pc_txt),
                            dash_dangerously_set_inner_html.DangerouslySetInnerHTML(pp_txt),
                            dash_dangerously_set_inner_html.DangerouslySetInnerHTML(phm_txt),
                            dash_dangerously_set_inner_html.DangerouslySetInnerHTML(phmx_txt),
                            dash_dangerously_set_inner_html.DangerouslySetInnerHTML(phmn_txt),
                        ]
                        
                    else:
                        result = [
                            "-",
                            "-",
                            "-",
                            "-",
                            "-"
                        ]
                else:
                    result = [
                        "-",
                        "-",
                        "-",
                        "-",
                        "-"
                    ]
                
                return result
                
            except:
                result = [
                    "-",
                    "-",
                    "-",
                    "-",
                    "-"
                ]
                return result
            
        else:
            result = [
                "-",
                "-",
                "-",
                "-",
                "-"
            ]
            return result
        
    


    # CONTENT 2 - PLOT
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GRAPH1-TAB2_BODY_CONTENT2', 'figure'),
        Output('GRAPH2-TAB2_BODY_CONTENT2', 'figure'),
        Output('GRAPH3-TAB2_BODY_CONTENT2', 'figure'),
        Input('SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_MAHDOUDE-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_STATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_ANALYSIS-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TIME_STEP-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_DURATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_DURATION-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_DAY-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_MONTH-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_DAY-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    )
    def FUNCTION_UPDATE_INFO_CARD_TAB2_BODY_CONTENT1(
        HOZE30_SELECTED,
        MAHDOUDE_SELECTED,
        STATION_SELECTED,
        TYPE_ANALYSIS,
        TIME_STEP,
        TYPE_YEAR,
        START_DURATION, 
        END_DURATION,
        START_YEAR, 
        START_MONTH,
        START_DAY,
        END_YEAR,
        END_MONTH,
        END_DAY
    ):
        if (HOZE30_SELECTED is not None) and (len(HOZE30_SELECTED) != 0) and\
            (MAHDOUDE_SELECTED is not None) and (len(MAHDOUDE_SELECTED) != 0) and\
                (STATION_SELECTED is not None) and (len(STATION_SELECTED) != 0) and\
                    (START_DURATION is not None) and (END_DURATION is not None) and\
                        (START_YEAR is not None) and (START_MONTH is not None) and\
                            (START_DAY is not None) and (END_YEAR is not None) and\
                                (END_MONTH is not None) and (END_DAY is not None):
            try:
                # LOAD DATA: ----------------------------------------------------------------------
                
                # DEFINED VARIABLE
                if TYPE_YEAR == "WATER_YEAR":
                    YEAR = "WATERYEAR"
                    MONTH = "WATERMONTH"
                    DAY = "DAY"
                    MONTH_NAME = M_WATERYEAR
                else:
                    YEAR = "YEAR"
                    MONTH = "MONTH"
                    DAY = "DAY"
                    MONTH_NAME = M_SHAMSIYEAR

                # LOAD STATIONS
                selected_station = station[
                    (station["drainageArea30"].isin(HOZE30_SELECTED)) &\
                        (station["areaStudyName"].isin(MAHDOUDE_SELECTED)) &\
                            (station["stationName"].isin(STATION_SELECTED))
                ]
                                
                # LOAD DATA
                unique_st_code = list(selected_station["stationCode"].unique())
                selected_data = data[data["stationCode"].isin(unique_st_code)]
                
                if "CURRENTvsPREVIOUS" in TYPE_ANALYSIS:
                    
                    PREVIOUS_YEAR = sorted(list(selected_data[YEAR].unique()))[-2]
                    
                    df_cp = selected_data.copy()
                    
                    df_cp = df_cp.loc[
                        ~((df_cp[MONTH] < (MONTH_NAME.index(START_MONTH) + 1)))
                    ]
                    df_cp = df_cp.loc[
                        ~((df_cp[MONTH] > (MONTH_NAME.index(END_MONTH) + 1)))
                    ]
                    df_cp = df_cp.loc[
                        ~((df_cp[MONTH] == (MONTH_NAME.index(START_MONTH) + 1)) &\
                            (df_cp[DAY] < START_DAY))
                    ]
                    df_cp = df_cp.loc[
                        ~((df_cp[MONTH] == (MONTH_NAME.index(END_MONTH) + 1)) &\
                            (df_cp[DAY] > END_DAY))
                    ]
                    
                    if TIME_STEP == "TIMESTEP_YEAR":
                        # YEARLY ANALYSIS
                        df_year = pd.pivot_table(
                            df_cp,
                            values=['JAM_BARAN'],
                            index=["stationCode", YEAR],
                            aggfunc=np.sum
                        ).reset_index()
                        
                        df_year = df_year.merge(
                            selected_station[["stationCode", "stationName"]], 
                            on="stationCode",
                            how='left'
                        )
                        
                        print(df_year)
                        
                        fig_1 = px.box(
                            df_year,
                            x="stationName", 
                            y="JAM_BARAN"
                        )
                        
                        fig_1.update_traces(boxmean=True, selector=dict(type='box'))
                        
                        
#                 fig.update_layout(
#                     margin={'l': 3, 'r': 3},
#                     xaxis_title="تاریخ",
#                     yaxis_title="ارتفاع سطح آب ایستابی - متر",
#                     autosize=False,
#                     font=dict(
#                         family="Tanha-FD",
#                         size=16,
#                         color="RebeccaPurple"
#                     ),
#                     xaxis=dict(
#                         tickformat="%Y-%m"
#                     ),
#                     legend=dict(
#                         orientation="h",
#                         yanchor="bottom",
#                         y=1.005,
#                         xanchor="left",
#                         x=0.000
#                     ),
#                     title=dict(
#                         text='متوسط تراز ماهانه (روز پانزدهم) تعدیل شده سطح آب زیرزمینی در آبخوان',
#                         yanchor="top",
#                         y=0.95,
#                         xanchor="center",
#                         x=0.500
#                     )
#                 )
                        
                        
                        
                        
                        
                        
                        # for st in df_cp["stationCode"].unique():
                        #     df = df_cp[df_cp["stationCode"] == st]
                        #     df.reset_index(inplace=True, drop=True)
                                                
                        #     df_year = pd.pivot_table(
                        #         df,
                        #         values=['JAM_BARAN'],
                        #         index=[YEAR],
                        #         aggfunc=np.sum
                        #     ).reset_index()
                            
                        #     st_name = selected_station.loc[
                        #         selected_station["stationCode"] == st, "stationName"
                        #     ].values[0]
                            
                        #     # CURRENT YEAR DATA
                        #     current_year_data = df_year[df_year[YEAR] == START_YEAR]
                        #     current_year_data.reset_index(inplace=True, drop=True)
                            
                        #     # PREVIOUS YEAR DATA
                        #     previous_year_data = df_year[df_year[YEAR] == PREVIOUS_YEAR]
                        #     previous_year_data.reset_index(inplace=True, drop=True)
                            
                        #     # HISTORICAL DATA 
                        #     historical_data = df_year[
                        #         (df_year[YEAR] >= START_DURATION) & (df_year[YEAR] <= END_DURATION)
                        #     ]
                        #     historical_data.reset_index(inplace=True, drop=True)
                            
                        #     # CURRENT YEAR
                        #     pc_value = round(current_year_data['JAM_BARAN'].mean(skipna = True), 1)
                        #     pc_txt = pc_txt + f'''
                        #             <tr>
                        #                 <td style="text-align: right;">{st_name}</td>
                        #                 <td style="text-align: left; color: red">{pc_value} میلیمتر</td>
                        #             </tr>
                        #     '''
                        #     # PREVIOUS YEAR
                        #     pp_value = round(previous_year_data['JAM_BARAN'].mean(skipna = True), 1)
                        #     pp_txt = pp_txt + f'''
                        #             <tr>
                        #                 <td style="text-align: right;">{st_name}</td>
                        #                 <td style="text-align: left; color: red">{pp_value} میلیمتر</td>
                        #             </tr>
                        #     '''
                            
                        #     # HISTORICAL MEAN
                        #     phm_value = round(historical_data['JAM_BARAN'].mean(skipna = True), 1)
                        #     phm_txt = phm_txt + f'''
                        #             <tr>
                        #                 <td style="text-align: right;">{st_name}</td>
                        #                 <td style="text-align: left; color: red">{phm_value} میلیمتر</td>
                        #             </tr>
                        #     '''
                             
                        #     # HISTORICAL MAX
                        #     phmx_index = historical_data["JAM_BARAN"].idxmax(axis=1, skipna=True)
                        #     phmx_value = round(historical_data.at[phmx_index, 'JAM_BARAN'], 1)
                        #     phmx_year = str(historical_data.at[phmx_index, YEAR])
                        #     phmx_txt = phmx_txt + f'''
                        #             <tr>
                        #                 <td style="text-align: right;">{st_name}</td>
                        #                 <td style="text-align: left; color: red">{phmx_value} میلیمتر</td>
                        #                 <td style="text-align: left; color: green">{phmx_year}</td>
                        #             </tr>
                        #     '''
                            
                        #     # HISTORICAL MIN
                        #     phmn_index = historical_data["JAM_BARAN"].idxmin(axis=1, skipna=True)
                        #     phmn_value = round(historical_data.at[phmn_index, 'JAM_BARAN'], 1)
                        #     phmn_year = str(historical_data.at[phmn_index, YEAR])
                        #     phmn_txt = phmn_txt + f'''
                        #             <tr>
                        #                 <td style="text-align: right;">{st_name}</td>
                        #                 <td style="text-align: left; color: red">{phmn_value} میلیمتر</td>
                        #                 <td style="text-align: left; color: green">{phmn_year}</td>
                        #             </tr>
                        #     '''

                        # pc_txt = pc_txt + "</table>"
                        # pp_txt = pp_txt + "</table>"
                        # phm_txt = phm_txt + "</table>"
                        # phmx_txt = phmx_txt + "</table>"
                        # phmn_txt = phmn_txt + "</table>"
                        
                        result = [
                            fig_1,
                            NO_MATCHING_DATA_FOUND,
                            NO_MATCHING_DATA_FOUND,
                        ]
                        
                    else:
                        result = [
                            NO_MATCHING_DATA_FOUND,
                            NO_MATCHING_DATA_FOUND,
                            NO_MATCHING_DATA_FOUND,
                        ]
                else:
                    result = [
                        NO_MATCHING_DATA_FOUND,
                        NO_MATCHING_DATA_FOUND,
                        NO_MATCHING_DATA_FOUND,
                    ]
                return result
                
            except:
                result = [
                    NO_MATCHING_DATA_FOUND,
                    NO_MATCHING_DATA_FOUND,
                    NO_MATCHING_DATA_FOUND,
                ]
                return result
            
        else:
            result = [
                NO_MATCHING_DATA_FOUND,
                NO_MATCHING_DATA_FOUND,
                NO_MATCHING_DATA_FOUND,
            ]
            return result

                # # TIME SLICING
                # selected_data = selected_data.loc[(selected_data[YEAR] >= START_YEAR)]
                # selected_data = selected_data.loc[~((selected_data[YEAR] == START_YEAR) & (selected_data[MONTH] < (MONTH_NAME.index(START_MONTH) + 1)))]
                # selected_data = selected_data.loc[~((selected_data[YEAR] == START_YEAR) & (selected_data[MONTH] == (MONTH_NAME.index(START_MONTH) + 1)) & (selected_data[DAY] < START_DAY))]
                # selected_data = selected_data.loc[(selected_data[YEAR] <= END_YEAR)]
                # selected_data = selected_data.loc[~((selected_data[YEAR] == END_YEAR) & (selected_data[MONTH] > (MONTH_NAME.index(END_MONTH) + 1)))]
                # selected_data = selected_data.loc[~((selected_data[YEAR] == END_YEAR) & (selected_data[MONTH] == (MONTH_NAME.index(END_MONTH) + 1)) & (selected_data[DAY] > END_DAY))]
                # selected_data.reset_index(inplace=True, drop=True)

                # # MAX
                # pmx_index = df_year["JAM_BARAN"].idxmax(axis=1, skipna=True)
                # pmx_value = df.at[pmx_index, 'JAM_BARAN']
                # pmx_year = str(df.at[pmx_index, 'YEAR']).zfill(4)
                # pmx_month = str(df.at[pmx_index, 'MONTH']).zfill(2)
                # pmx_day = str(df.at[pmx_index, 'DAY']).zfill(2)
                # pmx_houre = str(df.at[pmx_index, 'HOURE']).zfill(2)
                # pmx_minute = str(df.at[pmx_index, 'MINUTE']).zfill(2)
                # pmx_txt = pmx_txt + f'''
                #         <tr>
                #             <td style="text-align: right;">{st_name}</td>
                #             <td style="text-align: right; color: red">{pmx_value} میلیمتر</td>
                #             <td style="text-align: left; color: green">{pmx_houre}:{pmx_minute}</td>
                #             <td style="text-align: left; color: green">{pmx_year}/{pmx_month}/{pmx_day}</td>
                #         </tr>
                #     ''' 



#     # -----------------------------------------------------------------------------
#     #
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


#     # -----------------------------------------------------------------------------
#     # CREATE GRAPH - TAB2 BODY CONTENT1
#     # -----------------------------------------------------------------------------
#     @app.callback(
#         Output('GRAPH-TAB2_BODY_CONTENT1', 'figure'),
#         Input('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
#         Input('SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
#         Input('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
#         Input('SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value')
#     )
#     def FUNCTION_GRAPH_TAB2_BODY_CONTENT1(aquifers, wells, start, end):
#         if (aquifers is not None) and (len(aquifers) != 0) \
#             and (wells is not None) and (len(wells) != 0) \
#                 and (start is not None) and (end is not None):
#                     data = RawDATA[RawDATA["Aquifer_Name"].isin(aquifers)]
#                     data = data[data["Well_Name"].isin(wells)]
#                     data = data[data['year_Date_Persian'] >= start]
#                     data = data[data['year_Date_Persian'] <= end]

#                     # PLOT
#                     fig = go.Figure()

#                     for well in wells:
#                         df_well = data[data["Well_Name"] == well]

#                         fig.add_trace(
#                             go.Scatter(
#                                 x=df_well['Date_Persian'],
#                                 y=df_well['Well_Head'],
#                                 mode='lines+markers',
#                                 name=well
#                             )
#                         )

#                     fig.update_layout(
#                         margin={'l': 3, 'r': 3},
#                         xaxis_title="تاریخ",
#                         yaxis_title="ارتفاع سطح آب ایستابی - متر",
#                         autosize=False,
#                         font=dict(
#                             family="Tanha-FD",
#                             size=16,
#                             color="RebeccaPurple"
#                         ),
#                         xaxis=dict(
#                             tickformat="%Y-%m"
#                         ),
#                         legend=dict(
#                             orientation="h",
#                             yanchor="bottom",
#                             y=1.005,
#                             xanchor="left",
#                             x=0.000
#                         ),
#                         title=dict(
#                             text='تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی',
#                             yanchor="top",
#                             y=0.95,
#                             xanchor="center",
#                             x=0.500
#                         )
#                     )
#                     return fig
#         else:
#             return NO_MATCHING_DATA_FOUND


#     # -----------------------------------------------------------------------------
#     # WELL INFORMATION - TAB2 SIDEBAR RIGHT CARD1
#     # -----------------------------------------------------------------------------
#     @app.callback(
#         Output('IMG_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'src'),
#         Output('NAME_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),
#         Output('ID_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),
#         Output('AQUIFER_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),
#         Output('LONG_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),
#         Output('LAT_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),
#         Output('ELEV_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),
#         Output('START_DATE_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),
#         Output('END_DATE_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),
#         Output('TAB_2_SIDEBAR_RIGHT', 'hidden'),
#         Output('TAB_2_SIDEBAR_RIGHT', 'className'),
#         Output('TAB_2_BODY', 'className'),
#         Input('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
#         Input('SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1', 'value')
#     )
#     def FUNCTION_WELL_INFORMATION_TAB2_SIDEBAR_RIGHT_CARD1(aquifers, wells):
#         if (aquifers is not None) and (len(aquifers) != 0) \
#             and (wells is not None) and (len(wells) != 0):
#                 if (len(aquifers) == 1) and (len(wells) == 1):
#                     data = RawDATA[RawDATA["Aquifer_Name"].isin(aquifers)]
#                     data = data[data["Well_Name"].isin(wells)]
#                     data['Date_Gregorian'] = pd.to_datetime(data['Date_Gregorian'])
#                     data.reset_index(inplace = True)
#                     # Img OW
#                     if aquifers[0] == "جوین":
#                         Img_OW = base64.b64encode(
#                             open('./App/static/precipitation/images/ow1.png', 'rb').read()
#                         )
#                         Img_OW_SRC = 'data:image/png;base64,{}'.format(Img_OW.decode())
#                     else:
#                         Img_OW = base64.b64encode(
#                             open('./App/static/precipitation/images/ow2.png', 'rb').read()
#                         )
#                         Img_OW_SRC = 'data:image/png;base64,{}'.format(Img_OW.decode())

#                     # Para
#                     ID = str(data['ID'].values[0])
#                     LAT = str(data['X_UTM'].values[0])
#                     LONG = str(data['Y_UTM'].values[0])
#                     ELEV = str(data['Final_Elevation'].values[0])
#                     START_DATE = str(data['year_Date_Persian'].values[data["Date_Gregorian"].idxmin()])
#                     END_DATE = str(data['year_Date_Persian'].values[data["Date_Gregorian"].idxmax()])


#                     result = [
#                         Img_OW_SRC,
#                         wells[0],
#                         "شناسه: " + ID,
#                         "آبخوان: " + aquifers[0],
#                         "طول جغرافیایی: " + LAT,
#                         "عرض جغرافیایی: " + LONG,
#                         "ارتفاع: " + ELEV + " متر",
#                         "سال شروع دوره آماری: " + START_DATE,
#                         "سال پایان دوره آماری: " + END_DATE,
#                         False,
#                         "right-sidebar",
#                         'my-body pt-2'
#                     ]

#                     return result
#                 else:

#                     Img_OW = base64.b64encode(
#                         open('./App/static/precipitation/images/placeholder.png', 'rb').read()
#                     )  # EDITPATH

#                     result = [
#                         'data:image/png;base64,{}'.format(Img_OW.decode()),
#                         "نام چاه مشاهده‌ای",
#                         "شناسه چاه مشاهده‌ای",
#                         "نام آبخوان",
#                         "طول جغرافیایی",
#                         "عرض جغرافیایی",
#                         "ارتفاع",
#                         "سال شروع دوره آماری",
#                         "سال پایان دوره آماری",
#                         True,
#                         "tab2-right-sidebar-hidden",
#                         'tab2-right-sidebar-hidden-my-body pt-2'
#                     ]

#                     return result

#         else:

#             Img_OW = base64.b64encode(
#                 open('./App/static/precipitation/images/placeholder.png', 'rb').read()
#             )  # EDITPATH

#             result = [
#                 'data:image/png;base64,{}'.format(Img_OW.decode()),
#                 "نام چاه مشاهده‌ای",
#                 "شناسه چاه مشاهده‌ای",
#                 "نام آبخوان",
#                 "طول جغرافیایی",
#                 "عرض جغرافیایی",
#                 "ارتفاع",
#                 "سال شروع دوره آماری",
#                 "سال پایان دوره آماری",
#                 True,
#                 "tab2-right-sidebar-hidden",
#                 'tab2-right-sidebar-hidden-my-body pt-2'
#             ]

#             return result


#     # -----------------------------------------------------------------------------
#     # TABLE - TAB2 BODY CONTENT2
#     # -----------------------------------------------------------------------------
#     @app.callback(
#         Output('TABLE-TAB2_BODY_CONTENT2', 'data'),
#         Output('TABLE-TAB2_BODY_CONTENT2', 'columns'),
#         Output('TABLE_HEADER-TAB2_BODY_CONTENT2', 'children'),
#         Output('STATE_TABLE_DOWNLOAD_BUTTON-TAB2_SIDEBAR', 'children'),
#         Output('DATA_TABLE_WELL_STORE-TAB2_BODY_CONTENT2', 'data'),
#         Input('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
#         Input('SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
#         Input('SELECT_TYPE_YEAR-TAB2_SIDEBAR_LEFT_CARD2', 'value'),
#         Input('SELECT_PARAMETER-TAB2_SIDEBAR_LEFT_CARD2', 'value'),
#         Input('STATISTICAL_ANALYSIS-TAB2_SIDEBAR_LEFT_CARD2', 'value'),
#     )
#     def FUNCTION_TABLE_TAB2_BODY_CONTENT2(aquifers, wells, typeYear, para, statistical):
#         if (aquifers is not None) and (len(aquifers) != 0) \
#             and (wells is not None) and (len(wells) != 0):
#                 if (len(aquifers) == 1) and (len(wells) == 1):
#                     data = RawDATA[RawDATA["Aquifer_Name"].isin(aquifers)]
#                     data = data[data["Well_Name"].isin(wells)]
#                     data.reset_index(inplace = True)

#                     df_tmp = data[["year_Date_Persian", "month_Date_Persian", "Well_Head"]]
#                     df_tmp.columns = ["سال", "ماه", "پارامتر"]
#                     df_tmp = resultTable(df_tmp)
#                     df_tmp.columns = ["سال", "ماه", "تراز ماهانه سطح آب زیرزمینی", "سال آبی", "ماه آبی", "تغییرات هر ماه نسبت به ماه قبل", "تغییرات هر ماه نسبت به ماه سال قبل"]


#                     para_dic = {
#                         "WATER_TABLE_MONTLY" : "تراز ماهانه سطح آب زیرزمینی",
#                         "WATER_TABLE_DIFF_MONTLY" : "تغییرات هر ماه نسبت به ماه قبل",
#                         "WATER_TABLE_DIFF_MONTLY_YEARLY" : "تغییرات هر ماه نسبت به ماه سال قبل",
#                     }

#                     title_dic = {
#                         "WATER_TABLE_MONTLY" : "تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی (متر)",
#                         "WATER_TABLE_DIFF_MONTLY" : "تغییرات ماهانه (هر ماه نسبت به ماه قبل) تراز سطح آب زیرزمینی (متر)",
#                         "WATER_TABLE_DIFF_MONTLY_YEARLY" : "تغییرات ماهانه (هر ماه در سال جاری نسبت به ماه متناظر در سال قبل) تراز سطح آب زیرزمینی (متر)",
#                     }

#                     if typeYear == "WATER_YEAR":
#                         df_result = df_tmp.pivot_table(
#                             values=para_dic[para],
#                             index="سال آبی",
#                             columns="ماه آبی"
#                         ).reset_index()
#                         df_result.columns = ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]
#                     else:
#                         df_result = df_tmp.pivot_table(
#                             values=para_dic[para],
#                             index="سال",
#                             columns="ماه"
#                         ).reset_index()
#                         df_result.columns = ["سال شمسی", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

#                     df_result_statistical = df_result.copy()

#                     if statistical is not None and 'STATISTICAL_ANALYSIS' in statistical:
#                         if para == "WATER_TABLE_MONTLY":
#                             df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
#                             df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
#                             df_result_statistical["مقدار میانگین"] = df_result.iloc[:,1:].mean(axis=1).round(2)
#                             df_result = df_result_statistical.copy()
#                         elif para == "WATER_TABLE_DIFF_MONTLY":
#                             df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
#                             df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
#                             df_result_statistical["مقدار میانگین سالانه"] = df_result.iloc[:,1:].mean(axis=1).round(2)
#                             df_result_statistical["مقدار تجمعی میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"].cumsum(skipna=True).round(2)
#                             df_result_statistical["مجموع ماهانه"] = df_result.iloc[:,1:].sum(axis=1).round(2)
#                             df_result_statistical["مقدار تجمعی مجموع ماهانه"] = df_result_statistical["مجموع ماهانه"].cumsum(skipna=True).round(2)
#                             df_result = df_result_statistical.copy()
#                         elif para == "WATER_TABLE_DIFF_MONTLY_YEARLY":
#                             df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
#                             df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
#                             df_result_statistical["مقدار میانگین سالانه"] = df_result.iloc[:,1:].mean(axis=1).round(2)
#                             df_result_statistical["تغییرات مقدار میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"] - df_result_statistical["مقدار میانگین سالانه"].shift(1)
#                             df_result_statistical["تغییرات مقدار میانگین سالانه"] = df_result_statistical["تغییرات مقدار میانگین سالانه"].round(2)
#                             df_result_statistical["مقدار تجمعی میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"].cumsum(skipna=True).round(2)
#                             if typeYear == "WATER_YEAR":
#                                 df_result_statistical["مقدار تجمعی (مهر تا مهر)"] = df_result["مهر"].cumsum(skipna=True).round(2)
#                             df_result = df_result_statistical.copy()

#                     result = [
#                         df_result.to_dict('records'),
#                         [{"name": i, "id": i} for i in df_result.columns],
#                         title_dic[para] + " - چاه " + wells[0],
#                         True,
#                         df_result.to_dict('records')
#                     ]

#                     return result
#                 else:
#                     zz = ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]
#                     result = [
#                         [{}],
#                         [{"name": i, "id": i} for i in zz],
#                         "تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی (متر)",
#                         False,
#                         None
#                     ]
#                     return result
#         else:
#             zz = ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]
#             result = [
#                 [{}],
#                 [{"name": i, "id": i} for i in zz],
#                 "تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی (متر)",
#                 False,
#                 None
#             ]
#             return result


#     # -----------------------------------------------------------------------------
#     # ACTIVE DOWNLOAD BUTTON - TAB2 BODY CONTENT2
#     # -----------------------------------------------------------------------------
#     @app.callback(
#         Output('DOWNLOAD_TABLE_BUTTON-TAB2_BODY_CONTENT2', 'disabled'),
#         Input('STATE_TABLE_DOWNLOAD_BUTTON-TAB2_SIDEBAR', 'children'),
#     )
#     def FUNCTION_ACTIVE_DOWNLOAD_TABLE_BUTTON_TAB1_BODY_CONTENT2(state_table):
#         if state_table:
#             return False
#         else:
#             return True


#     # -----------------------------------------------------------------------------
#     # TABLE DOWNLOAD - TAB2 BODY CONTENT2
#     # -----------------------------------------------------------------------------
#     @app.callback(
#         Output('DOWNLOAD_TABLE_COMPONENT-TAB2_BODY_CONTENT2', 'data'),
#         Output('DOWNLOAD_TABLE_BUTTON-TAB2_BODY_CONTENT2', 'n_clicks'),
#         Input('DOWNLOAD_TABLE_BUTTON-TAB2_BODY_CONTENT2', 'n_clicks'),
#         Input('DATA_TABLE_WELL_STORE-TAB2_BODY_CONTENT2', 'data'),
#         prevent_initial_call=True,
#     )
#     def FUNCTION_DOWNLOAD_TABLE_COMPONENT_TAB1_BODY_CONTENT2(n, data):
#         if n != 0 and data is not None:
#             result = [
#                 dcc.send_data_frame(pd.DataFrame.from_dict(data).to_excel, "DataTable.xlsx", sheet_name="Sheet1", index=False),
#                 0
#             ]
#             return result
#         else:
#             raise PreventUpdate

    # # DEBUG SECTION
    # # -----------------------------------------------------------------------------

    # @app.callback(
    #     Output("DEBUG_OUTPUT-TAB2_SIDEBAR_CARD2", "children"),
    #     Output("DEBUG_BUTTON-TAB2_SIDEBAR_CARD2", "n_clicks"),
    #     Input("DEBUG_CONTENT-TAB2_SIDEBAR_LEFT_CARD2", "value"),
    #     Input("DEBUG_BUTTON-TAB2_SIDEBAR_CARD2", "n_clicks"),
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
