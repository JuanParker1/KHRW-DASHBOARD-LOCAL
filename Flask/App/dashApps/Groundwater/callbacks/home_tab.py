import os
import sqlite3
import pandas as pd
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH, ALL, ALLSMALLER
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
import ast
import time
import utm

from App.dashApps.Groundwater.callbacks.config import *




def groundwater_callback_home_tab(app):


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
                btn_classname = "BTN-SIDEBAR-CLOSE"
            else:
                sidebar_style = "SIDEBAR-SHOW"
                content_style = "CONTENT-WITH-SIDEBAR"
                cur_nclick = "SHOW"
                btn_classname = "BTN-SIDEBAR-OPEN"
        else:
            sidebar_style = "SIDEBAR-HIDEN"
            content_style = "CONTENT-WITHOUT-SIDEBAR"
            cur_nclick = 'HIDDEN'
            btn_classname = "BTN-SIDEBAR-CLOSE"

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
        Output("MAP_ITEM-TAB_HOME_BODY", "data"),
        Output("NUMBER_SELECTED_POLITICAL_MAP-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP", "children"),
        Output("NUMBER_SELECTED_WATER_MAP-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP", "children"),
        Input("ADD_POLITICAL_MAP-TAB_HOME_SIDEBAR", "value"),
        Input("ADD_WATER_MAP-TAB_HOME_SIDEBAR", "value"),
        Input("INTERVAL_COMPONENT-TAB_HOME_BODY", "n_intervals"),
        State("MAP-TAB_HOME_BODY", "children"),
        State("ADD_WATER_MAP-TAB_HOME_SIDEBAR", "value"),
    )
    def FUNCTION_ADD_SELECTED_GEOJSON_MAP_TAB_HOME_SIDEBAR(
        political_map_value, water_map_value, n,
        map_children_state, water_map_state
    ):
        if (not political_map_value) & (not water_map_value):
            map_items = []
        elif (not political_map_value):
            map_items = water_map_value
        elif (not water_map_value):
            map_items = political_map_value
        else:
            map_items = political_map_value + water_map_value

        if not map_items:
            result = map_children_state[:8]
            map_items = []
            return result, map_items, 0, 0
        result = map_children_state[:8]

        for i in map_items:

            NEW_MAP = dl.GeoJSON(
                data=GEOJSON_LOCATION[i]["data"],
                id={
                    'type': '*_MAP-TAB_HOME_BODY',
                    'index': i
                },
                format="geobuf",
                zoomToBounds=True,
                hoverStyle=arrow_function(
                    dict(
                        color="green",
                        weight=10,
                        fillColor="green",
                        fillOpacity=0.2,
                    )
                ),
                options=GEOJSON_LOCATION[i]["options"],
            )

            result.append(NEW_MAP)

        return result, map_items,\
            0 if not political_map_value else len(political_map_value),\
                0 if not water_map_value else len(water_map_value)


    @app.callback(
        Output("MAP_INFO-TAB_HOME_BODY", "children"),
        Input({"type": "*_MAP-TAB_HOME_BODY", 'index': ALL}, 'hover_feature')
    )
    def FUNCTION_MAP_INFO_TAB_HOME_BODY(
        maps
    ):
        map_name = eval(dash.callback_context.triggered[0]["prop_id"].split('.')[0])["index"]
        if dash.callback_context.triggered[0]['value']:
            map_properties = dash.callback_context.triggered[0]['value']['properties']
            if map_name == "BASIN1":
                return [
                    html.Span("حوزه آبریز درجه یک"),
                    html.H6(map_properties['FULL_NAME']),
                    html.Hr(className="mt-0 mb-1 py-0"),
                    html.Span("کد حوزه آبریز: "),
                    html.Span(map_properties['CODE'], className="text-info"),
                    html.Br(),
                    html.Span("مساحت: "),
                    html.Span(f"{int(round(map_properties['AREA'],0))} کیلومتر مربع", className="text-info"),
                    html.Br(),
                    html.Span("محیط: "),
                    html.Span(f"{int(round(map_properties['PERIMETER'],0))} کیلومتر", className="text-info"),
                ]
            elif map_name == "BASIN2":
                return [
                    html.Span("حوزه آبریز درجه دو"),
                    html.H6(map_properties['FULL_NAME']),
                    html.Hr(className="mt-0 mb-1 py-0"),
                    html.Span("کد حوزه آبریز: "),
                    html.Span(map_properties['CODE'], className="text-info"),
                    html.Br(),
                    html.Span("مساحت: "),
                    html.Span(f"{int(round(map_properties['AREA'],0))} کیلومتر مربع", className="text-info"),
                    html.Br(),
                    html.Span("محیط: "),
                    html.Span(f"{int(round(map_properties['PERIMETER'],0))} کیلومتر", className="text-info"),
                ]
            elif map_name == "MAHDOUDE":
                return [
                    html.Span("محدوده مطالعاتی"),
                    html.H6(map_properties['NAME']),
                    html.Hr(className="mt-0 mb-1 py-0"),
                    html.Span("کد محدوده مطالعاتی: "),
                    html.Span(map_properties['CODE'], className="text-info"),
                    html.Br(),
                    html.Span("امور: "),
                    html.Span(map_properties['OMOR'], className="text-info"),
                    html.Br(),
                    html.Span("مساحت: "),
                    html.Span(f"{int(round(map_properties['AREA'],0))} کیلومتر مربع", className="text-info"),
                    html.Br(),
                    html.Span("محیط: "),
                    html.Span(f"{int(round(map_properties['PERIMETER'],0))} کیلومتر", className="text-info"),
                ]
            elif map_name == "AQUIFER":
                return [
                    html.Span("آبخوان"),
                    html.H6(map_properties['AQUIFER_NAME']),
                    html.Hr(className="mt-0 mb-1 py-0"),
                    html.Span("محدوده مطالعاتی: "),
                    html.Span(map_properties['MAHDOUDE_NAME'], className="text-info"),
                    html.Br(),
                    html.Span("کد محدوده مطالعاتی: "),
                    html.Span(map_properties['MAHDOUDE_CODE'], className="text-info"),
                    html.Br(),
                    html.Span("مساحت: "),
                    html.Span(f"{int(round(map_properties['AREA'],0))} کیلومتر مربع", className="text-info"),
                ]
            elif map_name == "COUNTRY":
                return [
                    html.Span("کشور"),
                    html.H6(map_properties['NAME']),
                    html.Hr(className="mt-0 mb-1 py-0"),
                    html.Span("کد کشور: "),
                    html.Span(map_properties['CODE'], className="text-info"),
                ]
            elif map_name == "PROVINCE":
                return [
                    html.Span("استان"),
                    html.H6(map_properties['NAME']),
                    html.Hr(className="mt-0 mb-1 py-0"),
                    html.Span("کد استان: "),
                    html.Span(map_properties['CODE'], className="text-info"),
                ]
            elif map_name == "COUNTY":
                return [
                    html.Span("شهرستان"),
                    html.H6(map_properties['NAME']),
                    html.Hr(className="mt-0 mb-1 py-0"),
                    html.Span("استان: "),
                    html.Span(map_properties['OSTAN'], className="text-info"),
                    html.Br(),
                    html.Span("مساحت: "),
                    html.Span(f"{int(round(map_properties['AREA'],0))} کیلومتر مربع", className="text-info"),
                    html.Br(),
                    html.Span("محیط: "),
                    html.Span(f"{int(round(map_properties['PERIMETER'],0))} کیلومتر", className="text-info"),
                ]
            elif map_name == "DISTRICT":
                return [
                    html.Span("بخش"),
                    html.H6(map_properties['NAME']),
                    html.Hr(className="mt-0 mb-1 py-0"),
                    html.Span("شهرستان: "),
                    html.Span(map_properties['SHAHRESTAN'], className="text-info"),
                    html.Br(),
                    html.Span("استان: "),
                    html.Span(map_properties['OSTAN'], className="text-info"),
                    html.Br(),
                    html.Span("مساحت: "),
                    html.Span(f"{int(round(map_properties['AREA'],0))} کیلومتر مربع", className="text-info"),
                    html.Br(),
                    html.Span("محیط: "),
                    html.Span(f"{int(round(map_properties['PERIMETER'],0))} کیلومتر", className="text-info"),
                ]
            else:
                return html.Span("موس را روی یک عارضه نگه دارید")
        else:
            return html.Span("موس را روی یک عارضه نگه دارید")


    @app.callback(
        Output("CLICK_LAYER-TAB_HOME_BODY", "children"),
        Output("SEARCH-TAB_HOME_BODY", "value"),
        Output("MAP-TAB_HOME_BODY", "center"),
        Input("MAP-TAB_HOME_BODY", "dbl_click_lat_lng"),
        Input("SEARCH-TAB_HOME_BODY", "value")
    )
    def map_dbl_click_or_search(dbl_click_lat_lng, search):

        if (search is None or search == "") and (dbl_click_lat_lng is not None):
            latlong_to_utm = utm.from_latlon(dbl_click_lat_lng[0], dbl_click_lat_lng[1])
            result = dl.Marker(
                children=dl.Tooltip(
                    html.Div(
                        [
                            html.Span("Lat: {:.2f}, Long: {:.2f}".format(dbl_click_lat_lng[0], dbl_click_lat_lng[1]), className="p-0 m-1"),
                            html.Hr(className="p-0 m-1"),
                            html.Span("{}{} {:.2f} {:.2f}".format(latlong_to_utm[2], latlong_to_utm[3], latlong_to_utm[0], latlong_to_utm[1]), className="p-0 m-1")
                        ],
                        className="text-center"
                    ),
                    direction="center"
                ),
                position=dbl_click_lat_lng,
            )
            return [result], "", dbl_click_lat_lng

        else:
            if (search is not None and search != ""):

                search = list(
                    filter(
                        ("").__ne__,
                        search.split(" ")
                    )
                )

                search = [check_user_input(x) for x in search]

                if len(search) == 2 and all([isinstance(x, (int, float)) for x in search]):
                    try:
                        search_lat_lng = [float(x) for x in search]
                        latlong_to_utm = utm.from_latlon(search_lat_lng[0], search_lat_lng[1])
                        result = dl.Marker(
                            children=dl.Tooltip(
                                html.Div(
                                    [
                                        html.Span("Lat: {:.2f}, Long: {:.2f}".format(search_lat_lng[0], search_lat_lng[1]), className="p-0 m-1"),
                                        html.Hr(className="p-0 m-1"),
                                        html.Span("{}{} {:.2f} {:.2f}".format(latlong_to_utm[2], latlong_to_utm[3], latlong_to_utm[0], latlong_to_utm[1]), className="p-0 m-1")
                                    ],
                                    className="text-center p-0 m-1"
                                ),
                                direction="center"
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
                            latlong_to_utm = utm.from_latlon(search_lat_lng[0], search_lat_lng[1])
                            result = dl.Marker(
                                children=dl.Tooltip(
                                    html.Div(
                                        [
                                            html.Span("Lat: {:.2f}, Long: {:.2f}".format(search_lat_lng[0], search_lat_lng[1]), className="p-0 m-1"),
                                            html.Hr(className="p-0 m-1"),
                                            html.Span("{}{} {:.2f} {:.2f}".format(latlong_to_utm[2], latlong_to_utm[3], latlong_to_utm[0], latlong_to_utm[1]), className="p-0 m-1")
                                        ],
                                        className="text-center p-0 m-1"
                                    ),
                                    direction="center"
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
                            latlong_to_utm = utm.from_latlon(search_lat_lng[0], search_lat_lng[1])
                            result = dl.Marker(
                                children=dl.Tooltip(
                                    html.Div(
                                        [
                                            html.Span("Lat: {:.2f}, Long: {:.2f}".format(search_lat_lng[0], search_lat_lng[1]), className="p-0 m-1"),
                                            html.Hr(className="p-0 m-1"),
                                            html.Span("{}{} {:.2f} {:.2f}".format(latlong_to_utm[2], latlong_to_utm[3], latlong_to_utm[0], latlong_to_utm[1]), className="p-0 m-1")
                                        ],
                                        className="text-center p-0 m-1"
                                    ),
                                    direction="center"
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
                        result = dl.Marker(
                            children=dl.Tooltip(
                                html.Div(
                                    [
                                        html.Span("Lat: {:.2f}, Long: {:.2f}".format(p[1], p[0]), className="p-0 m-1"),
                                        html.Hr(className="p-0 m-1"),
                                        html.Span("{} {} {}".format(search[0], search[1], search[2]), className="p-0 m-1")
                                    ],
                                    className="text-center p-0 m-1"
                                ),
                                direction="center",
                            ),
                            position=(p[1], p[0])
                        )
                        return [result], "", (p[1], p[0])
                    except:
                        raise PreventUpdate
                else:
                    raise PreventUpdate
            else:
                raise PreventUpdate




    @app.callback(
        Output("USER_SETTINGS_MODEL-TAB_HOME_BODY", "is_open"),
        Input("USER_SETTINGS-TAB_HOME_BODY", "n_clicks"),
        Input("CLOSE_USER_SETTINGS_MODEL-TAB_HOME_BODY", "n_clicks"),
        State("USER_SETTINGS_MODEL-TAB_HOME_BODY", "is_open"),
    )
    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open




    # -----------------------------------------------------------------------------
    # CONNECT TO IP SERVER DATABASE - TAB HOME BODY
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("SUBMIT_IP_SERVER_DATABASE-TAB_HOME_BODY", "n_clicks"),    
        Output("IP_SERVER_DATABASE-TAB_HOME_BODY", "value"),
        Output("POPUP_IP_SERVER_DATABASE-TAB_HOME_BODY", "is_open"),
        Output("POPUP_IP_SERVER_DATABASE-TAB_HOME_BODY", "icon"),
        Output("POPUP_IP_SERVER_DATABASE-TAB_HOME_BODY", "header"),    
        Output("POPUP_IP_SERVER_DATABASE-TAB_HOME_BODY", "children"),
        Output("POPUP_IP_SERVER_DATABASE-TAB_HOME_BODY", "headerClassName"),
        Input("SUBMIT_IP_SERVER_DATABASE-TAB_HOME_BODY", "n_clicks"),
        State("IP_SERVER_DATABASE-TAB_HOME_BODY", "value"),
    )
    def FUNCTION_CONNECT_TO_IP_SERVER_DATABASE_TAB_HOME_BODY(n, ip_address):
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
    # CONNECT TO SPREADSHEET FILE AND CREATE DATABASE - TAB HOME BODY
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("SUBMIT_SPREADSHEET_DATABASE-TAB_HOME_BODY", "n_clicks"),        
        Output("CHOOSEED_FILE_NAME-TAB_HOME_BODY", "children"),
        Output("CHOOSEED_FILE_NAME-TAB_HOME_BODY", "style"),                
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_HOME_BODY", "is_open"),
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_HOME_BODY", "icon"),
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_HOME_BODY", "header"),
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_HOME_BODY", "children"),
        Output("POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_HOME_BODY", "headerClassName"),        
        Output('CHOOSE_SPREADSHEET-TAB_HOME_BODY', 'contents'),
        Output('SELECT_GEOINFO_WORKSHEET_SPREADSHEET_DATABASE-TAB_HOME_BODY', 'options'),
        Output('SELECT_DATA_WORKSHEET_SPREADSHEET_DATABASE-TAB_HOME_BODY', 'options'),
        Output('RAW_DATA-TAB_HOME_BODY', 'data'),
        Output('INPUT_GEOINFO_TABLE_NAME-TAB_HOME_BODY', 'value'),
        Output('INPUT_DATA_TABLE_NAME-TAB_HOME_BODY', 'value'),       
        Output('INTERVAL_COMPONENT_SELECT_TABLE_DATA_CLEANSING-TAB_HOME_BODY', 'n_intervals'),       
                      
        Input("SUBMIT_SPREADSHEET_DATABASE-TAB_HOME_BODY", "n_clicks"),        
        Input('CHOOSE_SPREADSHEET-TAB_HOME_BODY', 'contents'),
        State('INPUT_GEOINFO_TABLE_NAME-TAB_HOME_BODY', 'value'),
        State('INPUT_DATA_TABLE_NAME-TAB_HOME_BODY', 'value'),
        State('CHOOSE_SPREADSHEET-TAB_HOME_BODY', 'contents'),
        State('CHOOSE_SPREADSHEET-TAB_HOME_BODY', 'filename'),
        State('SELECT_GEOINFO_WORKSHEET_SPREADSHEET_DATABASE-TAB_HOME_BODY', 'value'),
        State('SELECT_DATA_WORKSHEET_SPREADSHEET_DATABASE-TAB_HOME_BODY', 'value'),      
        State('SELECT_GEOINFO_WORKSHEET_SPREADSHEET_DATABASE-TAB_HOME_BODY', 'options'),
        State('SELECT_DATA_WORKSHEET_SPREADSHEET_DATABASE-TAB_HOME_BODY', 'options'),
        State('RAW_DATA-TAB_HOME_BODY', 'data'),      
    )
    def FUNCTION_CONNECT_TO_SPREADSHEET_DATABASE_TAB_HOME_BODY(
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
                f"{filename[0:14]}..." if len(filename) >= 18 else filename,
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
                    f"{filename[0:14]}..." if len(filename) >= 18 else filename,
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
                    f"{filename[0:14]}..." if len(filename) >= 18 else filename,
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
                    f"{filename[0:14]}..." if len(filename) >= 18 else filename,
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
                    f"{filename[0:14]}..." if len(filename) >= 18 else filename,
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
                    f"{filename[0:14]}..." if len(filename) >= 18 else filename,
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
                    f"{filename[0:14]}..." if len(filename) >= 18 else filename,
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
                    f"{filename[0:14]}..." if len(filename) >= 18 else filename,
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
    # DATA CLEANSING - TAB HOME BODY
    # -----------------------------------------------------------------------------
    
    # SECTION 1:
    # ----------
    
    @app.callback(
        Output('SELECT_GEOINFO_TABLE_DATA_CLEANSING-TAB_HOME_BODY', 'options'),
        Output('SELECT_DATA_TABLE_DATA_CLEANSING-TAB_HOME_BODY', 'options'),
        Input("INTERVAL_COMPONENT_SELECT_TABLE_DATA_CLEANSING-TAB_HOME_BODY", "n_intervals"),
    )
    def FUNCTION_SELECT_TABLE_NAME_DATA_CLEANSING_TAB_HOME_BODY(
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


    # SECTION 2:
    # ----------
    
    @app.callback(
        Output('SELECT_ORDER_INTERPOLATE_METHOD_DATA_CLEANSING-TAB_HOME_BODY', 'disabled'),
        Input('SELECT_INTERPOLATE_METHOD_DATA_CLEANSING-TAB_HOME_BODY', 'value'),
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

