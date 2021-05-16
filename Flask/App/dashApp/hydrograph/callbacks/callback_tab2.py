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


from App.dashApp.hydrograph.callbacks.data_analysis import *



def hydrograph_callback_tab2(app):

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
                locations='Mah_Code',
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
            return BASE_MAP.update_layout(
                width=250,
                height=250
            )




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
                            y=0.95,
                            xanchor="center",
                            x=0.500
                        )
                    )
                    return fig
        else:
            return NO_MATCHING_DATA_FOUND





    # -----------------------------------------------------------------------------
    # WELL INFORMATION - TAB2 SIDEBAR RIGHT CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('IMG_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'src'),    
        Output('NAME_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),    
        Output('ID_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),    
        Output('AQUIFER_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),    
        Output('LONG_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),    
        Output('LAT_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),    
        Output('ELEV_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),    
        Output('START_DATE_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),
        Output('END_DATE_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),
        Output('TAB_2_SIDEBAR_RIGHT', 'hidden'),
        Output('TAB_2_SIDEBAR_RIGHT', 'className'),
        Output('TAB_2_BODY', 'className'),
        Input('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1', 'value')
    )
    def FUNCTION_WELL_INFORMATION_TAB2_SIDEBAR_RIGHT_CARD1(aquifers, wells):
        if (aquifers is not None) and (len(aquifers) != 0) \
            and (wells is not None) and (len(wells) != 0):
                if (len(aquifers) == 1) and (len(wells) == 1):
                    data = RawDATA[RawDATA["Aquifer_Name"].isin(aquifers)]
                    data = data[data["Well_Name"].isin(wells)]
                    data['Date_Gregorian'] = pd.to_datetime(data['Date_Gregorian'])
                    data.reset_index(inplace = True)
                    # Img OW
                    if aquifers[0] == "جوین":
                        Img_OW = base64.b64encode(
                            open('./App/static/hydrograph/images/ow1.png', 'rb').read()
                        )
                        Img_OW_SRC = 'data:image/png;base64,{}'.format(Img_OW.decode())
                    else:
                        Img_OW = base64.b64encode(
                            open('./App/static/hydrograph/images/ow2.png', 'rb').read()
                        )
                        Img_OW_SRC = 'data:image/png;base64,{}'.format(Img_OW.decode())
                        
                    # Para
                    ID = str(data['ID'].values[0])
                    LAT = str(data['X_UTM'].values[0])
                    LONG = str(data['Y_UTM'].values[0])
                    ELEV = str(data['Final_Elevation'].values[0])
                    START_DATE = str(data['year_Date_Persian'].values[data["Date_Gregorian"].idxmin()])
                    END_DATE = str(data['year_Date_Persian'].values[data["Date_Gregorian"].idxmax()])
                    
                    
                    result = [
                        Img_OW_SRC,
                        wells[0],
                        "شناسه: " + ID,
                        "آبخوان: " + aquifers[0],
                        "طول جغرافیایی: " + LAT,
                        "عرض جغرافیایی: " + LONG,
                        "ارتفاع: " + ELEV + " متر",
                        "سال شروع دوره آماری: " + START_DATE,
                        "سال پایان دوره آماری: " + END_DATE,
                        False,
                        "right-sidebar",
                        'my-body pt-2'
                    ]
                    
                    return result
                else:
                    
                    Img_OW = base64.b64encode(
                        open('./App/static/hydrograph/images/placeholder.png', 'rb').read()
                    )  # EDITPATH
                    
                    result = [
                        'data:image/png;base64,{}'.format(Img_OW.decode()),
                        "نام چاه مشاهده‌ای",
                        "شناسه چاه مشاهده‌ای",
                        "نام آبخوان",
                        "طول جغرافیایی",
                        "عرض جغرافیایی",
                        "ارتفاع",
                        "سال شروع دوره آماری",
                        "سال پایان دوره آماری",
                        True,
                        "tab2-right-sidebar-hidden",
                        'tab2-right-sidebar-hidden-my-body pt-2'
                    ]
                    
                    return result
                    
        else:
            
            Img_OW = base64.b64encode(
                open('./App/static/hydrograph/images/placeholder.png', 'rb').read()
            )  # EDITPATH
            
            result = [
                'data:image/png;base64,{}'.format(Img_OW.decode()),
                "نام چاه مشاهده‌ای",
                "شناسه چاه مشاهده‌ای",
                "نام آبخوان",
                "طول جغرافیایی",
                "عرض جغرافیایی",
                "ارتفاع",
                "سال شروع دوره آماری",
                "سال پایان دوره آماری",
                True,
                "tab2-right-sidebar-hidden",
                'tab2-right-sidebar-hidden-my-body pt-2'
            ]
            
            return result





    # -----------------------------------------------------------------------------
    # TABLE - TAB2 BODY CONTENT2
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('TABLE-TAB2_BODY_CONTENT2', 'data'),
        Output('TABLE-TAB2_BODY_CONTENT2', 'columns'),
        Output('TABLE_HEADER-TAB2_BODY_CONTENT2', 'children'),
        Output('STATE_TABLE_DOWNLOAD_BUTTON-TAB2_SIDEBAR', 'children'),
        Output('DATA_TABLE_WELL_STORE-TAB2_BODY_CONTENT2', 'data'),
        Input('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_TYPE_YEAR-TAB2_SIDEBAR_LEFT_CARD2', 'value'),
        Input('SELECT_PARAMETER-TAB2_SIDEBAR_LEFT_CARD2', 'value'),
        Input('STATISTICAL_ANALYSIS-TAB2_SIDEBAR_LEFT_CARD2', 'value'),
    )
    def FUNCTION_TABLE_TAB2_BODY_CONTENT2(aquifers, wells, typeYear, para, statistical):
        if (aquifers is not None) and (len(aquifers) != 0) \
            and (wells is not None) and (len(wells) != 0):
                if (len(aquifers) == 1) and (len(wells) == 1):
                    data = RawDATA[RawDATA["Aquifer_Name"].isin(aquifers)]
                    data = data[data["Well_Name"].isin(wells)]
                    data.reset_index(inplace = True)
                    
                    df_tmp = data[["year_Date_Persian", "month_Date_Persian", "Well_Head"]]
                    df_tmp.columns = ["سال", "ماه", "پارامتر"]
                    df_tmp = resultTable(df_tmp)
                    df_tmp.columns = ["سال", "ماه", "تراز ماهانه سطح آب زیرزمینی", "سال آبی", "ماه آبی", "تغییرات هر ماه نسبت به ماه قبل", "تغییرات هر ماه نسبت به ماه سال قبل"]
                    
                    
                    para_dic = {
                        "WATER_TABLE_MONTLY" : "تراز ماهانه سطح آب زیرزمینی",
                        "WATER_TABLE_DIFF_MONTLY" : "تغییرات هر ماه نسبت به ماه قبل",
                        "WATER_TABLE_DIFF_MONTLY_YEARLY" : "تغییرات هر ماه نسبت به ماه سال قبل",
                    }
                    
                    title_dic = {
                        "WATER_TABLE_MONTLY" : "تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی (متر)",
                        "WATER_TABLE_DIFF_MONTLY" : "تغییرات ماهانه (هر ماه نسبت به ماه قبل) تراز سطح آب زیرزمینی (متر)",
                        "WATER_TABLE_DIFF_MONTLY_YEARLY" : "تغییرات ماهانه (هر ماه در سال جاری نسبت به ماه متناظر در سال قبل) تراز سطح آب زیرزمینی (متر)",
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
                    
                    if statistical is not None and 'STATISTICAL_ANALYSIS' in statistical:
                        if para == "WATER_TABLE_MONTLY":
                            df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
                            df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
                            df_result_statistical["مقدار میانگین"] = df_result.iloc[:,1:].mean(axis=1).round(2)
                            df_result = df_result_statistical.copy()
                        elif para == "WATER_TABLE_DIFF_MONTLY":
                            df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
                            df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
                            df_result_statistical["مقدار میانگین سالانه"] = df_result.iloc[:,1:].mean(axis=1).round(2)
                            df_result_statistical["مقدار تجمعی میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"].cumsum(skipna=True).round(2) 
                            df_result_statistical["مجموع ماهانه"] = df_result.iloc[:,1:].sum(axis=1).round(2)
                            df_result_statistical["مقدار تجمعی مجموع ماهانه"] = df_result_statistical["مجموع ماهانه"].cumsum(skipna=True).round(2)
                            df_result = df_result_statistical.copy()
                        elif para == "WATER_TABLE_DIFF_MONTLY_YEARLY":
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
                        title_dic[para] + " - چاه " + wells[0],
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
    # ACTIVE DOWNLOAD BUTTON - TAB2 BODY CONTENT2
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('DOWNLOAD_TABLE_BUTTON-TAB2_BODY_CONTENT2', 'disabled'),
        Input('STATE_TABLE_DOWNLOAD_BUTTON-TAB2_SIDEBAR', 'children'),
    )
    def FUNCTION_ACTIVE_DOWNLOAD_TABLE_BUTTON_TAB1_BODY_CONTENT2(state_table):
        if state_table:
            return False
        else:
            return True


    # -----------------------------------------------------------------------------
    # TABLE DOWNLOAD - TAB2 BODY CONTENT2
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('DOWNLOAD_TABLE_COMPONENT-TAB2_BODY_CONTENT2', 'data'),
        Output('DOWNLOAD_TABLE_BUTTON-TAB2_BODY_CONTENT2', 'n_clicks'),
        Input('DOWNLOAD_TABLE_BUTTON-TAB2_BODY_CONTENT2', 'n_clicks'),
        Input('DATA_TABLE_WELL_STORE-TAB2_BODY_CONTENT2', 'data'),
        prevent_initial_call=True,
    )
    def FUNCTION_DOWNLOAD_TABLE_COMPONENT_TAB1_BODY_CONTENT2(n, data):
        if n != 0 and data is not None:
            result = [
                dcc.send_data_frame(pd.DataFrame.from_dict(data).to_excel, "DataTable.xlsx", sheet_name="Sheet1", index=False),
                0
            ]
            return result
        else:
            raise PreventUpdate