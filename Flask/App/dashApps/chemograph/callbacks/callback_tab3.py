import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash.exceptions import PreventUpdate

from App.dashApp.chemograph.callbacks.database_config import *
from App.dashApp.chemograph.callbacks.initial_settings import *

def chemograph_callback_tab3(app):

    # -----------------------------------------------------------------------------
    # CALCULATE CHEMOGRAPH - TAB3 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("POPUP_CALCULATE_AQUIFER_CHEMOGRAPH-TAB3_SIDEBAR_CARD1", "is_open"),
        Output("POPUP_CALCULATE_AQUIFER_CHEMOGRAPH-TAB3_SIDEBAR_CARD1", "icon"),
        Output("POPUP_CALCULATE_AQUIFER_CHEMOGRAPH-TAB3_SIDEBAR_CARD1", "header"),
        Output("POPUP_CALCULATE_AQUIFER_CHEMOGRAPH-TAB3_SIDEBAR_CARD1", "children"),
        Output("POPUP_CALCULATE_AQUIFER_CHEMOGRAPH-TAB3_SIDEBAR_CARD1", "headerClassName"),
        Output("CALCULATE_AQUIFER_CHEMOGRAPH-TAB3_SIDEBAR_LEFT_CARD1", "n_clicks"),
        Output("STATE_TABLE_CHEMOGHRAP-TAB3_SIDEBAR", "children"),
        Input("TABLE_RAWDATA-TAB1_SIDEBAR", "children"),
        Input("CALCULATE_AQUIFER_CHEMOGRAPH-TAB3_SIDEBAR_LEFT_CARD1", "n_clicks")
    )
    def FUNCTION_CALCULATE_AQUIFER_CHEMOGRAPH_TAB3_SIDEBAR_LEFT_CARD1(RAWDATA_TABLE, n):
        if RAWDATA_TABLE == "OK" and n != 0:
            
            raw_data = pd.read_sql_query(sql="SELECT * FROM RawDATA", con=db)
            para = ["ca", "mg", "na", "k", "cl", "so4", "co3", "hco3", "no3", "ec", "ph"]
            
            for p in para:
                raw_data[p] = raw_data[p] * raw_data["mahal_area"] / raw_data["mahdodeh_area"]
            
            
            data = raw_data.groupby(['mahdodeh_name', 'date']).agg(
                {
                    'ca': 'sum',
                    'mg': 'sum',
                    'na': 'sum',
                    'k': 'sum',
                    'cl': 'sum',
                    'so4': 'sum',
                    'co3': 'sum',
                    'hco3': 'sum',
                    'no3': 'sum',
                    'ec': 'sum',
                    'ph': 'sum',
                }
            ).reset_index()
            
            data[['year', 'month', 'day']] = data['date'].str.split("-", n=2, expand=True)
            data['year'] = data['year'].astype(int)
            data['month'] = data['month'].astype(int)
            data['day'] = data['day'].astype(int)
            data.sort_values(['mahdodeh_name', 'year', 'month', 'day'], inplace=True)
            data.to_sql(name="ChemoGRAPH", con=db, if_exists="replace")
            
            
            result = [
                True,
                None,
                "موفقیت آمیز",
                "محاسبات با موفقیت انجام شد.",
                "popup-notification-header-success",
                1,
                "OK"        
            ]
            return result   
        elif RAWDATA_TABLE != "OK" and n != 0:
            result = [
                True,
                None,
                "خطا",
                "هیچ جدولی در پایگاه داده‌ای موجود نمی‌باشد.",
                "popup-notification-header-danger",
                0,
                "NO"          
            ]
            return result
        else:
            result = [
                False,
                None,
                None,
                None,
                None,
                0,
                "NO"          
            ]
            return result
            

    # -----------------------------------------------------------------------------
    # SELECT AQUIFER - TAB3 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('SELECT_AQUIFER-TAB3_SIDEBAR_LEFT_CARD1', 'options'),
        Input("STATE_TABLE_CHEMOGHRAP-TAB3_SIDEBAR", "children")
    )
    def FUNCTION_SELECT_AQUIFER_TAB3_SIDEBAR_LEFT_CARD1(CHEMOGRAPH_TABLE):
        if CHEMOGRAPH_TABLE == "OK":
            GeoinformationDATA = pd.read_sql_query(sql="SELECT * FROM GeoinformationDATA", con=db)
            return [{"label": col, "value": col} for col in GeoinformationDATA['mahdodeh_name'].unique()]            
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
            GeoinformationDATA = pd.read_sql_query(sql="SELECT * FROM GeoinformationDATA", con=db)
            df = GeoinformationDATA[GeoinformationDATA["mahdodeh_name"].isin(aquifers)]
            return [{"label": col, "value": col} for col in df["mahal"].unique()]
        else:
            return []



    # -----------------------------------------------------------------------------
    # SELECT PARAMETER - TAB3 SIDEBAR LEFT CARD1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('SELECT_PARAMETER-TAB3_SIDEBAR_LEFT_CARD1', 'options'),
        Input("STATE_TABLE_CHEMOGHRAP-TAB3_SIDEBAR", "children")
    )
    def FUNCTION_SELECT_PARAMETER_TAB3_SIDEBAR_LEFT_CARD1(CHEMOGRAPH_TABLE):
        if CHEMOGRAPH_TABLE == "OK":
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
            
            data = pd.read_sql_query(sql="SELECT * FROM GeoinformationDATA", con=db)
            
            
            if (wells is not None) and (len(wells) != 0):        
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
                    state="OK",
                    data=data,
                    shapefile_path=AQUIFERS,
                    shapefile_mahdodeh_code_column='mah_code',
                    selected_mahdodeh=aquifers,
                    selected_wells='all'
                )
                    
        else:
            return map_area_studies_wells(state="NO") 



    # -----------------------------------------------------------------------------
    # CREATE GRAPH - TAB3 BODY CONTENT1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GRAPH-TAB3_BODY_CONTENT1', 'figure'),   
        Input('SELECT_AQUIFER-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_WELL-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_START_YEAR-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_END_YEAR-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
        Input('SELECT_PARAMETER-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
    )
    def FUNCTION_GRAPH_TAB3_BODY_CONTENT1(aquifers, wells, start, end, para):
        if (aquifers is not None) and (len(aquifers) != 0) \
            and (para is not None) and (len(para) != 0) \
                and (start is not None) and (end is not None):
                    data_mahdodeh = pd.read_sql_query(sql="SELECT * FROM ChemoGRAPH", con=db)  
                    data_mahdodeh = data_mahdodeh[data_mahdodeh["mahdodeh_name"].isin(aquifers)]                
                    data_mahdodeh = data_mahdodeh[data_mahdodeh['year'] >= start]
                    data_mahdodeh = data_mahdodeh[data_mahdodeh['year'] <= end]
                                

                    # PLOT
                    fig = go.Figure()            
                                
                    for mah in aquifers:                    
                        df_mah = data_mahdodeh[data_mahdodeh["mahdodeh_name"] == mah]                                     
                        fig.add_trace(
                            go.Scatter(
                                x=df_mah['date'],
                                y=df_mah[para],
                                mode='lines+markers',
                                line_shape='spline',
                                name=mah,
                                # text=df_mah[para],
                                # textfont=dict(
                                #     size=12,
                                #     color="Black",
                                # )
                            )
                        )
                        
                        # fig.update_traces(textposition='top center')
                    
                    if para == 'ec':
                        yaxis_title = "هدایت الکتریکی - میکروموس بر سانتی‌متر"
                        title = 'تغییرات میزان هدایت الکتریکی آبخوان'
                    else:
                        yaxis_title = ""
                        title = ""

                    if (wells is not None) and (len(wells) != 0):
                        data_wells = pd.read_sql_query(sql="SELECT * FROM RawDATA", con=db)
                        data_wells = data_wells[data_wells["mahdodeh_name"].isin(aquifers)]
                        data_wells = data_wells[data_wells["mahal"].isin(wells)]
                        data_wells = data_wells[data_wells['year'] >= start]
                        data_wells = data_wells[data_wells['year'] <= end]
                        for well in wells:                    
                            data_well = data_wells[data_wells["mahal"] == well]                                   
                            fig.add_trace(
                                go.Scatter(
                                    x=data_well['date'],
                                    y=data_well[para],
                                    mode='lines+markers',
                                    name=well
                                )
                            )
                    

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
    # # TABLE - TAB3 BODY CONTENT2
    # # -----------------------------------------------------------------------------
    # @app.callback(
    #     Output('TABLE-TAB3_BODY_CONTENT2', 'data'),
    #     Output('TABLE-TAB3_BODY_CONTENT2', 'columns'),
    #     Output('TABLE_HEADER-TAB3_BODY_CONTENT2', 'children'),
    #     Output('STATE_TABLE_DOWNLOAD_BUTTON-TAB3_SIDEBAR', 'children'),
    #     Output('DATA_TABLE_WELL_STORE-TAB3_BODY_CONTENT2', 'data'),
    #     Input('SELECT_AQUIFER-TAB3_SIDEBAR_LEFT_CARD1', 'value'),
    #     Input('SELECT_TYPE_YEAR-TAB3_SIDEBAR_LEFT_CARD2', 'value'),
    #     Input('SELECT_PARAMETER-TAB3_SIDEBAR_LEFT_CARD2', 'value'),
    #     Input('STATISTICAL_ANALYSIS-TAB3_SIDEBAR_LEFT_CARD2', 'value'),
    # )
    # def FUNCTION_TABLE_TAB3_BODY_CONTENT2(aquifers, typeYear, para, statistical):
    #     if (aquifers is not None) and (len(aquifers) != 0):
    #         if (len(aquifers) == 1):
    #             data = AquiferDATA[AquiferDATA["Aquifer_Name"].isin(aquifers)]
    #             data.reset_index(inplace = True)
                
    #             df_tmp = data[["year_Date_Persian", "month_Date_Persian", "Adjusted_Aquifer_Head", "Aquifer_Area", "Aquifer_Storage_Coefficient"]]
    #             df_tmp.columns = ["سال", "ماه", "هد", "مساحت", "ضریب"]
    #             df_tmp = resultTableAquifer(df_tmp)
    #             df_tmp.columns = ["سال", "ماه", "تراز ماهانه سطح آب زیرزمینی", "مساحت شبکه تیسن", "ضریب ذخیره", "سال آبی", "ماه آبی", "تغییرات هر ماه نسبت به ماه قبل", "تغییرات هر ماه نسبت به ماه سال قبل"]
    #             df_tmp["تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"] = df_tmp["تغییرات هر ماه نسبت به ماه قبل"] * df_tmp["مساحت شبکه تیسن"] * df_tmp["ضریب ذخیره"]
    #             df_tmp["تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"] = df_tmp["تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"].round(2)
    #             df_tmp["تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"] = df_tmp["تغییرات هر ماه نسبت به ماه سال قبل"] * df_tmp["مساحت شبکه تیسن"] * df_tmp["ضریب ذخیره"]
    #             df_tmp["تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"] = df_tmp["تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"] .round(2)
                
    #             df_tmp.to_csv("dddsdsdsd.csv")
                
    #             para_dic = {
    #                 "WATER_TABLE_MONTLY" : "تراز ماهانه سطح آب زیرزمینی",
    #                 "WATER_TABLE_DIFF_MONTLY" : "تغییرات هر ماه نسبت به ماه قبل",
    #                 "WATER_TABLE_DIFF_MONTLY_YEARLY" : "تغییرات هر ماه نسبت به ماه سال قبل",
    #                 "STOREG_DIFF_MONTLY" : "تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل",
    #                 "STOREG_DIFF_MONTLY_YEARLY" : "تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"
    #             }
                
    #             title_dic = {
    #                 "WATER_TABLE_MONTLY" : "تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی (متر)",
    #                 "WATER_TABLE_DIFF_MONTLY" : "تغییرات ماهانه (هر ماه نسبت به ماه قبل) تراز سطح آب زیرزمینی (متر)",
    #                 "WATER_TABLE_DIFF_MONTLY_YEARLY" : "تغییرات ماهانه (هر ماه در سال جاری نسبت به ماه متناظر در سال قبل) تراز سطح آب زیرزمینی (متر)",
    #                 "STOREG_DIFF_MONTLY" : "متوسط تغییرات ماهانه (هر ماه نسبت به ماه قبل) ذخیره در آبخوان (میلیون متر مکعب)",
    #                 "STOREG_DIFF_MONTLY_YEARLY" : "تغییرات ماهانه (هر ماه در سال جاری نسبت به ماه متناظر در سال قبل) ذخیره در آبخوان (میلیون متر مکعب)",
    #             }                

    #             if typeYear == "WATER_YEAR":
    #                 df_result = df_tmp.pivot_table(
    #                     values=para_dic[para],
    #                     index="سال آبی",
    #                     columns="ماه آبی"
    #                 ).reset_index()
    #                 df_result.columns = ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]
    #             else:
    #                 df_result = df_tmp.pivot_table(
    #                     values=para_dic[para],
    #                     index="سال",
    #                     columns="ماه"
    #                 ).reset_index()
    #                 df_result.columns = ["سال شمسی", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
                
    #             df_result_statistical = df_result.copy()
                
    #             if statistical is not None:
    #                 if para == "WATER_TABLE_MONTLY":
    #                     df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
    #                     df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
    #                     df_result_statistical["مقدار میانگین"] = df_result.iloc[:,1:].mean(axis=1).round(2)
    #                     df_result = df_result_statistical.copy()
    #                 elif para == "WATER_TABLE_DIFF_MONTLY" or para == "STOREG_DIFF_MONTLY":
    #                     df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
    #                     df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
    #                     df_result_statistical["مقدار میانگین سالانه"] = df_result.iloc[:,1:].mean(axis=1).round(2)
    #                     df_result_statistical["مقدار تجمعی میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"].cumsum(skipna=True).round(2) 
    #                     df_result_statistical["مجموع ماهانه"] = df_result.iloc[:,1:].sum(axis=1).round(2)
    #                     df_result_statistical["مقدار تجمعی مجموع ماهانه"] = df_result_statistical["مجموع ماهانه"].cumsum(skipna=True).round(2)
    #                     df_result = df_result_statistical.copy()
    #                 elif para == "WATER_TABLE_DIFF_MONTLY_YEARLY" or para == "STOREG_DIFF_MONTLY_YEARLY":
    #                     df_result_statistical["مقدار حداکثر"] = df_result.iloc[:,1:].max(axis=1).round(2)
    #                     df_result_statistical["مقدار حداقل"] = df_result.iloc[:,1:].min(axis=1).round(2)
    #                     df_result_statistical["مقدار میانگین سالانه"] = df_result.iloc[:,1:].mean(axis=1).round(2)
    #                     df_result_statistical["تغییرات مقدار میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"] - df_result_statistical["مقدار میانگین سالانه"].shift(1)
    #                     df_result_statistical["تغییرات مقدار میانگین سالانه"] = df_result_statistical["تغییرات مقدار میانگین سالانه"].round(2)
    #                     df_result_statistical["مقدار تجمعی میانگین سالانه"] = df_result_statistical["مقدار میانگین سالانه"].cumsum(skipna=True).round(2)
    #                     if typeYear == "WATER_YEAR":
    #                         df_result_statistical["مقدار تجمعی (مهر تا مهر)"] = df_result["مهر"].cumsum(skipna=True).round(2)
    #                     df_result = df_result_statistical.copy()
                        
    #             result = [
    #                 df_result.to_dict('records'),
    #                 [{"name": i, "id": i} for i in df_result.columns],
    #                 title_dic[para] + " - آبخوان " + aquifers[0],
    #                 True,
    #                 df_result.to_dict('records')
    #             ]
                
    #             return result
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
    # # ACTIVE DOWNLOAD BUTTON - TAB3 BODY CONTENT2
    # # -----------------------------------------------------------------------------
    # @app.callback(
    #     Output('DOWNLOAD_TABLE_BUTTON-TAB3_BODY_CONTENT2', 'disabled'),
    #     Input('STATE_TABLE_DOWNLOAD_BUTTON-TAB3_SIDEBAR', 'children'),
    # )
    # def FUNCTION_ACTIVE_DOWNLOAD_TABLE_BUTTON_TAB1_BODY_CONTENT2(state_table):
    #     if state_table:
    #         return False
    #     else:
    #         return True


    # # -----------------------------------------------------------------------------
    # # TABLE DOWNLOAD - TAB3 BODY CONTENT2
    # # -----------------------------------------------------------------------------
    # @app.callback(
    #     Output('DOWNLOAD_TABLE_COMPONENT-TAB3_BODY_CONTENT2', 'data'),
    #     Output('DOWNLOAD_TABLE_BUTTON-TAB3_BODY_CONTENT2', 'n_clicks'),
    #     Input('DOWNLOAD_TABLE_BUTTON-TAB3_BODY_CONTENT2', 'n_clicks'),
    #     Input('DATA_TABLE_WELL_STORE-TAB3_BODY_CONTENT2', 'data'),
    #     prevent_initial_call=True,
    # )
    # def FUNCTION_DOWNLOAD_TABLE_COMPONENT_TAB1_BODY_CONTENT2(n, data):
    #     if n != 0 and data is not None:
    #         result = [
    #             dcc.send_data_frame(pd.DataFrame.from_dict(data).to_excel, "DataTableAquifer.xlsx", sheet_name="Sheet1", index=False),
    #             1
    #         ]
    #         return result
    #     else:
    #         raise PreventUpdate