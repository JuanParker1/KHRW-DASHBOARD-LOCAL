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
                "font": {"size": 36}
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
# SELECT AQUIFER - TAB3 SIDEBAR LEFT CARD1
# -----------------------------------------------------------------------------
@app.callback(
    Output('SELECT_AQUIFER-TAB3_SIDEBAR_LEFT_CARD1', 'options'),
    Input("TABLE_RAWDATA-TAB1_SIDEBAR", "children") # CHECH TABLE EXISTED
)
def FUNCTION_SELECT_AQUIFER_TAB3_SIDEBAR_LEFT_CARD1(RAWDATA_TABLE):
    if RAWDATA_TABLE == "OK":
        return [{"label": col, "value": col} for col in GeoInfoData['Aquifer_Name'].unique()]            
    else:
        return []


# -----------------------------------------------------------------------------
# SELECT WELL - TAB3 SIDEBAR LEFT CARD1
# -----------------------------------------------------------------------------
@app.callback(
    Output('SELECT_WELL-TAB3_SIDEBAR_LEFT_CARD1', 'options'),
    Input('SELECT_AQUIFER-TAB3_SIDEBAR_LEFT_CARD1', 'value')
)
def FUNCTION_SELECT_WELL_TAB3_SIDEBAR_LEFT_CARD1(aquifers):
    if aquifers is not None and len(aquifers) != 0:
        df = GeoInfoData[GeoInfoData["Aquifer_Name"].isin(aquifers)]
        return [{"label": col, "value": col} for col in df["Well_Name"].unique()]
    else:
        return []


# -----------------------------------------------------------------------------
# SELECT END YEAR - TAB3 SIDEBAR LEFT CARD1
# -----------------------------------------------------------------------------
# FIXME : Problem Duration Of Date
@app.callback(
    Output('SELECT_END_YEAR-TAB3_SIDEBAR_LEFT_CARD1', 'options'),
    Input('SELECT_START_YEAR-TAB3_SIDEBAR_LEFT_CARD1', 'value')
)
def FUNCTION_SELECT_END_YEAR_TAB3_SIDEBAR_LEFT_CARD1(start):
    if start is not None:
        return [{'label': '{}'.format(i), 'value': i, 'disabled': False if i >= start else True} for i in range(1370, 1426)]
    else:
        return []


