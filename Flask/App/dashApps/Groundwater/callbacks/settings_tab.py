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
        Output("SUBMIT_IP_SERVER_DATABASE-TAB_SETTING_BODY", "n_clicks"),    
        Output("IP_SERVER_DATABASE-TAB_SETTING_BODY", "value"),
        Output("POPUP_IP_SERVER_DATABASE-TAB_SETTING_BODY", "is_open"),
        Output("POPUP_IP_SERVER_DATABASE-TAB_SETTING_BODY", "icon"),
        Output("POPUP_IP_SERVER_DATABASE-TAB_SETTING_BODY", "header"),    
        Output("POPUP_IP_SERVER_DATABASE-TAB_SETTING_BODY", "children"),
        Output("POPUP_IP_SERVER_DATABASE-TAB_SETTING_BODY", "headerClassName"),
        Input("SUBMIT_IP_SERVER_DATABASE-TAB_SETTING_BODY", "n_clicks"),
        State("IP_SERVER_DATABASE-TAB_SETTING_BODY", "value"),
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
        Output("SUBMIT_SPREADSHEET_DATABASE-TAB_SETTING_BODY", "n_clicks"),
        Output("CLOSE_SPREADSHEET_DATABASE_MODEL-TAB_SETTING_BODY", "n_clicks"),        
        Output("CHOOSEED_FILE_NAME-TAB_SETTING_BODY", "children"),
        Output("CHOOSEED_FILE_NAME-TAB_SETTING_BODY", "className"),        
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_SETTING_BODY", "is_open"),
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_SETTING_BODY", "icon"),
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_SETTING_BODY", "header"),
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_SETTING_BODY", "children"),
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_SETTING_BODY", "headerClassName"),        
        Output("SPREADSHEET_DATABASE_MODEL-TAB_SETTING_BODY", "is_open"),
        Output('CHOOSE_SPREADSHEET-TAB_SETTING_BODY', 'contents'),
               
        Input("SUBMIT_SPREADSHEET_DATABASE-TAB_SETTING_BODY", "n_clicks"),
        Input("CLOSE_SPREADSHEET_DATABASE_MODEL-TAB_SETTING_BODY", "n_clicks"),
        Input('CHOOSE_SPREADSHEET-TAB_SETTING_BODY', 'contents'),
        State('CHOOSE_SPREADSHEET-TAB_SETTING_BODY', 'contents'),
        State('CHOOSE_SPREADSHEET-TAB_SETTING_BODY', 'filename'),
        State("CHOOSEED_FILE_NAME-TAB_SETTING_BODY", "children"),
        State("SPREADSHEET_DATABASE_MODEL-TAB_SETTING_BODY", "is_open")
    )
    def FUNCTION_CONNECT_TO_SPREADSHEET_DATABASE_TAB_SETTING_BODY(
        submit_btn, close_btn, content, state_content, filename, file_name_location, is_open
    ):
        if submit_btn != 0 and content is None:
            result = [
                0,
                0,
                file_name_location,
                "font-weight-light",
                True,
                None,
                "هشدار",
                "فایل صفحه گسترده‌ای انتخاب نشده است.",
                "popup-notification-header-warning",
                is_open,
                None         
            ]
            return result
        elif submit_btn == 0 and content is not None:
            result = [
                0,
                0,
                f"{filename[0:12]}..." if len(filename) >= 15 else filename,
                "font-weight-light text-success",
                False,
                None,
                None,
                None,
                None,
                is_open,
                state_content          
            ]
            return result
        elif submit_btn != 0 and content is not None:
            # raw_data = read_spreadsheet(contents=content, filename=filename)
            # data, data_aquifer = data_cleansing(
            #     well_info_data_all=raw_data['Info'],
            #     dtw_data_all=raw_data['Depth_To_Water'],
            #     thiessen_data_all=raw_data['Thiessen'],
            #     sc_data_all=raw_data['Storage_Coefficient']
            # )
            # db = sqlite3.connect(database="groundwater.sqlite")
            # data.to_sql(name="RawAquiferDATA", con=db, if_exists="replace")
            # data_aquifer.to_sql(name="AquiferDATA", con=db, if_exists="replace")
            if close_btn != 0:
                result = [
                    0,
                    0,
                    ['انتخاب فایل', html.I(className="fas fa-cloud-upload-alt ml-2")],
                    "font-weight-light",
                    False,
                    None,
                    None,
                    None,
                    None,
                    not is_open,
                    None        
                ]
                return result
            else:
                result = [
                    1,
                    0,
                    file_name_location,
                    "font-weight-light text-success",
                    False,
                    None,
                    None,
                    None,
                    None,
                    not is_open,
                    state_content        
                ]
                return result      
        else:
            result = [
                0,
                0,
                file_name_location,
                "font-weight-light",
                False,
                None,
                None,
                None,
                None,
                is_open,
                None         
            ]
            return result
    