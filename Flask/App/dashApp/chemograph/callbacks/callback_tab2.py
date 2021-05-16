import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash.exceptions import PreventUpdate

from App.dashApp.chemograph.callbacks.database_config import *
from App.dashApp.chemograph.callbacks.initial_settings import *

def chemograph_callback_tab2(app):


    # -----------------------------------------------------------------------------
    # SELECT AQUIFER - TAB2 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Input("TABLE_RAWDATA-TAB1_SIDEBAR", "children")
    )
    def FUNCTION_SELECT_AQUIFER_TAB2_SIDEBAR_LEFT_CARD1(RAWDATA_TABLE):
        if RAWDATA_TABLE == "OK":
            GeoinformationDATA = pd.read_sql_query(sql="SELECT * FROM GeoinformationDATA", con=db)
            return [{"label": col, "value": col} for col in GeoinformationDATA['mahdodeh_name'].unique()]            
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
            GeoinformationDATA = pd.read_sql_query(sql="SELECT * FROM GeoinformationDATA", con=db)
            df = GeoinformationDATA[GeoinformationDATA["mahdodeh_name"].isin(aquifers)]
            return [{"label": col, "value": col} for col in df["mahal"].unique()]
        else:
            return []


    # -----------------------------------------------------------------------------
    # SELECT PARAMETER - TAB2 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('SELECT_PARAMETER-TAB2_SIDEBAR_LEFT_CARD1', 'options'),
        Input("TABLE_RAWDATA-TAB1_SIDEBAR", "children")
    )
    def FUNCTION_SELECT_PARAMETER_TAB2_SIDEBAR_LEFT_CARD1(RAWDATA_TABLE):
        if RAWDATA_TABLE == "OK":
            PARAMETER = {    
                "Ca{}{} (Calcium)".format(superscript_map["+"], superscript_map["2"]) : "ca",
                "Mg{}{} (Magnesium)".format(superscript_map["+"], superscript_map["2"]) : "mg",
                "Na{} (Sodium)".format(superscript_map["+"]) : "na",
                "K{} (Potassium)".format(superscript_map["+"]) : "k",
                "Cl{} (Chloride)".format(superscript_map["-"]) : "cl",
                "SO{}{}{} (Sulfate)".format(subscript_map["4"], superscript_map["2"], superscript_map["-"]) : "so4",
                "CO{}{}{} (Carbonate)".format(subscript_map["3"], superscript_map["2"], superscript_map["-"]) : "co3",
                "HCO{}{} (Bicarbonate)".format(subscript_map["3"], superscript_map["-"]) : "hco3",
                "NO{}{} (Nitrate)".format(subscript_map["3"], superscript_map["-"]) : "no3",
                "EC (Electrical Conductivity)" : "ec",
                "pH (Potential of Hydrogen)" : "ph"
            }
            return [{"label": label, "value": value} for label, value in PARAMETER.items()]           
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
        
            data = pd.read_sql_query(sql="SELECT * FROM GeoinformationDATA", con=db)
            
            return map_area_studies_wells(
                state="OK",
                data=data,
                shapefile_path=AQUIFERS,
                shapefile_mahdodeh_code_column='mah_code',
                selected_mahdodeh=aquifers,
                selected_wells=wells
            )        
        else:
            return map_area_studies_wells(
                state="NO"
            )  




    # -----------------------------------------------------------------------------
    # CREATE GRAPH - TAB2 BODY CONTENT1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GRAPH-TAB2_BODY_CONTENT1', 'figure'),   
        Input('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_PARAMETER-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    )
    def FUNCTION_GRAPH_TAB2_BODY_CONTENT1(aquifers, wells, start, end, para):
        if (aquifers is not None) and (len(aquifers) != 0) \
            and (wells is not None) and (len(wells) != 0) and (para is not None) and (len(para) != 0) \
                and (start is not None) and (end is not None):
                    data = pd.read_sql_query(sql="SELECT * FROM RawDATA", con=db)  
                    data = data[data["mahdodeh_name"].isin(aquifers)]                
                    data = data[data["mahal"].isin(wells)]                
                    data = data[data['year'] >= start]
                    data = data[data['year'] <= end]
                                
                    # PLOT
                    fig = go.Figure()
                                    
                    for well in wells:                    
                        df_well = data[data["mahal"] == well]                                     
                        fig.add_trace(
                            go.Scatter(
                                x=df_well['date'],
                                y=df_well[para],
                                mode='lines+markers',
                                line_shape='spline',
                                name=well,
                                # text=df_well[para],
                                # textfont=dict(
                                #     size=12,
                                #     color="Black",
                                # )
                            )
                        )
                        
                        # fig.update_traces(textposition='top center')
                    
                    if para == 'ec':
                        yaxis_title = "هدایت الکتریکی - میکروموس بر سانتی‌متر"
                        title = 'تغییرات هدایت الکتریکی'
                    else:
                        yaxis_title = ""
                        title = ""
                    

                    fig.update_layout(
                        margin={'l': 3, 'r': 3},
                        xaxis_title="تاریخ نمونه برداری",
                        yaxis_title=yaxis_title,
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
                            text=title,
                            yanchor="top",
                            y=0.95,
                            xanchor="center",
                            x=0.500
                        )
                    )
                    return fig
        else:
            return NO_MATCHING_DATA_FOUND





    # # -----------------------------------------------------------------------------
    # # WELL INFORMATION - TAB2 SIDEBAR RIGHT CARD1
    # # -----------------------------------------------------------------------------
    # @app.callback(
    #     Output('IMG_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'src'),    
    #     Output('NAME_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),    
    #     Output('ID_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),    
    #     Output('AQUIFER_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),    
    #     Output('LONG_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),    
    #     Output('LAT_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),    
    #     Output('ELEV_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),    
    #     Output('START_DATE_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),
    #     Output('END_DATE_OW-TAB2_SIDEBAR_RIGHT_CARD1', 'children'),
    #     Output('TAB_2_SIDEBAR_RIGHT', 'hidden'),
    #     Output('TAB_2_SIDEBAR_RIGHT', 'className'),
    #     Output('TAB_2_BODY', 'className'),
    #     Input('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    #     Input('SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1', 'value')
    # )
    # def FUNCTION_WELL_INFORMATION_TAB2_SIDEBAR_RIGHT_CARD1(aquifers, wells):
    #     if (aquifers is not None) and (len(aquifers) != 0) \
    #         and (wells is not None) and (len(wells) != 0):
    #             if (len(aquifers) == 1) and (len(wells) == 1):
    #                 data = RawDATA[RawDATA["Aquifer_Name"].isin(aquifers)]
    #                 data = data[data["Well_Name"].isin(wells)]
    #                 data['Date_Gregorian'] = pd.to_datetime(data['Date_Gregorian'])
    #                 data.reset_index(inplace = True)
    #                 # Img OW
    #                 if aquifers[0] == "جوین":
    #                     Img_OW = base64.b64encode(
    #                         open('assets/images/ow1.png', 'rb').read()
    #                     )
    #                     Img_OW_SRC = 'data:image/png;base64,{}'.format(Img_OW.decode())
    #                 else:
    #                     Img_OW = base64.b64encode(
    #                         open('assets/images/ow2.png', 'rb').read()
    #                     )
    #                     Img_OW_SRC = 'data:image/png;base64,{}'.format(Img_OW.decode())
                        
    #                 # Para
    #                 ID = str(data['ID'].values[0])
    #                 LAT = str(data['X_UTM'].values[0])
    #                 LONG = str(data['Y_UTM'].values[0])
    #                 ELEV = str(data['Final_Elevation'].values[0])
    #                 START_DATE = str(data['year_Date_Persian'].values[data["Date_Gregorian"].idxmin()])
    #                 END_DATE = str(data['year_Date_Persian'].values[data["Date_Gregorian"].idxmax()])
                    
                    
    #                 result = [
    #                     Img_OW_SRC,
    #                     wells[0],
    #                     "شناسه: " + ID,
    #                     "آبخوان: " + aquifers[0],
    #                     "طول جغرافیایی: " + LAT,
    #                     "عرض جغرافیایی: " + LONG,
    #                     "ارتفاع: " + ELEV + " متر",
    #                     "سال شروع دوره آماری: " + START_DATE,
    #                     "سال پایان دوره آماری: " + END_DATE,
    #                     False,
    #                     "right-sidebar",
    #                     'my-body pt-2'
    #                 ]
                    
    #                 return result
    #             else:
                    
    #                 Img_OW = base64.b64encode(
    #                     open('assets/images/placeholder.png', 'rb').read()
    #                 )  # EDITPATH
                    
    #                 result = [
    #                     'data:image/png;base64,{}'.format(Img_OW.decode()),
    #                     "نام چاه مشاهده‌ای",
    #                     "شناسه چاه مشاهده‌ای",
    #                     "نام آبخوان",
    #                     "طول جغرافیایی",
    #                     "عرض جغرافیایی",
    #                     "ارتفاع",
    #                     "سال شروع دوره آماری",
    #                     "سال پایان دوره آماری",
    #                     True,
    #                     "tab2-right-sidebar-hidden",
    #                     'tab2-right-sidebar-hidden-my-body pt-2'
    #                 ]
                    
    #                 return result
                    
    #     else:
            
    #         Img_OW = base64.b64encode(
    #             open('assets/images/placeholder.png', 'rb').read()
    #         )  # EDITPATH
            
    #         result = [
    #             'data:image/png;base64,{}'.format(Img_OW.decode()),
    #             "نام چاه مشاهده‌ای",
    #             "شناسه چاه مشاهده‌ای",
    #             "نام آبخوان",
    #             "طول جغرافیایی",
    #             "عرض جغرافیایی",
    #             "ارتفاع",
    #             "سال شروع دوره آماری",
    #             "سال پایان دوره آماری",
    #             True,
    #             "tab2-right-sidebar-hidden",
    #             'tab2-right-sidebar-hidden-my-body pt-2'
    #         ]
            
    #         return result





    # # -----------------------------------------------------------------------------
    # # TABLE - TAB2 BODY CONTENT2
    # # -----------------------------------------------------------------------------
    # @app.callback(
    #     Output('TABLE-TAB2_BODY_CONTENT2', 'data'),
    #     Output('TABLE-TAB2_BODY_CONTENT2', 'columns'),
    #     Output('TABLE_HEADER-TAB2_BODY_CONTENT2', 'children'),
    #     Output('STATE_TABLE_DOWNLOAD_BUTTON-TAB2_SIDEBAR', 'children'),
    #     Output('DATA_TABLE_WELL_STORE-TAB2_BODY_CONTENT2', 'data'),
    #     Input('SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    #     Input('SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1', 'value'),
    #     Input('SELECT_TYPE_YEAR-TAB2_SIDEBAR_LEFT_CARD2', 'value'),
    #     Input('SELECT_PARAMETER-TAB2_SIDEBAR_LEFT_CARD2', 'value'),
    #     Input('STATISTICAL_ANALYSIS-TAB2_SIDEBAR_LEFT_CARD2', 'value'),
    # )
    # def FUNCTION_TABLE_TAB2_BODY_CONTENT2(aquifers, wells, typeYear, para, statistical):
    #     if (aquifers is not None) and (len(aquifers) != 0) \
    #         and (wells is not None) and (len(wells) != 0):
    #             if (len(aquifers) == 1) and (len(wells) == 1):
    #                 data = RawDATA[RawDATA["Aquifer_Name"].isin(aquifers)]
    #                 data = data[data["Well_Name"].isin(wells)]
    #                 data.reset_index(inplace = True)
                    
    #                 df_tmp = data[["year_Date_Persian", "month_Date_Persian", "Well_Head"]]
    #                 df_tmp.columns = ["سال", "ماه", "پارامتر"]
    #                 df_tmp = resultTable(df_tmp)
    #                 df_tmp.columns = ["سال", "ماه", "تراز ماهانه سطح آب زیرزمینی", "سال آبی", "ماه آبی", "تغییرات هر ماه نسبت به ماه قبل", "تغییرات هر ماه نسبت به ماه سال قبل"]
                    
                    
    #                 para_dic = {
    #                     "WATER_TABLE_MONTLY" : "تراز ماهانه سطح آب زیرزمینی",
    #                     "WATER_TABLE_DIFF_MONTLY" : "تغییرات هر ماه نسبت به ماه قبل",
    #                     "WATER_TABLE_DIFF_MONTLY_YEARLY" : "تغییرات هر ماه نسبت به ماه سال قبل",
    #                 }
                    
    #                 title_dic = {
    #                     "WATER_TABLE_MONTLY" : "تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی (متر)",
    #                     "WATER_TABLE_DIFF_MONTLY" : "تغییرات ماهانه (هر ماه نسبت به ماه قبل) تراز سطح آب زیرزمینی (متر)",
    #                     "WATER_TABLE_DIFF_MONTLY_YEARLY" : "تغییرات ماهانه (هر ماه در سال جاری نسبت به ماه متناظر در سال قبل) تراز سطح آب زیرزمینی (متر)",
    #                 }                

    #                 if typeYear == "WATER_YEAR":
    #                     df_result = df_tmp.pivot_table(
    #                         values=para_dic[para],
    #                         index="سال آبی",
    #                         columns="ماه آبی"
    #                     ).reset_index()
    #                     df_result.columns = ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]
    #                 else:
    #                     df_result = df_tmp.pivot_table(
    #                         values=para_dic[para],
    #                         index="سال",
    #                         columns="ماه"
    #                     ).reset_index()
    #                     df_result.columns = ["سال شمسی", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
                    
    #                 df_result_statistical = df_result.copy()
                    
    #                 if statistical is not None and 'STATISTICAL_ANALYSIS' in statistical:
    #                     if para == "WATER_TABLE_MONTLY":
    #                         df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
    #                         df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
    #                         df_result_statistical["مقدار میانگین"] = df_result.iloc[:,1:].mean(axis=1).round(2)
    #                         df_result = df_result_statistical.copy()
    #                     elif para == "WATER_TABLE_DIFF_MONTLY":
    #                         df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
    #                         df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
    #                         df_result_statistical["مقدار میانگین سالانه"] = df_result.iloc[:,1:].mean(axis=1).round(2)
    #                         df_result_statistical["مقدار تجمعی میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"].cumsum(skipna=True).round(2) 
    #                         df_result_statistical["مجموع ماهانه"] = df_result.iloc[:,1:].sum(axis=1).round(2)
    #                         df_result_statistical["مقدار تجمعی مجموع ماهانه"] = df_result_statistical["مجموع ماهانه"].cumsum(skipna=True).round(2)
    #                         df_result = df_result_statistical.copy()
    #                     elif para == "WATER_TABLE_DIFF_MONTLY_YEARLY":
    #                         df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
    #                         df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
    #                         df_result_statistical["مقدار میانگین سالانه"] = df_result.iloc[:,1:].mean(axis=1).round(2)
    #                         df_result_statistical["تغییرات مقدار میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"] - df_result_statistical["مقدار میانگین سالانه"].shift(1)
    #                         df_result_statistical["تغییرات مقدار میانگین سالانه"] = df_result_statistical["تغییرات مقدار میانگین سالانه"].round(2)
    #                         df_result_statistical["مقدار تجمعی میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"].cumsum(skipna=True).round(2)
    #                         if typeYear == "WATER_YEAR":
    #                             df_result_statistical["مقدار تجمعی (مهر تا مهر)"] = df_result["مهر"].cumsum(skipna=True).round(2)
    #                         df_result = df_result_statistical.copy()
                            
    #                 result = [
    #                     df_result.to_dict('records'),
    #                     [{"name": i, "id": i} for i in df_result.columns],
    #                     title_dic[para] + " - چاه " + wells[0],
    #                     True,
    #                     df_result.to_dict('records')
    #                 ]
                    
    #                 return result
    #             else:  
    #                 zz = ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]              
    #                 result = [
    #                     [{}],
    #                     [{"name": i, "id": i} for i in zz],
    #                     "تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی (متر)",
    #                     False,
    #                     None
    #                 ]                
    #                 return result 
    #     else:
    #         zz = ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]
    #         result = [
    #             [{}],
    #             [{"name": i, "id": i} for i in zz],
    #             "تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی (متر)",
    #             False,
    #             None
    #         ]
    #         return result



    # # -----------------------------------------------------------------------------
    # # ACTIVE DOWNLOAD BUTTON - TAB2 BODY CONTENT2
    # # -----------------------------------------------------------------------------
    # @app.callback(
    #     Output('DOWNLOAD_TABLE_BUTTON-TAB2_BODY_CONTENT2', 'disabled'),
    #     Input('STATE_TABLE_DOWNLOAD_BUTTON-TAB2_SIDEBAR', 'children'),
    # )
    # def FUNCTION_ACTIVE_DOWNLOAD_TABLE_BUTTON_TAB1_BODY_CONTENT2(state_table):
    #     if state_table:
    #         return False
    #     else:
    #         return True


    # # -----------------------------------------------------------------------------
    # # TABLE DOWNLOAD - TAB2 BODY CONTENT2
    # # -----------------------------------------------------------------------------
    # @app.callback(
    #     Output('DOWNLOAD_TABLE_COMPONENT-TAB2_BODY_CONTENT2', 'data'),
    #     Output('DOWNLOAD_TABLE_BUTTON-TAB2_BODY_CONTENT2', 'n_clicks'),
    #     Input('DOWNLOAD_TABLE_BUTTON-TAB2_BODY_CONTENT2', 'n_clicks'),
    #     Input('DATA_TABLE_WELL_STORE-TAB2_BODY_CONTENT2', 'data'),
    #     prevent_initial_call=True,
    # )
    # def FUNCTION_DOWNLOAD_TABLE_COMPONENT_TAB1_BODY_CONTENT2(n, data):
    #     if n != 0 and data is not None:
    #         result = [
    #             dcc.send_data_frame(pd.DataFrame.from_dict(data).to_excel, "DataTable.xlsx", sheet_name="Sheet1", index=False),
    #             1
    #         ]
    #         return result
    #     else:
    #         raise PreventUpdate