# -----------------------------------------------------------------------------
# CREATE MAP - TAB3 SIDEBAR LEFT CARD1
# -----------------------------------------------------------------------------
# FIXME : Problem With Same Well Name
@app.callback(
    Output('MAP-TAB3_SIDEBAR_LEFT_CARD1', 'figure'),
    Input('SELECT_AQUIFER-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
    Input('SELECT_WELL-TAB3_SIDEBAR_LEFT_CARD1', 'value')
)
def FUNCTION_MAP_TAB3_SIDEBAR_LEFT_CARD1(aquifers, wells):
    if (aquifers is not None) and (len(aquifers) != 0):
       
        # Load Required Data
        data = GeoInfoData[GeoInfoData["Aquifer_Name"].isin(aquifers)]
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
        
        fig.update_layout(
            mapbox = {
                'style': "stamen-terrain",
                'zoom': 5,
                'center': {
                    'lon': data.X_Decimal.mean(),
                    'lat': data.Y_Decimal.mean()
                },
            },
            showlegend = False,
            hovermode='closest',
            margin = {'l':0, 'r':0, 'b':0, 't':0}
        )
        
        if (wells is not None) and (len(wells) != 0):
            selected_wells = data[data['Well_Name'].isin(wells)]

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
# SHOW DELTA VALUE - TAB3 BODY CONTENT1
# -----------------------------------------------------------------------------
@app.callback(
    Output('SHOW_DELTA-TAB3_SIDEBAR_LEFT_CARD1', 'children'),
    Input('SELECT_DELTA-TAB3_SIDEBAR_LEFT_CARD1', 'value')
)
def FUNCTION_SHOW_DELTA_TAB3_SIDEBAR_LEFT_CARD1(value):
    return '{}'.format(value)




# -----------------------------------------------------------------------------
# ADJUSTMENT AQUIFER HEAD - TAB3 BODY CONTENT1
# -----------------------------------------------------------------------------
@app.callback(
    Output('GRAPH-TAB3_BODY_CONTENT1', 'figure'),
    Input('CALCULATE_AQUIFER_HYDROGRAPH-TAB3_SIDEBAR_LEFT_CARD1', 'n_clicks'),
    Input('SELECT_AQUIFER-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
    Input('SELECT_START_YEAR-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
    Input('SELECT_END_YEAR-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
    Input('SELECT_DELTA-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
    Input('SELECT_TYPE_MEAN-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
    Input('SELECT_WELL-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
)
def FUNCTION_adjustment_aquifer_head(n, aquifers, start, end, threshold, mean_type, wells):
    if (aquifers is not None) and (len(aquifers) != 0) and (start is not None) and (end is not None) and n == 0:
        if len(aquifers) > 1:
            data = AquiferDATA[AquiferDATA["Aquifer_Name"].isin(aquifers)]
            data = data[data['year_Date_Persian'] >= start]
            data = data[data['year_Date_Persian'] <= end]
        
            fig = go.Figure()
            
            for aquifer in aquifers:
                data_aquifer = data[data["Aquifer_Name"] == aquifer]
                fig.add_trace(
                    go.Scatter(
                        x=data_aquifer['Date_Persian'],
                        y=data_aquifer['Adjusted_Aquifer_Head'],
                        mode='lines+markers',
                        name=aquifer
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
                    text='متوسط تراز ماهانه (روز پانزدهم) تعدیل شده سطح آب زیرزمینی در آبخوان',
                    yanchor="top",
                    y=0.95,
                    xanchor="center",
                    x=0.500
                )
            )
            return fig
        
        elif len(aquifers) == 1:            
            data = AquiferDATA[AquiferDATA["Aquifer_Name"].isin(aquifers)]
            data = data[data['year_Date_Persian'] >= start]
            data = data[data['year_Date_Persian'] <= end]
        
            fig = go.Figure()
                
            fig.add_trace(
                go.Scatter(
                    x=data['Date_Persian'],
                    y=data['Aquifer_Head'],
                    mode='lines+markers',
                    name='تعدیل نشده'
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=data['Date_Persian'],
                    y=data['Adjusted_Aquifer_Head'],
                    mode='lines+markers',
                    name='تعدیل شده'
                )
            )

            if mean_type is not None and 'Arithmetic' in mean_type:
                fig.add_trace(
                    go.Scatter(
                        x=data['Date_Persian'],
                        y=data['Aquifer_Head_Arithmetic_Mean'],
                        mode='lines+markers',
                        name='میانگین حسابی'
                    )
                )

            if mean_type is not None and 'Geometric' in mean_type:
                fig.add_trace(
                    go.Scatter(
                        x=data['Date_Persian'],
                        y=data['Aquifer_Head_Geometric_Mean'],
                        mode='lines+markers',
                        name='میانگین هندسی'
                    )
                )

            if mean_type is not None and 'Harmonic' in mean_type:
                fig.add_trace(
                    go.Scatter(
                        x=data['Date_Persian'],
                        y=data['Aquifer_Head_Harmonic_Mean'],
                        mode='lines+markers',
                        name='میانگین هارمونیک'
                    )
                )
            
            
            if (wells is not None) and (len(wells) != 0):
                data_wells = RawDATA[RawDATA["Aquifer_Name"].isin(aquifers)]
                data_wells = data_wells[data_wells["Well_Name"].isin(wells)]
                data_wells = data_wells[data_wells['year_Date_Persian'] >= start]
                data_wells = data_wells[data_wells['year_Date_Persian'] <= end]
                for well in wells:                    
                    data_well = data_wells[data_wells["Well_Name"] == well]                                   
                    fig.add_trace(
                        go.Scatter(
                            x=data_well['Date_Persian'],
                            y=data_well['Well_Head'],
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
                    text= 'متوسط تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی در آبخوان ' + aquifers[0],
                    yanchor="top",
                    y=0.95,
                    xanchor="center",
                    x=0.500
                )
            )
            return fig
        else:
            return NO_MATCHING_DATA_FOUND            

    else:
        return NO_MATCHING_DATA_FOUND



# -----------------------------------------------------------------------------
# TABLE - TAB3 BODY CONTENT2
# -----------------------------------------------------------------------------
@app.callback(
    Output('TABLE-TAB3_BODY_CONTENT2', 'data'),
    Output('TABLE-TAB3_BODY_CONTENT2', 'columns'),
    Output('TABLE_HEADER-TAB3_BODY_CONTENT2', 'children'),
    Output('STATE_TABLE_DOWNLOAD_BUTTON-TAB3_SIDEBAR', 'children'),
    Output('DATA_TABLE_WELL_STORE-TAB3_BODY_CONTENT2', 'data'),
    Input('SELECT_AQUIFER-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
    Input('SELECT_TYPE_YEAR-TAB3_SIDEBAR_LEFT_CARD2', 'value'),
    Input('SELECT_PARAMETER-TAB3_SIDEBAR_LEFT_CARD2', 'value'),
    Input('STATISTICAL_ANALYSIS-TAB3_SIDEBAR_LEFT_CARD2', 'value'),
)
def FUNCTION_TABLE_TAB3_BODY_CONTENT2(aquifers, typeYear, para, statistical):
    if (aquifers is not None) and (len(aquifers) != 0):
        if (len(aquifers) == 1):
            data = AquiferDATA[AquiferDATA["Aquifer_Name"].isin(aquifers)]
            data.reset_index(inplace = True)
            
            df_tmp = data[["year_Date_Persian", "month_Date_Persian", "Adjusted_Aquifer_Head", "Aquifer_Area", "Aquifer_Storage_Coefficient"]]
            df_tmp.columns = ["سال", "ماه", "هد", "مساحت", "ضریب"]
            df_tmp = resultTableAquifer(df_tmp)
            df_tmp.columns = ["سال", "ماه", "تراز ماهانه سطح آب زیرزمینی", "مساحت شبکه تیسن", "ضریب ذخیره", "سال آبی", "ماه آبی", "تغییرات هر ماه نسبت به ماه قبل", "تغییرات هر ماه نسبت به ماه سال قبل"]
            df_tmp["تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"] = df_tmp["تغییرات هر ماه نسبت به ماه قبل"] * df_tmp["مساحت شبکه تیسن"] * df_tmp["ضریب ذخیره"]
            df_tmp["تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"] = df_tmp["تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"].round(2)
            df_tmp["تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"] = df_tmp["تغییرات هر ماه نسبت به ماه سال قبل"] * df_tmp["مساحت شبکه تیسن"] * df_tmp["ضریب ذخیره"]
            df_tmp["تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"] = df_tmp["تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"] .round(2)
            
            df_tmp.to_csv("dddsdsdsd.csv")
            
            para_dic = {
                "WATER_TABLE_MONTLY" : "تراز ماهانه سطح آب زیرزمینی",
                "WATER_TABLE_DIFF_MONTLY" : "تغییرات هر ماه نسبت به ماه قبل",
                "WATER_TABLE_DIFF_MONTLY_YEARLY" : "تغییرات هر ماه نسبت به ماه سال قبل",
                "STOREG_DIFF_MONTLY" : "تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل",
                "STOREG_DIFF_MONTLY_YEARLY" : "تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"
            }
            
            title_dic = {
                "WATER_TABLE_MONTLY" : "تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی (متر)",
                "WATER_TABLE_DIFF_MONTLY" : "تغییرات ماهانه (هر ماه نسبت به ماه قبل) تراز سطح آب زیرزمینی (متر)",
                "WATER_TABLE_DIFF_MONTLY_YEARLY" : "تغییرات ماهانه (هر ماه در سال جاری نسبت به ماه متناظر در سال قبل) تراز سطح آب زیرزمینی (متر)",
                "STOREG_DIFF_MONTLY" : "متوسط تغییرات ماهانه (هر ماه نسبت به ماه قبل) ذخیره در آبخوان (میلیون متر مکعب)",
                "STOREG_DIFF_MONTLY_YEARLY" : "تغییرات ماهانه (هر ماه در سال جاری نسبت به ماه متناظر در سال قبل) ذخیره در آبخوان (میلیون متر مکعب)",
            }                

            if typeYear == "WATER_YEAR":
                df_result = df_tmp.pivot_table(
                    values=para_dic[para],
                    index="سال آبی",
                    columns="ماه آبی"
                ).reset_index()
                df_result.columns = ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]
            else:
                df_result = df_tmp.pivot_table(
                    values=para_dic[para],
                    index="سال",
                    columns="ماه"
                ).reset_index()
                df_result.columns = ["سال شمسی", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
            
            df_result_statistical = df_result.copy()
            
            if statistical is not None:
                if para == "WATER_TABLE_MONTLY":
                    df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
                    df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
                    df_result_statistical["مقدار میانگین"] = df_result.iloc[:,1:].mean(axis=1).round(2)
                    df_result = df_result_statistical.copy()
                elif para == "WATER_TABLE_DIFF_MONTLY" or para == "STOREG_DIFF_MONTLY":
                    df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
                    df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
                    df_result_statistical["مقدار میانگین سالانه"] = df_result.iloc[:,1:].mean(axis=1).round(2)
                    df_result_statistical["مقدار تجمعی میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"].cumsum(skipna=True).round(2) 
                    df_result_statistical["مجموع ماهانه"] = df_result.iloc[:,1:].sum(axis=1).round(2)
                    df_result_statistical["مقدار تجمعی مجموع ماهانه"] = df_result_statistical["مجموع ماهانه"].cumsum(skipna=True).round(2)
                    df_result = df_result_statistical.copy()
                elif para == "WATER_TABLE_DIFF_MONTLY_YEARLY" or para == "STOREG_DIFF_MONTLY_YEARLY":
                    df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
                    df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
                    df_result_statistical["مقدار میانگین سالانه"] = df_result.iloc[:,1:].mean(axis=1).round(2)
                    df_result_statistical["تغییرات مقدار میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"] - df_result_statistical["مقدار میانگین سالانه"].shift(1)
                    df_result_statistical["تغییرات مقدار میانگین سالانه"] = df_result_statistical["تغییرات مقدار میانگین سالانه"].round(2)
                    df_result_statistical["مقدار تجمعی میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"].cumsum(skipna=True).round(2)
                    if typeYear == "WATER_YEAR":
                        df_result_statistical["مقدار تجمعی (مهر تا مهر)"] = df_result["مهر"].cumsum(skipna=True).round(2)
                    df_result = df_result_statistical.copy()
                    
            result = [
                df_result.to_dict('records'),
                [{"name": i, "id": i} for i in df_result.columns],
                title_dic[para] + " - آبخوان " + aquifers[0],
                True,
                df_result.to_dict('records')
            ]
            
            return result
        else:  
            zz = ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]              
            result = [
                [{}],
                [{"name": i, "id": i} for i in zz],
                "تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی (متر)",
                False,
                None
            ]                
            return result 
    else:
        zz = ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]
        result = [
            [{}],
            [{"name": i, "id": i} for i in zz],
            "تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی (متر)",
            False,
            None
        ]
        return result



# -----------------------------------------------------------------------------
# ACTIVE DOWNLOAD BUTTON - TAB3 BODY CONTENT2
# -----------------------------------------------------------------------------
@app.callback(
    Output('DOWNLOAD_TABLE_BUTTON-TAB3_BODY_CONTENT2', 'disabled'),
    Input('STATE_TABLE_DOWNLOAD_BUTTON-TAB3_SIDEBAR', 'children'),
)
def FUNCTION_ACTIVE_DOWNLOAD_TABLE_BUTTON_TAB1_BODY_CONTENT2(state_table):
    if state_table:
        return False
    else:
        return True


# -----------------------------------------------------------------------------
# TABLE DOWNLOAD - TAB3 BODY CONTENT2
# -----------------------------------------------------------------------------
@app.callback(
    Output('DOWNLOAD_TABLE_COMPONENT-TAB3_BODY_CONTENT2', 'data'),
    Output('DOWNLOAD_TABLE_BUTTON-TAB3_BODY_CONTENT2', 'n_clicks'),
    Input('DOWNLOAD_TABLE_BUTTON-TAB3_BODY_CONTENT2', 'n_clicks'),
    Input('DATA_TABLE_WELL_STORE-TAB3_BODY_CONTENT2', 'data'),
    prevent_initial_call=True,
)
def FUNCTION_DOWNLOAD_TABLE_COMPONENT_TAB1_BODY_CONTENT2(n, data):
    if n != 0 and data is not None:
        result = [
            dcc.send_data_frame(pd.DataFrame.from_dict(data).to_excel, "DataTableAquifer.xlsx", sheet_name="Sheet1", index=False),
            1
        ]
        return result
    else:
        raise PreventUpdate