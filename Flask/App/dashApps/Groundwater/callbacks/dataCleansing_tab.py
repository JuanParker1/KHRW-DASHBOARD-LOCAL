import os
import sqlite3
import json
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

    # -----------------------------------------------------------------------------
    # CHECK DATABASE EXIST AND STORE DATA
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('DATABASE_STATE___DATA_CLEANSING_TAB', 'data'),
        Output('DATA_STORE___DATA_CLEANSING_TAB', 'data'),
        Output('BUTTON___BUTTONS___DATA_CLEANSING_TAB', 'n_clicks'),
        Input('LOAD_DATABASE___DATA_CLEANSING_TAB', 'n_intervals'),
        Input('BUTTON___BUTTONS___DATA_CLEANSING_TAB', 'n_clicks'),
        Input('GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB', 'selectedData'),
        State('TABLE___DATA_CLEANSING_TAB', 'data'),
        State('DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___DATABASE____DATA_CLEANSING_TAB(n_interval, n_click, graphData, tableData, data):
        if os.path.exists(PATH_DB_GROUNDWATER_RAW_DATA):
            if n_click != 0 and graphData is not None:
                df = pd.DataFrame(tableData).reset_index(drop=True)
                df.columns = ["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN_RAW", "WATER_TABLE_RAW", "WATER_TABLE_MODIFY"]               
                data = pd.DataFrame.from_dict(data)
                for i in range(len(df)):                    
                    MN = df.loc[i, "MAHDOUDE_NAME"]
                    AN = df.loc[i, "AQUIFER_NAME"]
                    LN = df.loc[i, "LOCATION_NAME"]
                    DPR =  df.loc[i, "DATE_PERSIAN_RAW"]                    
                    data.loc[
                        (data['MAHDOUDE_NAME'] == MN) & (data['AQUIFER_NAME'] == AN) & (data['LOCATION_NAME'] == LN) & (data['DATE_PERSIAN_RAW'] == DPR),
                        'WATER_TABLE_MODIFY'
                    ] = float(df.loc[i, "WATER_TABLE_MODIFY"])
                data.to_sql(
                    name="GROUNDWATER_DATA",
                    con=DB_GROUNDWATER_RAW_DATA,
                    if_exists="replace"
                )
                return [
                    "OK",
                    data.to_dict('records'),
                    0,
                ]
            else:
                data = pd.read_sql_query(
                    sql="SELECT * FROM GROUNDWATER_DATA",
                    con=DB_GROUNDWATER_RAW_DATA
                ).drop(['index'], axis=1)
                return [
                    "OK",
                    data.to_dict('records'),
                    0,
                ]
        else:
            return [
                "NO",
                None,
                0,
            ]



    # -----------------------------------------------------------------------------
    # STUDY AREA SELECT - CONTROLS - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'options'),
        Input('DATABASE_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB(database_state, data):        
        if database_state == "OK" and data is not None:
            data = pd.DataFrame.from_dict(data)
            return [{"label": col, "value": col} for col in data['MAHDOUDE_NAME'].unique()]        
        else:
            return []
    
    
    
    # -----------------------------------------------------------------------------
    # AQUIFER SELECT - CONTROLS - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'options'),
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('DATABASE_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB(study_area, database_state, data):
        if database_state == "OK" and data is not None:
            if study_area is not None and len(study_area) != 0:
                data = pd.DataFrame.from_dict(data)
                data = data[data["MAHDOUDE_NAME"].isin(study_area)]
                return [{"label": col, "value": col} for col in data['AQUIFER_NAME'].unique()]
            else:
                return []
        else:
            return []



    # -----------------------------------------------------------------------------
    # WELL SELECT - CONTROLS - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'options'),
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('DATABASE_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB(study_area, aquifer, database_state, data):
        if database_state == "OK" and data is not None:
            if study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) != 0:
                data = pd.DataFrame.from_dict(data)
                data = data[data["MAHDOUDE_NAME"].isin(study_area)]
                data = data[data["AQUIFER_NAME"].isin(aquifer)]
                return [{"label": col, "value": col} for col in data['LOCATION_NAME'].unique()]
            else:
                return []
        else:
            return []
    
    
    
    # -----------------------------------------------------------------------------
    # GRAPH - GRAPH & MAP - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB', 'figure'),   
        Input('LOAD_DATABASE___DATA_CLEANSING_TAB', 'n_intervals'),
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        State('DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB(n_interval, study_area, aquifer, well, data):        
        if study_area is not None and len(study_area) != 0 and\
            aquifer is not None and len(aquifer) != 0 and\
                well is not None and len(well) != 0:
                    
                    data = pd.DataFrame.from_dict(data)
                    data = data[data["MAHDOUDE_NAME"].isin(study_area)]
                    data = data[data["AQUIFER_NAME"].isin(aquifer)]
                    data = data[data["LOCATION_NAME"].isin(well)]
                    data = data.sort_values(
                        by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_RAW"]
                    ).reset_index(drop=True)
                    
                    # Method 1:
                    
                    data["DIFF"] = data["WATER_TABLE_MODIFY"].diff().abs()
                    data["DIFF_MEAN"] = data["DIFF"].rolling(6).mean()
                    data["CHECK_METHOD_1"] = data["DIFF"] > (data["DIFF_MEAN"] * 2)
                    data["SHIFT_DATE"] = data["DATE_GREGORIAN_RAW"].shift(periods=1, fill_value=0)                    
                    data[['DATE_GREGORIAN_RAW','SHIFT_DATE']] = data[['DATE_GREGORIAN_RAW','SHIFT_DATE']].apply(pd.to_datetime)                  
                    data["DIFF_DATE"] = (data["DATE_GREGORIAN_RAW"] - data["SHIFT_DATE"]).dt.days.abs()
                    data["DERIVATIV"] = (data["DIFF"] / data["DIFF_DATE"]) * 100
                    data["CHECK_METHOD_2"] = data["DERIVATIV"] > 2

                                
                    # PLOT
                    fig = go.Figure()
                                    
                    for w in well:                    
                        df_w = data[data["LOCATION_NAME"] == w]
                        
                        df_w = df_w.sort_values(
                            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_RAW"]
                        ).reset_index(drop=True)  
                        
                        fig.add_trace(
                            go.Scatter(
                                x=df_w['DATE_PERSIAN_RAW'],
                                y=df_w['WATER_TABLE_RAW'],
                                mode='lines+markers',
                                name=f'داده‌های خام - {w}',
                                marker=dict(
                                    color='black',
                                    size=8,
                                ),
                                line=dict(
                                    color='black',
                                    width=1
                                )  
                            )
                        )
                        
                        fig.add_trace(
                            go.Scatter(
                                x=df_w['DATE_PERSIAN_RAW'],
                                y=df_w['WATER_TABLE_MODIFY'],
                                mode='lines+markers',
                                name=f'داده‌های اصلاح شده - {w}',
                                marker=dict(
                                    color='green',
                                    size=8,
                                ),
                                line=dict(
                                    color='green',
                                    width=1
                                )  
                            )
                        )
                        
                        
                        df_w_m_1 = df_w[df_w["CHECK_METHOD_1"]]
                        
                        fig.add_trace(
                            go.Scatter(
                                x=df_w_m_1['DATE_PERSIAN_RAW'],
                                y=df_w_m_1['WATER_TABLE_MODIFY'],
                                mode='markers',
                                name=f'روش میانگین - {w}',
                                marker=dict(
                                    color='orange',
                                    size=12,
                                    symbol='x'
                                )
                            )
                        )
                        
                        df_w_m_2 = df_w[df_w["CHECK_METHOD_2"]]
                        
                        fig.add_trace(
                            go.Scatter(
                                x=df_w_m_2['DATE_PERSIAN_RAW'],
                                y=df_w_m_2['WATER_TABLE_MODIFY'],
                                mode='markers',
                                name=f'روش مشتق - {w}',
                                marker=dict(
                                    color='red',
                                    size=6,
                                    symbol='x'
                                )
                            )
                        )
                    # fig.update_traces(hovertemplate=None)

                    fig.update_layout(
                        hoverlabel=dict(
                            namelength = -1
                        ),
                        # hovermode="x unified",
                        yaxis_title="ارتفاع سطح ایستابی - متر",
                        autosize=False,
                        font=dict(
                            family="Tanha-FD",
                            size=14,
                            color="RebeccaPurple"
                        ),
                        xaxis=dict(
                            tickformat="%Y-%m-%d"
                        ),
                        title=dict(
                            text='ارتفاع ماهانه سطح ایستابی',
                            yanchor="top",
                            y=0.98,
                            xanchor="center",
                            x=0.500
                        ),
                        margin=dict(
                            l=50,
                            r=30,
                            b=30,
                            t=50,
                            pad=0
                        ),
                        legend=dict(
                            yanchor="top",
                            y=0.99,
                            xanchor="left",
                            x=0.01
                        )
                    )
                    
                    fig.update_layout(clickmode='event+select')
                                        
                    return fig
        else:
            return NO_MATCHING_DATA_FOUND
    
    
    
    # -----------------------------------------------------------------------------
    # MAP - GRAPH & MAP - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('MAP___GRAPH_MAP___DATA_CLEANSING_TAB', 'figure'),
        Input('LOAD_DATABASE___DATA_CLEANSING_TAB', 'n_intervals'),   
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        State('DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___MAP___GRAPH_MAP___DATA_CLEANSING_TAB(n_interval, study_area, aquifer, well, data):        
        if study_area is not None and len(study_area) != 0 and\
            aquifer is not None and len(aquifer) != 0 and\
                well is not None and len(well) != 0:
                    
                    return BASE_MAP        
        else:
            return BASE_MAP

    
    
    # -----------------------------------------------------------------------------
    # TABLE - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('TABLE___DATA_CLEANSING_TAB', 'columns'),
        Output('TABLE___DATA_CLEANSING_TAB', 'data'),
        Input('LOAD_DATABASE___DATA_CLEANSING_TAB', 'n_intervals'),
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB', 'selectedData'),
        State('DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___TABLE___DATA_CLEANSING_TAB(n_interval, study_area, aquifer, well, graphData, data):     
        if study_area is not None and len(study_area) != 0 and\
            aquifer is not None and len(aquifer) != 0 and\
                well is not None and len(well) != 0 and\
                    graphData is not None:
                        
                        data = pd.DataFrame.from_dict(data)
                        data = data[data["MAHDOUDE_NAME"].isin(study_area)]
                        data = data[data["AQUIFER_NAME"].isin(aquifer)]
                        data = data[data["LOCATION_NAME"].isin(well)]
                        data = data.sort_values(
                            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_RAW"]
                        ).reset_index(drop=True)
                        
                        x = []
                        curveNumber = []
                        
                        for i in graphData["points"]:
                            x.append(i['x'])
                            curveNumber.append(i['curveNumber'])

                        df = data[data["DATE_PERSIAN_RAW"].isin(x)][["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN_RAW", "WATER_TABLE_RAW", "WATER_TABLE_MODIFY"]]
                        
                        df.columns = ["محدوده مطالعاتی", "آبخوان", "چاه مشاهداتی", "تاریخ", "داده خام سطح ایستابی", "داده اصلاح شده سطح ایستابی"]
                                                
                        return [
                            [{"name": i, "id": i} for i in df.columns],
                            df.to_dict('records'),
                        ]
        else:
            return [
                [{}],
                []
            ]