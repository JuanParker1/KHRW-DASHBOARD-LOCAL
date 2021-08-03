import dash_leaflet as dl
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_leaflet.express as dlx
from dash_extensions.javascript import arrow_function
import geopandas as gpd

from App.dashApps.Groundwater.callbacks.config import *


# -----------------------------------------------------------------------------
# ELEMAN ON MAP
# -----------------------------------------------------------------------------

# SIDEBAR_BUTTON = html.Div(
#     children=[
#         html.I(
#             className="fas fa-outdent fa-2x BTN-SIDEBAR-CLOSE",
#             id="SIDEBAR_BUTTON-TAB_HOME_BODY"
#         )
#     ]
# )
SIDEBAR_BUTTON = html.Div(
    children=[
        html.I(
            html.Img(
                src='data:image/png;base64,{}'.format(KHRW_LOGO),
                height="42px",
                className="m-1"
            ),
            className="BTN-SIDEBAR-CLOSE",
            id="SIDEBAR_BUTTON-TAB_HOME_BODY"
        )
    ]
)


TITLE = html.Div(
    id="TITLE-TAB_HOME_BODY",
    children=[
        html.H5("گروه آب‌های زیرزمینی‏", className="p-0 m-0 mb-1 mr-1"),
        html.P("دفتر مطالعات پایه منابع آب شرکت سهامی آب منطقه‌ای خراسان رضوی", className="text-primary p-0 m-0"),
    ],
    className="TILTE-SHOW",
    dir="rtl"
)



MAP_INFO = html.Div(
    id="MAP_INFO-TAB_HOME_BODY",
    className="MAP-INFO",
    dir="rtl"
)


SHOW_COORDINATE = html.Div(
    id="SHOW_COORDINATE_INFO-TAB_HOME_BODY",
    className="info",
    style={
        "position": "absolute",
        "bottom": "10px",
        "left": "50%",
        "transform": "translateX(-50%)",
        "zIndex": "1000",
        "font-family": "Vazir",
        "font-size": "small",
        "line-height": "1.5"
    },
    dir="rtl"
)


SEARCH_BAR = html.Div(
    id="SEARCH_BAR-TAB_HOME_BODY",
    children=[
        dcc.Input(
            id="SEARCH-TAB_HOME_BODY",
            placeholder="جستجو",
            type="search",
            debounce=True,
            className="searchicon text-center"
        ),
        dbc.Tooltip(
            target="SEARCH-TAB_HOME_BODY",
            autohide=True,
            placement="right",
            hide_arrow=True,
            delay={ "show": 0, "hide": 10 },
            children=[
                html.Div(
                    children=[
                        html.P(
                            "- سرچ براساس درجه:",
                            className="text-right my-0 py-0"
                        ),
                        html.P(
                            "به ترتیب عرض و طول جغرافیایی وارد شود، مانند:",
                            className="text-nowrap text-right my-0 py-0 mr-4"
                        ),
                        html.P(
                            "> 36.3 59.0",
                            className="text-left my-0 py-0",
                            dir="ltr"
                        ),
                        html.Hr(className="my-1 py-1"),
                        html.P(
                            "- سرچ براساس درجه/دقیقه/ثانیه:",
                            className="text-right my-0 py-0"
                        ),
                        html.P(
                            "به ترتیب عرض و طول جغرافیایی وارد شود، مانند:",
                            className="text-nowrap text-right my-0 py-0 mr-4"
                        ),
                        html.P(
                            "> 36 17 48 59 36 0",
                            className="text-left my-0 py-0",
                            dir="ltr"
                        ),
                        html.Hr(className="my-1 py-1"),
                        html.P(
                            "- سرچ براساس UTM:",
                            className="text-right my-0 py-0"
                        ),
                        html.P(
                            "به ترتیب زون، مولفه شرقی و مولفه شمالی وارد شود، مانند:",
                            className="text-nowrap text-right my-0 py-0 mr-4"
                        ),
                        html.P(
                            "> 40S 733465 4020360",
                            className="text-left my-0 py-0",
                            dir="ltr"
                        )
                    ],
                    dir="rtl"
                )
            ],
            style = {
                "maxWidth": "50rem",
                "width": "30rem",
            },
        ),
    ],
    className="SEARCH-BAR",
    dir="ltr"
)


# -------------------------------------------------------------------------------------------------
# TAB HOME - BODY
# -------------------------------------------------------------------------------------------------

BODY_TAB_HOME = html.Div(
    children=[
        html.Div(
            children=[
                SIDEBAR_BUTTON,
                dl.Map(
                    id="MAP-TAB_HOME_BODY",
                    center=[36.30, 59.60],
                    zoom=6,
                    children=[
                        dl.TileLayer(
                            url=STREETS_URL,
                            opacity=1,
                            attribution=ATTRIBUTION,
                            id="BASE_MAP-TAB_HOME_BODY"
                        ),
                        dl.LayerGroup(
                            id="CLICK_LAYER-TAB_HOME_BODY"
                        ),
                        dl.LocateControl(
                            id="LOCATE_CONTROL-TAB_HOME_BODY",
                            options={
                                'locateOptions': {
                                    'enableHighAccuracy': True
                                }
                            }
                        ),
                        dl.MeasureControl(
                            id="MEASURE_CONTROL-TAB_HOME_BODY",
                            position="topleft",
                            primaryLengthUnit="kilometers",
                            primaryAreaUnit="hectares",
                            activeColor="#214097",
                            completedColor="#972158",
                        ),
                        dl.FeatureGroup([                            
                            dl.EditControl(id="edit_control"),
                        ],
                        id="FEATURE_GROUP-TAB_HOME_BODY",
                        ),
                        MAP_INFO,
                        SEARCH_BAR,
                        TITLE,
                        # SHOW_COORDINATE
                    ],
                    style={
                        'height': '93vh',
                        "font-family": "Tanha-FD",
                        "font-size": "medium"
                    },
                ),
            ],
            dir="rtl"
        ),
        html.Div(
            children=[
                html.Div(
                    id="out1",
                    className="col-6"
                ),
                html.Div(
                    id="out2",
                    className="col-6"
                )
            ],
            className="row"
        )
    ],
    id="BODY-TAB_HOME",
    className="CONTENT-WITHOUT-SIDEBAR"
)


