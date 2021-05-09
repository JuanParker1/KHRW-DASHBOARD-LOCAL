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
from callbacks.data_analysis import *




# CASE-DEPENDENT
TABLE_HEADER_NAME = {    
    "Mahdodeh_Name" : "نام محدوده",
    "Mahdodeh_Code" : "کد محدوده",
    "Aquifer_Name" : "نام آبخوان",
    "Well_Type" : "نوع چاه",
    "Well_Type_Sign" : "علامت نوع چاه",
    "Well_Name" : "نام چاه",
    "Well_ID" : "شناسه چاه",
    "ID" : "شناسه",
    "Zone_UTM" : "منطقه UTM",
    "X_UTM" : "طول جغرافیایی - UTM",
    "Y_UTM" : "عرض جغرافیایی - UTM",
    "UTM_Grid" : "شبکه UTM",
    "X_Decimal" : "طول جغرافیایی",
    "Y_Decimal" : "عرض جغرافیایی",
    "G.S.L_M.S.L" : "ارتفاع - MSL",
    "G.S.L_DGPS" : "ارتفاع - DGPS",
    "G.S.L_DEM_SRTM" : "ارتفاع - SRTM",
    "Final_Elevation" : "ارتفاع",
    "Data_Typ" : "نوع داده",  
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
                "font": {"size": 24}
            }
        ]
    }
}


# -----------------------------------------------------------------------------
# BASE MAP
# -----------------------------------------------------------------------------
BASE_MAP = go.Figure(
    go.Scattermapbox(
        lat=[36.25],
        lon=[59.55],
        mode='markers',
        marker=go.scattermapbox.Marker(size=9),
        text="شهر مشهد"
    )
)

BASE_MAP.update_layout(
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
# SELECT AQUIFER - TAB2 SIDEBAR LEFT CARD1
# -----------------------------------------------------------------------------
@app.callback(
    Output('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
    Input("TABLE_RAWDATA-TAB1_SIDEBAR", "children")
)
def FUNCTION_SELECT_AQUIFER_TAB2_SIDEBAR_LEFT_CARD1(RAWDATA_TABLE):
    if RAWDATA_TABLE == "OK":
        return [{"label": col, "value": col} for col in GeoInfoData['Aquifer_Name'].unique()]            
    else:
        return []


# -----------------------------------------------------------------------------
# SELECT WELL - TAB2 SIDEBAR LEFT CARD1
# -----------------------------------------------------------------------------
@app.callback(
    Output('SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
    Input('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'value')
)
def FUNCTION_SELECT_WELL_TAB2_SIDEBAR_LEFT_CARD1(aquifers):
    if aquifers is not None and len(aquifers) != 0:
        df = GeoInfoData[GeoInfoData["Aquifer_Name"].isin(aquifers)]
        return [{"label": col, "value": col} for col in df["Well_Name"].unique()]
    else:
        return []


# -----------------------------------------------------------------------------
# SELECT END YEAR - TAB2 SIDEBAR LEFT CARD1
# -----------------------------------------------------------------------------
# FIXME : Problem Duration Of Date
@app.callback(
    Output('SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
    Input('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value')
)
def FUNCTION_SELECT_END_YEAR_TAB2_SIDEBAR_LEFT_CARD1(start):
    if start is not None:
        return [{'label': '{}'.format(i), 'value': i, 'disabled': False if i >= start else True} for i in range(1370, 1426)]
    else:
        return []


# -----------------------------------------------------------------------------
# CREATE MAP - TAB2 SIDEBAR LEFT CARD1
# -----------------------------------------------------------------------------
# FIXME : Problem With Same Well Name
@app.callback(
    Output('MAP-TAB2_SIDEBAR_LEFT_CARD1', 'figure'),
    Input('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    Input('SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1', 'value')
)
def FUNCTION_MAP_TAB2_SIDEBAR_LEFT_CARD1(aquifers, wells):
    if (aquifers is not None) and (len(aquifers) != 0) and (wells is not None) and (len(wells) != 0):
       
        # Load Required Data
        data = GeoInfoData[GeoInfoData["Aquifer_Name"].isin(aquifers)]
        selected_wells = data[data['Well_Name'].isin(wells)]
        mah_code = list(data["Mahdodeh_Code"].unique())
        
        # Load Shapefile
        geodf, j_file = read_shapfile(mah_code=mah_code)
        
        # Create Map
        fig = px.choropleth_mapbox(
            data_frame=geodf,
            geojson=j_file,
            locations='Mah_code',
            opacity=0.4
        )
        
        fig.add_trace(
            go.Scattermapbox(
                lat=data.Y_Decimal,
                lon=data.X_Decimal,
                mode='markers',
                marker=go.scattermapbox.Marker(size=8),
                text=data["Well_Name"],
                hoverinfo='text',
                hovertemplate='<span style="color:white;">%{text}</span><extra></extra>'
            )
        )
        
        fig.add_trace(
            go.Scattermapbox(
                lat=selected_wells.Y_Decimal,
                lon=selected_wells.X_Decimal,
                mode='markers',
                marker=go.scattermapbox.Marker(
                    size=10,
                    color='green'
                ),
                text=selected_wells["Well_Name"],
                hoverinfo='text',
                hovertemplate='<b>%{text}</b><extra></extra>'
            ), 
        )
               
        fig.update_layout(
            mapbox = {
                'style': "stamen-terrain",
                'zoom': 5,
                'center': {
                    'lon': selected_wells.X_Decimal.mean(),
                    'lat': selected_wells.Y_Decimal.mean()
                },
            },
            showlegend = False,
            hovermode='closest',
            margin = {'l':0, 'r':0, 'b':0, 't':0}
        )
                 
        return fig        
    else:
        return BASE_MAP




# -----------------------------------------------------------------------------
# CREATE GRAPH - TAB2 BODY CONTENT1
# -----------------------------------------------------------------------------
@app.callback(
    Output('GRAPH-TAB2_BODY_CONTENT1', 'figure'),    
    Input('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    Input('SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    Input('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    Input('SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value')
)
def FUNCTION_GRAPH_TAB2_BODY_CONTENT1(aquifers, wells, start, end):
    if (aquifers is not None) and (len(aquifers) != 0) \
        and (wells is not None) and (len(wells) != 0) \
            and (start is not None) and (end is not None):
                data = RawDATA[RawDATA["Aquifer_Name"].isin(aquifers)]
                data = data[data["Well_Name"].isin(wells)]
                data = data[data['year_Date_Persian'] >= start]
                data = data[data['year_Date_Persian'] <= end]
                
                data.to_csv("ddd.csv")
                
                # PLOT
                fig = go.Figure()
                                
                for well in wells:                    
                    df_well = data[data["Well_Name"] == well]   
                                     
                    fig.add_trace(
                        go.Scatter(
                            x=df_well['Date_Persian'],
                            y=df_well['Well_Head'],
                            mode='lines+markers',
                            name=well
                        )
                    )

                fig.update_layout(
                    margin={'l': 3, 'r': 3},
                    xaxis_title="تاریخ",
                    yaxis_title="ارتفاع سطح آب ایستابی - متر",
                    autosize=False,
                    font=dict(
                        family="Tanha-FD",
                        size=16,
                        color="RebeccaPurple"
                    ),
                    xaxis=dict(
                        tickformat="%Y-%m"
                    ),
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=1.005,
                        xanchor="left",
                        x=0.000
                    ),
                    title=dict(
                        text='تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی',
                        yanchor="top",
                        y=0.925,
                        xanchor="center",
                        x=0.500
                    )
                )
                return fig
    else:
        return NO_MATCHING_DATA_FOUND
