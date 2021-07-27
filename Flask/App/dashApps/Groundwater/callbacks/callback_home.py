import os
import sqlite3
import pandas as pd
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash_html_components.Hr import Hr
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash_extensions.javascript import arrow_function
import pyproj

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_table
import geojson


from App.dashApps.Groundwater.callbacks.data_analysis import *




def groundwater_callback_home(app):


    @app.callback(
        Output("SIDEBAR-TAB_HOME", "className"),
        Output("BODY-TAB_HOME", "className"),
        Output("SIDEBAR_STATE-TAB_HOME", "data"),
        Output("SIDEBAR_BUTTON-TAB_HOME_BODY", "className"),
        Input("SIDEBAR_BUTTON-TAB_HOME_BODY", "n_clicks"),
        State("SIDEBAR_STATE-TAB_HOME", "data")
    )
    def FUNCTION_TOGGLE_SIDEBAR_TAB_HOME_SIDEBAR(n, nclick):
        if n:
            if nclick == "SHOW":
                sidebar_style = "SIDEBAR-HIDEN"
                content_style = "CONTENT-WITHOUT-SIDEBAR"
                cur_nclick = "HIDDEN"
                btn_classname = "fas fa-align-justify fa-2x BTN-SIDEBAR-CLOSE"
            else:
                sidebar_style = "SIDEBAR-SHOW"
                content_style = "CONTENT-WITH-SIDEBAR"
                cur_nclick = "SHOW"
                btn_classname = "fas fa-angle-double-right fa-3x BTN-SIDEBAR-OPEN"
        else:
            sidebar_style = "SIDEBAR-HIDEN"
            content_style = "CONTENT-WITHOUT-SIDEBAR"
            cur_nclick = 'HIDDEN'
            btn_classname = "fas fa-align-justify fa-2x BTN-SIDEBAR-CLOSE"
                

        return sidebar_style, content_style, cur_nclick, btn_classname


    @app.callback(
        Output("COLLAPSE_BODY-TAB_HOME_SIDEBAR_COLLAPSE_BASE_MAP", "is_open"),
        Output("ARROW-TAB_HOME_SIDEBAR_COLLAPSE_BASE_MAP", "className"),
        Output("COLLAPSE_BODY-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP", "is_open"),
        Output("ARROW-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP", "className"),
        Output("COLLAPSE_BODY-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP", "is_open"),
        Output("ARROW-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP", "className"),
        
        Input("OPEN_CLOSE-TAB_HOME_SIDEBAR_COLLAPSE_BASE_MAP", "n_clicks"),
        Input("OPEN_CLOSE-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP", "n_clicks"),
        Input("OPEN_CLOSE-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP", "n_clicks"),
        State("COLLAPSE_BODY-TAB_HOME_SIDEBAR_COLLAPSE_BASE_MAP", "is_open"),
        State("COLLAPSE_BODY-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP", "is_open"),
        State("COLLAPSE_BODY-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP", "is_open"),
    )
    def FUNCTION_TOGGLE_ACCORDION_TAB_HOME_SIDEBAR(
        n_bace_map, n_political_map, n_water_map,
        state_base_map, state_political_map, state_water_map,
    ):
        ctx = dash.callback_context

        if not ctx.triggered:
            return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

        else:
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            
            if button_id == "OPEN_CLOSE-TAB_HOME_SIDEBAR_COLLAPSE_BASE_MAP" and n_bace_map:
                if not state_base_map:
                    return True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP" and n_political_map:
                if not state_political_map:
                    return False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP" and n_water_map:
                if not state_water_map:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            else:
                return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"


    @app.callback(
        Output("BASE_MAP-TAB_HOME_BODY", "url"),

        Output("NONEBASEMAP_BASE_MAP-TAB_HOME_BODY", "style"),
        Output("STREETS_BASE_MAP-TAB_HOME_BODY", "style"),
        Output("IMAGERY_BASE_MAP-TAB_HOME_BODY", "style"),
        Output("TERRAIN_BASE_MAP-TAB_HOME_BODY", "style"),
        Output("TOPOGRAPHIC_BASE_MAP-TAB_HOME_BODY", "style"),
        Output("DARK_BASE_MAP-TAB_HOME_BODY", "style"),

        Input("NONEBASEMAP_BASE_MAP-TAB_HOME_BODY", "n_clicks"),
        Input("STREETS_BASE_MAP-TAB_HOME_BODY", "n_clicks"),
        Input("IMAGERY_BASE_MAP-TAB_HOME_BODY", "n_clicks"),
        Input("TERRAIN_BASE_MAP-TAB_HOME_BODY", "n_clicks"),
        Input("TOPOGRAPHIC_BASE_MAP-TAB_HOME_BODY", "n_clicks"),
        Input("DARK_BASE_MAP-TAB_HOME_BODY", "n_clicks"),
    )
    def FUNCTION_UPDATE_BASE_MAP_TAB_HOME_BODY(
        n_nonebasemap, n_streets, n_imagery, n_terrain, n_topo, n_dark
    ):
        ctx = dash.callback_context
        if not ctx.triggered:
            raise PreventUpdate
        else:
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            if button_id == "NONEBASEMAP_BASE_MAP-TAB_HOME_BODY" and n_nonebasemap:
                return NONEBASEMAP_URL, BASE_MAP_SELECTED_STYLE, None, None, None, None, None
            elif button_id == "STREETS_BASE_MAP-TAB_HOME_BODY" and n_streets:
                return STREETS_URL, None, BASE_MAP_SELECTED_STYLE, None, None, None, None
            elif button_id == "IMAGERY_BASE_MAP-TAB_HOME_BODY" and n_imagery:
                return IMAGERY_URL, None, None, BASE_MAP_SELECTED_STYLE, None, None, None
            elif button_id == "TERRAIN_BASE_MAP-TAB_HOME_BODY" and n_terrain:
                return TERRAIN_URL, None, None, None, BASE_MAP_SELECTED_STYLE, None, None
            elif button_id == "TOPOGRAPHIC_BASE_MAP-TAB_HOME_BODY" and n_topo:
                return TOPOGRAPHIC_URL, None, None, None, None, BASE_MAP_SELECTED_STYLE, None
            elif button_id == "DARK_BASE_MAP-TAB_HOME_BODY" and n_dark:
                return DARK_URL, None, None, None, None, None, BASE_MAP_SELECTED_STYLE
            else:
                raise PreventUpdate


    @app.callback(
        Output("BASE_MAP-TAB_HOME_BODY", "opacity"),
        Output("BADGE_OPACITY_BASE_MAP-TAB_HOME_SIDEBAR", "children"),
        Input("OPACITY_BASE_MAP-TAB_HOME_SIDEBAR", "value"),
    )
    def FUNCTION_UPDATE_OPACITY_BASE_MAP_TAB_HOME_BODY(
        opacity
    ):
        opacity = int(opacity)
        return opacity / 100, f"{str(opacity)}%"


    @app.callback(
        Output("MAP-TAB_HOME_BODY", "children"),   
        Input("ADD_POLITICAL_MAP-TAB_HOME_SIDEBAR", "value"),
        Input("ADD_WATER_MAP-TAB_HOME_SIDEBAR", "value"),
        State("MAP-TAB_HOME_BODY", "children"),
        State("ADD_WATER_MAP-TAB_HOME_SIDEBAR", "value"),
    )
    def FUNCTION_ADD_SELECTED_GEOJSON_MAP_TAB_HOME_SIDEBAR(
        political_map_value, water_map_value,
        map_children_state, water_map_state
    ):

        if (not political_map_value) & (not water_map_value):
            map_value = None
        elif (not political_map_value):
            map_value = water_map_value
        elif (not water_map_value):
            map_value = political_map_value
        else:
            map_value = political_map_value + water_map_value

        if not map_value:
            result = map_children_state[:4]
            return result
        
        result = map_children_state[:4]

        for i in map_value:

            print(GEOJSON_LOCATION[i]["url"])

            with open(GEOJSON_LOCATION[i]["url"]) as f:
                data = geojson.load(f)

            data = dlx.geojson_to_geobuf(data)

            print(data)

            ID = f"{i}_MAP-TAB_HOME_BODY"

            result = result + [dl.GeoJSON(
                data=data,
                id=ID,
                format="geobuf",
                zoomToBounds=True,
                hoverStyle=arrow_function(
                    dict(
                        weight=10,
                        color="green",
                        dashArray=''
                    )
                ),
                options=GEOJSON_LOCATION[i]["options"],
                )
            ]

        return result


        
        













    @app.callback(
        Output("search_coordinate", "placeholder"),
        Input("select_coordinate", "value"),
    )
    def search_coordinate_placeholder(coordinate):    
        if coordinate == "LatLon":
            return "Lat: 36.30 Lon: 59.60"
        else:
            return "40S 433967 4016252"

    @app.callback(
        Output("layer", "children"),
        Output("search_coordinate", "value"),
        Output("map", "center"),
        Input("map", "dbl_click_lat_lng"),
        Input("search_coordinate", "value")
    )
    def map_dbl_click_or_search(dbl_click_lat_lng, search):    
        if search is None or search == "" and dbl_click_lat_lng:
            result = dl.Marker(
                children=dl.Tooltip(
                    "({:.3f}, {:.3f})".format(*dbl_click_lat_lng)
                ),
                position=dbl_click_lat_lng
            )
            return [result], "", dbl_click_lat_lng      
        else:
            search = list(
                filter(
                    ("").__ne__,
                    search.split(" ")
                )
            )

            search = [check_user_input(x) for x in search]

            print("1: ", search)

            if len(search) == 2 and all([isinstance(x, (int, float)) for x in search]):
                try:
                    search_lat_lng = [float(x) for x in search]
                    print("2: ", search_lat_lng)
                    result = dl.Marker(
                        children=dl.Tooltip(
                            "({:.2f}, {:.2f})".format(*search_lat_lng)
                        ),
                        position=search_lat_lng
                    )
                    return [result], "", search_lat_lng
                except:
                    raise PreventUpdate
            elif (len(search) == 4 or len(search) == 6) and all([isinstance(x, (int)) for x in search]):
                if len(search) == 6:
                    try:
                        lat = search[0] + (search[1]/60) + (search[2]/3600)
                        lng = search[3] + (search[4]/60) + (search[5]/3600)
                        search_lat_lng = [lat, lng]
                        print("3: ", search_lat_lng)
                        result = dl.Marker(
                            children=dl.Tooltip(
                                "({:.2f}, {:.2f})".format(*search_lat_lng)
                            ),
                            position=search_lat_lng
                        )
                        return [result], "", search_lat_lng
                    except:
                        raise PreventUpdate
                elif len(search) == 4:
                    try:
                        lat = search[0] + (search[1]/60)
                        lng = search[2] + (search[3]/60)
                        search_lat_lng = [lat, lng]
                        print("4: ", search_lat_lng)
                        result = dl.Marker(
                            children=dl.Tooltip(
                                "({:.2f}, {:.2f})".format(*search_lat_lng)
                            ),
                            position=search_lat_lng
                        )
                        return [result], "", search_lat_lng
                    except:
                        raise PreventUpdate
                else:
                    raise PreventUpdate
            elif len(search) == 3 and isinstance(search[0], (str)) and\
                all([isinstance(x, (int, float)) for x in search[1:3]]) and\
                    len(str(int(search[1]))) == 6 and len(str(int(search[2]))) == 7:
                try:
                    p = pyproj.Proj(proj='utm', ellps='WGS84', zone=int(search[0][0:2]))
                    p = p(float(search[1]), float(search[2]), inverse=True)
                    print("5: ", p)
                    result = dl.Marker(
                        children=dl.Tooltip(
                            "({:.2f}, {:.2f})".format(p[1], p[0])
                        ),
                        position=(p[1], p[0])
                    )
                    return [result], "", (p[1], p[0])
                except:
                    raise PreventUpdate
            else:
                raise PreventUpdate
                
        
    @app.callback(
        Output("info", "children"), 
        Input("hozeh6", "hover_feature"),
        Input("hozeh30", "hover_feature"),
        Input("mahdoude", "hover_feature"),
        Input("ostan", "hover_feature"),
        Input("shahrestan", "hover_feature"),
    )
    def ostan_click(
        f_hozeh6,
        f_hozeh30,
        f_mahdoude,
        f_ostan,
        f_shahrestan
    ):

        if f_hozeh6:
            return [
                html.Span("حوزه آبریز درجه یک"),
                html.H6(f_hozeh6['properties']['FULL_NAME']),
                html.Hr(className="mt-0 mb-1 py-0"),
                html.Span("کد حوزه آبریز: "),
                html.Span(f_hozeh6['properties']['CODE'], className="text-info"),
                html.Br(),
                html.Span("مساحت: "),
                html.Span(f"{int(round(f_hozeh6['properties']['AREA'],0))} کیلومتر مربع", className="text-info"),
                html.Br(),
                html.Span("محیط: "),
                html.Span(f"{int(round(f_hozeh6['properties']['PERIMETER'],0))} کیلومتر", className="text-info"),
            ]
        elif f_hozeh30:
            return [
                html.Span("حوزه آبریز درجه دو"),
                html.H6(f_hozeh30['properties']['FULL_NAME']),
                html.Hr(className="mt-0 mb-1 py-0"),
                html.Span("کد حوزه آبریز: "),
                html.Span(f_hozeh30['properties']['CODE'], className="text-info"),
                html.Br(),
                html.Span("مساحت: "),
                html.Span(f"{int(round(f_hozeh30['properties']['AREA'],0))} کیلومتر مربع", className="text-info"),
                html.Br(),
                html.Span("محیط: "),
                html.Span(f"{int(round(f_hozeh30['properties']['PERIMETER'],0))} کیلومتر", className="text-info"),
            ]
        elif f_mahdoude:
            return [
                html.Span("محدوده مطالعاتی"),
                html.H6(f_mahdoude['properties']['NAME']),
                html.Hr(className="mt-0 mb-1 py-0"),
                html.Span("کد محدوده مطالعاتی: "),
                html.Span(f_mahdoude['properties']['CODE'], className="text-info"),
                html.Br(),
                html.Span("امور: "),
                html.Span(f_mahdoude['properties']['OMOR'], className="text-info"),
                html.Br(),
                html.Span("مساحت: "),
                html.Span(f"{int(round(f_mahdoude['properties']['AREA'],0))} کیلومتر مربع", className="text-info"),
                html.Br(),
                html.Span("محیط: "),
                html.Span(f"{int(round(f_mahdoude['properties']['PERIMETER'],0))} کیلومتر", className="text-info"),
            ]
        elif f_ostan:
            return [
                html.Span("استان"),
                html.H6(f_ostan['properties']['NAME']),
                html.Hr(className="mt-0 mb-1 py-0"),
                html.Span("مساحت: "),
                html.Span(f"{int(round(f_ostan['properties']['AREA'],0))} کیلومتر مربع", className="text-info"),
                html.Br(),
                html.Span("محیط: "),
                html.Span(f"{int(round(f_ostan['properties']['PERIMETER'],0))} کیلومتر", className="text-info"),
            ]
        elif f_shahrestan:
            return [
                html.Span("شهرستان"),
                html.H6(f_shahrestan['properties']['NAME']),
                html.Hr(className="mt-0 mb-1 py-0"),
                html.Span("استان: "),
                html.Span(f_shahrestan['properties']['OSTAN'], className="text-info"),
                html.Br(),
                html.Span("مساحت: "),
                html.Span(f"{int(round(f_shahrestan['properties']['AREA'],0))} کیلومتر مربع", className="text-info"),
                html.Br(),
                html.Span("محیط: "),
                html.Span(f"{int(round(f_shahrestan['properties']['PERIMETER'],0))} کیلومتر", className="text-info"),
            ]
        else:
            return html.Span("موس را روی یک عارضه نگه دارید")


    @app.callback(
        Output("ostan", "children"),
        Input("ostan", "hover_feature"),
    )
    def oss(feature_ostan):
        if feature_ostan is not None:
            return dl.Tooltip(
                f"{feature_ostan['properties']['ostn_name']}"
            )
        else:
            raise PreventUpdate




    # df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
    # fig = px.scatter(df, x="gdp per capita", y="life expectancy",
    #                 size="population", color="continent", hover_name="country",
    #                 log_x=True, size_max=60)

    

    # df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    # fig2 = go.Figure([go.Scatter(x=df2['Date'], y=df2['AAPL.High'])])     
            

    # labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    # values = [4500, 2500, 1053, 500]
    # fig3 = go.Figure(data=[go.Pie(labels=labels, values=values)])

    # df4 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
    # fig4 = dash_table.DataTable(
    #     id='life4',
    #     columns=[{"name": i, "id": i} for i in df4.columns],
    #     data=df4.to_dict('records'),
    #     style_cell={
    #         'maxWidth': 80
    #     },
    #     style_table={'overflowX': 'auto', 'maxWidth': '600px'}
    # )

    # @app.callback(
    #     Output("modal", "is_open"),
    #     Output("modal_header", "children"),
    #     Output("modal_body", "children"),
    #     Input("ostan", "click_feature"),
    #     Input("mahdoude", "click_feature"),
    #     State("modal", "is_open"),
    # )
    # def toggle_modal(feature_ostan, feature_mahdoude, is_open):
    #     if feature_ostan is not None:
    #         return not is_open, f"{feature_ostan['properties']['ostn_name']}", html.Div([dcc.Graph(id='life', figure=fig)])

    #     elif feature_mahdoude is not None:
    #         return not is_open, f"{feature_mahdoude['properties']['MahName']}", html.Div([dcc.Graph(id='life', figure=fig2)])
    #     else:
    #         raise PreventUpdate


    # @app.callback(
    #     Output("modal2", "is_open"),
    #     Output("modal2_header", "children"),
    #     Output("modal2_body", "children"),
    #     Input("hozeh30", "click_feature"),
    #     State("modal2", "is_open"),
    # )
    # def toggle_modal2(feature_hozeh30, is_open):

    #     if feature_hozeh30 is not None:
    #         return not is_open, f"{feature_hozeh30['properties']['Hoze30Name']}", html.Div([dcc.Graph(id='life2', figure=fig3)])
    #     else:
    #         raise PreventUpdate
    

    # @app.callback(
    #     Output("modal3", "is_open"),
    #     Output("modal3_header", "children"),
    #     Output("modal3_body", "children"),
    #     Input("hozeh6", "click_feature"),
    #     State("modal3", "is_open"),
    # )
    # def toggle_modal3(feature_hozeh6, is_open):

    #     if feature_hozeh6 is not None:
    #         return not is_open, f"{feature_hozeh6['properties']['Hoze6Name']}", html.Div(fig4)
    #     else:
    #         raise PreventUpdate


    # -----------------------------------------------------------------------------
    # CONNECT TO SERVER DATABASE - COLLAPSE 1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("CONNECT_TO_SERVER_DATABASE-TAB_HOME_COLLAPSE1", "n_clicks"),    
        Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB_HOME_COLLAPSE1", "is_open"),
        Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB_HOME_COLLAPSE1", "icon"),
        Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB_HOME_COLLAPSE1", "header"),    
        Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB_HOME_COLLAPSE1", "children"),
        Output("POPUP_CONNECT_TO_SERVER_DATABASE-TAB_HOME_COLLAPSE1", "headerClassName"),
        Input("CONNECT_TO_SERVER_DATABASE-TAB_HOME_COLLAPSE1", "n_clicks")
    )
    def FUNCTION_CONNECT_TO_SERVER_DATABASE_TAB_HOME_COLLAPSE1(n):
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


    # -----------------------------------------------------------------------------
    # CONNECT TO SPREADSHEET FILE AND CREATE DATABASE - COLLAPSE 1
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("CONNECT_TO_SPREADSHEET-TAB_HOME_COLLAPSE1", "n_clicks"),
        Output("FILENAME_SPREADSHEET-TAB_HOME_COLLAPSE1", "children"),
        Output("FILENAME_SPREADSHEET-TAB_HOME_COLLAPSE1", "className"),
        Output("POPUP_CONNECT_TO_SPREADSHEET-TAB_HOME_COLLAPSE1", "is_open"),
        Output("POPUP_CONNECT_TO_SPREADSHEET-TAB_HOME_COLLAPSE1", "icon"),
        Output("POPUP_CONNECT_TO_SPREADSHEET-TAB_HOME_COLLAPSE1", "header"),
        Output("POPUP_CONNECT_TO_SPREADSHEET-TAB_HOME_COLLAPSE1", "children"),
        Output("POPUP_CONNECT_TO_SPREADSHEET-TAB_HOME_COLLAPSE1", "headerClassName"),
        Input('CONNECT_TO_SPREADSHEET-TAB_HOME_COLLAPSE1', 'n_clicks'),    
        Input('CHOOSE_SPREADSHEET-TAB_HOME_COLLAPSE1', 'contents'), 
        State('CHOOSE_SPREADSHEET-TAB_HOME_COLLAPSE1', 'filename')
    )
    def FUNCTION_CONNECT_TO_SPREADSHEET_TAB_HOME_COLLAPSE1(n, content, filename):
        if n != 0 and content is None:
            result = [
                0,
                "فایلی انتخاب نشده است!",
                "text-danger",
                True,
                None,
                "هشدار",
                "فایل صفحه گسترده‌ای انتخاب نشده است.",
                "popup-notification-header-warning"            
            ]
            return result
        elif n == 0 and content is not None:
            result = [
                0,
                "فایل انتخابی شما: " + filename,
                "text-success",
                False,
                None,
                None,
                None,
                None           
            ]
            return result
        elif n != 0 and content is not None:
            raw_data = read_spreadsheet(contents=content, filename=filename)
            data, data_aquifer = data_cleansing(
                well_info_data_all=raw_data['Info'],
                dtw_data_all=raw_data['Depth_To_Water'],
                thiessen_data_all=raw_data['Thiessen'],
                sc_data_all=raw_data['Storage_Coefficient']
            )
            db = sqlite3.connect(database="groundwater.sqlite")
            data.to_sql(name="RawAquiferDATA", con=db, if_exists="replace")
            data_aquifer.to_sql(name="AquiferDATA", con=db, if_exists="replace")
            result = [
                1,
                "فایل انتخابی شما: " + filename,
                "text-success",
                True,
                None,
                "موفقیت آمیز",
                "پایگاه داده با موفقیت ایجاد شد.",
                "popup-notification-header-success"            
            ]
            return result    
        else:
            result = [
                0,
                "فایلی انتخاب نشده است!",
                "text-danger",
                False,
                None,
                None,
                None,
                None           
            ]
            return result
