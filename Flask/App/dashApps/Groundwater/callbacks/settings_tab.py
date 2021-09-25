import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, MATCH, ALL, ALLSMALLER
from dash.exceptions import PreventUpdate

from App.dashApps.Groundwater.callbacks.config import *


def groundwater_callback_settings_tab(app):
    
    
    # -----------------------------------------------------------------------------
    # CONNECT TO IP SERVER DATABASE - TAB SETTINGS BODY
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("SUBMIT_IP_SERVER_DATABASE-TAB_SETTINGS_BODY", "n_clicks"),    
        Output("IP_SERVER_DATABASE-TAB_SETTINGS_BODY", "value"),
        Output("POPUP_IP_SERVER_DATABASE-TAB_SETTINGS_BODY", "is_open"),
        Output("POPUP_IP_SERVER_DATABASE-TAB_SETTINGS_BODY", "icon"),
        Output("POPUP_IP_SERVER_DATABASE-TAB_SETTINGS_BODY", "header"),    
        Output("POPUP_IP_SERVER_DATABASE-TAB_SETTINGS_BODY", "children"),
        Output("POPUP_IP_SERVER_DATABASE-TAB_SETTINGS_BODY", "headerClassName"),
        Input("SUBMIT_IP_SERVER_DATABASE-TAB_SETTINGS_BODY", "n_clicks"),
        State("IP_SERVER_DATABASE-TAB_SETTINGS_BODY", "value"),
    )
    def FUNCTION_CONNECT_TO_IP_SERVER_DATABASE_TAB_SETTINGS_BODY(n, ip_address):
        if n != 0:
            result = [
                0,
                "",
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
                "",
                False,
                None,
                None,
                None,
                None          
            ]
            return result
        
        
    # -----------------------------------------------------------------------------
    # CONNECT TO SPREADSHEET FILE AND CREATE DATABASE - TAB SETTINGS BODY
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("SUBMIT_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY", "n_clicks"),        
        Output("CHOOSEED_FILE_NAME-TAB_SETTINGS_BODY", "children"),
        Output("CHOOSEED_FILE_NAME-TAB_SETTINGS_BODY", "style"),                
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY", "is_open"),
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY", "icon"),
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY", "header"),
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY", "children"),
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY", "headerClassName"),        
        Output('CHOOSE_SPREADSHEET-TAB_SETTINGS_BODY', 'contents'),
        Output('SELECT_GEOINFO_WORKSHEET_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY', 'options'),
        Output('SELECT_DATA_WORKSHEET_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY', 'options'),
        Output('RAW_DATA-TAB_HOME_BODY', 'data'),
        Output('INPUT_GEOINFO_TABLE_NAME-TAB_SETTINGS_BODY', 'value'),
        Output('INPUT_DATA_TABLE_NAME-TAB_SETTINGS_BODY', 'value'),       
        Output('INTERVAL_COMPONENT_SELECT_TABLE_DATA_CLEANSING-TAB_HOME_BODY', 'n_intervals'),       
                      
        Input("SUBMIT_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY", "n_clicks"),        
        Input('CHOOSE_SPREADSHEET-TAB_SETTINGS_BODY', 'contents'),
        State('INPUT_GEOINFO_TABLE_NAME-TAB_SETTINGS_BODY', 'value'),
        State('INPUT_DATA_TABLE_NAME-TAB_SETTINGS_BODY', 'value'),
        State('CHOOSE_SPREADSHEET-TAB_SETTINGS_BODY', 'contents'),
        State('CHOOSE_SPREADSHEET-TAB_SETTINGS_BODY', 'filename'),
        State('SELECT_GEOINFO_WORKSHEET_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY', 'value'),
        State('SELECT_DATA_WORKSHEET_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY', 'value'),      
        State('SELECT_GEOINFO_WORKSHEET_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY', 'options'),
        State('SELECT_DATA_WORKSHEET_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY', 'options'),
        State('RAW_DATA-TAB_HOME_BODY', 'data'),      
    )
    def FUNCTION_CONNECT_TO_SPREADSHEET_DATABASE_TAB_SETTINGS_BODY(
        submit_btn, content,
        GEOINFO_TABLE_NAME, DATA_TABLE_NAME,
        state_content, filename, 
        GEOINFO_WORKSHEET_NAME, DATA_WORKSHEET_NAME,
        GEOINFO_WORKSHEET_OPTIONS, DATA_WORKSHEET_OPTIONS,
        RAW_DATA
    ):

        if (submit_btn != 0 and content is None):
            result = [
                0,
                "فایلی انتخاب نشده است!",
                {'direction': 'rtl', 'color': 'red', 'text-align': 'right'},
                True,
                None,
                "هشدار",
                "فایل صفحه گسترده‌ای انتخاب نشده است.",
                "popup-notification-header-warning",
                None,
                [],
                [],
                None,       
                [],                   
                [],
                0      
            ]
            return result
        
        elif submit_btn == 0 and content is not None:
            
            raw_data, worksheet_name = read_spreadsheet(contents=content, filename=filename)
                     
            if worksheet_name is None:
                result = [
                    0,
                    "فایلی انتخاب نشده است!",
                    {'direction': 'rtl', 'color': 'red', 'text-align': 'right'},
                    True,
                    None,
                    "اخطار",
                    "تعداد کاربرگ‏‌های فایل ورودی باید حداقل دو عدد باشند.",
                    "popup-notification-header-danger",
                    None,      
                    [],
                    [],
                    None,     
                    [],                   
                    [],
                    0     
                ]
                return result

            result = [
                0,
                f"{filename[0:12]}...{filename[-8:]}" if len(filename) > 20 else filename,
                {'direction': 'ltr', 'color': 'green', 'text-align': 'left'},
                False,
                None,
                None,
                None,
                None,
                state_content,
                [{'label': wn, 'value': wn} for wn in worksheet_name],
                [{'label': wn, 'value': wn} for wn in worksheet_name],
                raw_data,
                GEOINFO_TABLE_NAME,
                DATA_TABLE_NAME,
                0
                
            ]
            return result
        
        elif submit_btn != 0 and content is not None:
            
            if (GEOINFO_WORKSHEET_NAME is None) | (DATA_WORKSHEET_NAME is None):
                result = [
                    1,
                    f"{filename[0:12]}...{filename[-8:]}" if len(filename) > 20 else filename,
                    {'direction': 'ltr', 'color': 'green', 'text-align': 'left'},
                    True,
                    None,
                    "هشدار",
                    "کاربرگ مشخصات یا کاربرگ داده‌ها انتخاب نشده است!",
                    "popup-notification-header-warning",
                    state_content,
                    GEOINFO_WORKSHEET_OPTIONS,
                    DATA_WORKSHEET_OPTIONS,
                    RAW_DATA,
                    GEOINFO_TABLE_NAME,
                    DATA_TABLE_NAME,
                    0             
                ]
                return result 
            
            elif GEOINFO_WORKSHEET_NAME == DATA_WORKSHEET_NAME:
                result = [
                    1,
                    f"{filename[0:12]}...{filename[-8:]}" if len(filename) > 20 else filename,
                    {'direction': 'ltr', 'color': 'green', 'text-align': 'left'},
                    True,
                    None,
                    "هشدار",
                    "کاربرگ مشخصات و کاربرگ داده‌ها نمی‌توانند یکسان باشند!",
                    "popup-notification-header-warning",
                    state_content,
                    GEOINFO_WORKSHEET_OPTIONS,
                    DATA_WORKSHEET_OPTIONS,
                    RAW_DATA,
                    GEOINFO_TABLE_NAME,
                    DATA_TABLE_NAME,
                    0
                                 
                ]
                return result
            
            elif set(RAW_DATA[GEOINFO_WORKSHEET_NAME].keys()) != set(HydrographDataSample_GeoInfoColumns):
                result = [
                    0,
                    "فایلی انتخاب نشده است!",
                    {'direction': 'rtl', 'color': 'red', 'text-align': 'right'},
                    True,
                    None,
                    "اخطار",
                    "سر ستون‌های «کاربرگ مشخصات» با فایل نمونه همخوانی ندارند!",
                    "popup-notification-header-danger",
                    None,
                    [],
                    [],
                    None,
                    [],                   
                    [], 
                    0 
                                   
                ]
                return result
            
            elif set(RAW_DATA[DATA_WORKSHEET_NAME].keys()) != set(HydrographDataSample_DataColumns):
                result = [
                    0,
                    "فایلی انتخاب نشده است!",
                    {'direction': 'rtl', 'color': 'red', 'text-align': 'right'},
                    True,
                    None,
                    "اخطار",
                    "سر ستون‌های «کاربرگ داده‌ها» با فایل نمونه همخوانی ندارند!",
                    "popup-notification-header-danger",
                    None,
                    [],
                    [],
                    None,              
                    [],                   
                    [],  
                    0              
                ]
                return result
            
            elif (GEOINFO_TABLE_NAME is None) | (DATA_TABLE_NAME is None) | (GEOINFO_TABLE_NAME == "") | (DATA_TABLE_NAME == ""):
                result = [
                    1,
                    f"{filename[0:12]}...{filename[-8:]}" if len(filename) > 20 else filename,
                    {'direction': 'ltr', 'color': 'green', 'text-align': 'left'},
                    True,
                    None,
                    "هشدار",
                    "نام جداول نمی‌تواند خالی باشد!",
                    "popup-notification-header-warning",
                    state_content,
                    GEOINFO_WORKSHEET_OPTIONS,
                    DATA_WORKSHEET_OPTIONS,
                    RAW_DATA,
                    GEOINFO_TABLE_NAME,
                    DATA_TABLE_NAME,
                    0             
                ]
                return result 
            
            elif GEOINFO_TABLE_NAME == DATA_TABLE_NAME:
                result = [
                    1,
                    f"{filename[0:12]}...{filename[-8:]}" if len(filename) > 20 else filename,
                    {'direction': 'ltr', 'color': 'green', 'text-align': 'left'},
                    True,
                    None,
                    "هشدار",
                    "نام جداول نمی‌تواند یکسان باشند!",
                    "popup-notification-header-warning",
                    state_content,
                    GEOINFO_WORKSHEET_OPTIONS,
                    DATA_WORKSHEET_OPTIONS,
                    RAW_DATA,
                    GEOINFO_TABLE_NAME,
                    DATA_TABLE_NAME,
                    0              
                ]
                return result
            
            elif (not all(c in EN_CHAR for c in GEOINFO_TABLE_NAME)) | (not all(c in EN_CHAR for c in DATA_TABLE_NAME)):
                result = [
                    1,
                    f"{filename[0:12]}...{filename[-8:]}" if len(filename) > 20 else filename,
                    {'direction': 'ltr', 'color': 'green', 'text-align': 'left'},
                    True,
                    None,
                    "هشدار",
                    "در نامگذاری جداول فقط می‌توان از حروف کوچک و بزرگ انگلیسی، اعداد و خط زیر استفاده کرد!",
                    "popup-notification-header-warning",
                    state_content,
                    GEOINFO_WORKSHEET_OPTIONS,
                    DATA_WORKSHEET_OPTIONS,
                    RAW_DATA,
                    GEOINFO_TABLE_NAME,
                    DATA_TABLE_NAME,
                    0
                ]
                return result
            
            elif (GEOINFO_TABLE_NAME.lower() in [i.lower() for i in list(pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", DB_GROUNDWATER).name)]) |\
                ((GEOINFO_TABLE_NAME.lower() + "_raw") in [i.lower() for i in list(pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", DB_GROUNDWATER).name)]):
                result = [
                    1,
                    f"{filename[0:12]}...{filename[-8:]}" if len(filename) > 20 else filename,
                    {'direction': 'ltr', 'color': 'green', 'text-align': 'left'},
                    True,
                    None,
                    "هشدار",
                    f"در پایگاه داده جدولی با نام {GEOINFO_TABLE_NAME} موجود می‌باشد!",
                    "popup-notification-header-warning",
                    state_content,
                    GEOINFO_WORKSHEET_OPTIONS,
                    DATA_WORKSHEET_OPTIONS,
                    RAW_DATA,
                    "",
                    DATA_TABLE_NAME,
                    0
                ]
                return result
            
            elif (DATA_TABLE_NAME.lower() in [i.lower() for i in list(pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", DB_GROUNDWATER).name)]) |\
                ((DATA_TABLE_NAME.lower() + "_raw") in [i.lower() for i in list(pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", DB_GROUNDWATER).name)]):
                result = [
                    1,
                    f"{filename[0:12]}...{filename[-8:]}" if len(filename) > 20 else filename,
                    {'direction': 'ltr', 'color': 'green', 'text-align': 'left'},
                    True,
                    None,
                    "هشدار",
                    f"در پایگاه داده جدولی با نام {DATA_TABLE_NAME} موجود می‌باشد!",
                    "popup-notification-header-warning",
                    state_content,
                    GEOINFO_WORKSHEET_OPTIONS,
                    DATA_WORKSHEET_OPTIONS,
                    RAW_DATA,
                    GEOINFO_TABLE_NAME,
                    "",
                    0
                ]
                return result
            

            pd.DataFrame.from_dict(RAW_DATA[GEOINFO_WORKSHEET_NAME]).to_sql(
                name=GEOINFO_TABLE_NAME.lower() + "_raw",
                con=DB_GROUNDWATER,
                if_exists="replace"
            )
            
            
            pd.DataFrame.from_dict(RAW_DATA[DATA_WORKSHEET_NAME]).to_sql(
                name=DATA_TABLE_NAME.lower() + "_raw",
                con=DB_GROUNDWATER,
                if_exists="replace"
            )

                
            result = [
                0,
                "فایلی انتخاب نشده است!",
                {'direction': 'rtl', 'color': 'red', 'text-align': 'right'},
                True,
                None,
                "موفقیت آمیز",
                "پایگاه داده با موفقیت ایجاد شد.",
                "popup-notification-header-success",
                None,
                [],
                [],
                None,                   
                [],                   
                [],
                0                   
            ]
            return result 
             
        else:
            result = [
                0,
                "فایلی انتخاب نشده است!",
                {'direction': 'rtl', 'color': 'red', 'text-align': 'right'},
                False,
                None,
                None,
                None,
                None,
                None,        
                [],
                [],
                None,        
                [],                   
                [],
                0         
            ]
            return result


    # -----------------------------------------------------------------------------
    # DATA CLEANSING - TAB SETTINGS BODY
    # -----------------------------------------------------------------------------
    
    # SECTION 1:
    # ----------
    
    @app.callback(
        Output('SELECT_GEOINFO_TABLE_DATA_CLEANSING-TAB_SETTINGS_BODY', 'options'),
        Output('SELECT_DATA_TABLE_DATA_CLEANSING-TAB_SETTINGS_BODY', 'options'),
        Input("INTERVAL_COMPONENT_SELECT_TABLE_DATA_CLEANSING-TAB_HOME_BODY", "n_intervals"),
    )
    def FUNCTION_SELECT_TABLE_NAME_DATA_CLEANSING_TAB_SETTINGS_BODY(
        n
    ):
        DB_GROUNDWATER_TABELS = list(
            pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", DB_GROUNDWATER).name
        )
                     
        result = [
            [{'label': t, 'value': t} for t in DB_GROUNDWATER_TABELS],
            [{'label': t, 'value': t} for t in DB_GROUNDWATER_TABELS],
        ]
        
        return result


    # SECTION 3:
    # ----------
    
    @app.callback(
        Output('SELECT_ORDER_INTERPOLATE_METHOD_DATA_CLEANSING-TAB_SETTINGS_BODY', 'disabled'),
        Input('SELECT_INTERPOLATE_METHOD_DATA_CLEANSING-TAB_SETTINGS_BODY', 'value'),
    )
    def FUNCTION_SELECT_ORDER_INTERPOLATE_METHOD_DATA_CLEANSING(
        method
    ):
        if method in ["polynomial", "spline"]:
            return False
        else:
            return True
        
    
    @app.callback(
        Output('output_id', 'output_prop'),
        Input('input_id', 'input_prop')
    )
    def fn(input_prop):
        return
    
    
    # SUBMIT BTN:
    # ----------
    
    @app.callback(
        Output('SUBMIT_DATACLEANSING-TAB_SETTINGS_BODY', 'n_clicks'),
        Output("POPUP_DATA_CLEANSING_DATABASE-TAB_SETTINGS_BODY", "is_open"),
        Output("POPUP_DATA_CLEANSING_DATABASE-TAB_SETTINGS_BODY", "icon"),
        Output("POPUP_DATA_CLEANSING_DATABASE-TAB_SETTINGS_BODY", "header"),
        Output("POPUP_DATA_CLEANSING_DATABASE-TAB_SETTINGS_BODY", "children"),
        Output("POPUP_DATA_CLEANSING_DATABASE-TAB_SETTINGS_BODY", "headerClassName"),
        
        Input("SUBMIT_DATACLEANSING-TAB_SETTINGS_BODY", "n_clicks"),        
        Input("SELECT_GEOINFO_TABLE_DATA_CLEANSING-TAB_SETTINGS_BODY", "value"),
        Input("SELECT_DATA_TABLE_DATA_CLEANSING-TAB_SETTINGS_BODY", "value"),        
        Input("SELECT_DATE_TYPE_DATA_CLEANSING-TAB_SETTINGS_BODY", "value"),        
        Input("SELECT_INTERPOLATE_METHOD_DATA_CLEANSING-TAB_SETTINGS_BODY", "value"),
        Input("SELECT_ORDER_INTERPOLATE_METHOD_DATA_CLEANSING-TAB_SETTINGS_BODY", "value"),        
        Input("SELECT_LIMIT_DATA_CLEANSING-TAB_SETTINGS_BODY", "value"),
        Input("THIESSEN_CALCULATION_DATA_CLEANSING-TAB_SETTINGS_BODY", "value"),
    )
    def FUNCTION_SUBMIT_DATACLEANSING_TAB_SETTINGS_BODY(
        submit_btn, geoinfo, data, date_type, interpolate, order, interpolate_limit, thiessen
    ):
        if (submit_btn != 0) and (geoinfo is None) and (data is None):
            result = [
                0,
                True,
                None,
                "هشدار",
                "جدول داده‌ها یا جدول مشخصات انتخاب نشده‌اند!",
                "popup-notification-header-warning",
            ]
            return results
        elif (submit_btn != 0) and (geoinfo is not None) and (data is not None) :
            print(submit_btn, geoinfo, data, date_type, interpolate, order, interpolate_limit, thiessen)
            result = [
                0,
                True,
                None,
                "موفقیت آمیز",
                "پایگاه داده با موفقیت به روزرسانی شد.",
                "popup-notification-header-success",
            ]
            return result
        else:
            result = [
                0,
                False,
                None,
                None,
                None,
                None,
            ]
            return result