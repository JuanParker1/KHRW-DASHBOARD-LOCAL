from dash_html_components.Hr import Hr
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



# USER SETTINGS
# -----------------------------------------------------------------------------

USER_SETTINGS = html.Span(
    id="USER_SETTINGS-TAB_HOME_BODY",
    children=[
        html.I(
            className="fas fa-user-cog fa-2x text-dark",
        ),
        dbc.Tooltip(
            "تنظیمات داشبورد مدیریتی",
            target="USER_SETTINGS-TAB_HOME_BODY",
        ),
    ],
    n_clicks=0,
    className="USER-SETTINGS",
    dir="rtl"
)


IP_SERVER_DATABASE = html.Div(
    children=[
        
        html.Div(
            children=[
                "اتصال به پایگاه داده از طریق نشانی آی‌پی"
            ],
            className='row p-0 m-0 pb-3 text-center',
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Input(
                            id='IP_SERVER_DATABASE-TAB_HOME_BODY', 
                            className='form-group ip-box p-0 m-0 text-center w-100 h-100',
                            type='text',
                            placeholder='127.0.0.1:8080',
                        )
                    ],
                    className='col-xl-8 col-lg-8 col-8 p-0 m-0 py-1',
                ),
                html.Div(
                    children=[
                        html.Button(
                            id='SUBMIT_IP_SERVER_DATABASE-TAB_HOME_BODY', 
                            className='btn btn-primary rounded-0 p-0 m-0 w-100 h-100',
                            n_clicks=0,
                            children=[
                                html.I(
                                    className="fa fa-plug ml-2"
                                ),
                                "اتصال",                                
                            ],
                            style={
                                "height": "40px",
                                "line-height": "40px"
                            }
                        )
                    ],
                    className='col-xl-4 col-lg-4 col-4 p-0 m-0 py-1',
                ),
            ],
            className='row p-0 m-0 align-items-center justify-content-center',
        ),
        
        dbc.Toast(
            id="POPUP_IP_SERVER_DATABASE-TAB_HOME_BODY",
            is_open=False,
            dismissable=True,
            duration=5000,
            className="popup-notification",
        )
        
    ],
    className="form-group p-0 m-0"
)


SPREADSHEET_DATABASE = html.Div(
    children=[
        
        html.Div(
            children=[
                "ایجاد پایگاه داده از فایل صفحه گسترده"
            ],
            className='row p-0 m-0 pb-3 text-center',
        ),
        # TODO: Use "dash-uploader" Instead "dcc.Upload"
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Upload(
                            children=[
                                html.B(
                                    children=[
                                        'انتخاب فایل',
                                        html.I(
                                            className="fas fa-cloud-upload-alt ml-2"
                                        ),
                                    ],
                                    className='font-weight-light',
                                ),
                            ],
                            className="upload-button m-auto rounded",
                            id="CHOOSE_SPREADSHEET-TAB_HOME_BODY",
                            accept=".xlsx, .xls",
                        ),
                    ],
                    className='col-xl-5 col-lg-5 col-5 p-0 m-0',
                    dir="ltr"
                ),
                html.Div(
                    id='CHOOSEED_FILE_NAME-TAB_HOME_BODY',
                    children=[
                        "فایلی انتخاب نشده است!"
                    ],
                    className='col-xl-7 col-lg-7 col-7 p-0 m-0 pr-2',
                ),

            ],
            className='row p-0 m-0 align-items-center justify-content-center',
        ),
        
        html.P("", className="breakLine p-0 my-2 mx-auto w-75 text-info"),
        
        html.Div(
            children=[
                "انتخاب کاربرگ"
            ],
            className='row p-0 m-0 align-items-center justify-content-center text-center',
            dir="rtl"
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Span(
                            children=[
                                "کاربرگ مشخصات"
                            ]
                        ),
                        dcc.Dropdown(
                            id="SELECT_GEOINFO_WORKSHEET_SPREADSHEET_DATABASE-TAB_HOME_BODY",
                            placeholder="انتخاب...",
                            clearable=False,
                            style={
                                "line-height": "40px",
                            }
                        )
                    ],
                    className='col-6 p-0 m-0 text-center',
                ),
                html.Div(
                    children=[
                        html.Span(
                            children=[
                                "کاربرگ داده‏‌ها"
                            ]
                        ),
                        dcc.Dropdown(
                            id="SELECT_DATA_WORKSHEET_SPREADSHEET_DATABASE-TAB_HOME_BODY",
                            placeholder="انتخاب...",
                            clearable=False,
                            style={
                                "line-height": "40px",
                            }
                        )
                    ],
                    className='col-6 p-0 m-0 text-center ',
                ),
            ],
            className='row p-0 m-0 align-items-center justify-content-center',
        ),
        
        html.P("", className="breakLine p-0 my-2 mx-auto w-75 text-info"),
        
        html.Div(
            children=[
                "انتخاب نام جدول"
            ],
            className='row p-0 m-0 align-items-center justify-content-center text-center',
            dir="rtl"
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Span(
                            children=[
                                "جدول مشخصات"
                            ]
                        ),
                        dcc.Input(
                            id="INPUT_GEOINFO_TABLE_NAME-TAB_HOME_BODY",
                            className="text-center w-100",
                            value='',
                            style={
                                "line-height": "40px",
                                "border": "solid 1px #ccc",
                                "border-radius": "4px",
                                "direction": "ltr"
                            }
                        )
                    ],
                    className='col-6 p-0 m-0 text-center',
                ),
                html.Div(
                    children=[
                        html.Span(
                            children=[
                                "جدول داده‌ها"
                            ]
                        ),
                        dcc.Input(
                            id="INPUT_DATA_TABLE_NAME-TAB_HOME_BODY",
                            className="text-center w-100",
                            value='',
                            style={
                                "line-height": "40px",
                                "border": "solid 1px #ccc",
                                "border-radius": "4px",
                                "direction": "ltr"
                            }
                        )
                    ],
                    className='col-6 p-0 m-0 text-center ',
                ),
            ],
            className='row p-0 m-0 pb-3 align-items-center justify-content-center',
        ),       
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Button(
                            id='SUBMIT_SPREADSHEET_DATABASE-TAB_HOME_BODY', 
                            className='btn btn-primary rounded p-0 m-0 w-100 h-100',
                            n_clicks=0,
                            children=[
                                html.I(
                                    className="fa fa-database ml-2"
                                ),
                                "ایجاد",                                
                            ],
                            style={
                                "height": "40px",
                                "line-height": "40px"
                            }
                        )
                    ],
                    className='col-4 p-0 m-0 ',
                ),
            ],
            className='row p-0 m-0 align-items-end justify-content-center',
        ), 
        
        dbc.Toast(
            id="POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_HOME_BODY",
            is_open=False,
            dismissable=True,
            duration=5000,
            className="popup-notification",
        ),
        
    ],
    className="form-group p-0 m-0"
)


DATABASE_CARD = html.Div(
    children=[
        # CARD HEADER +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        html.H5(
            children=[
                html.Img(
                    src='data:image/png;base64,{}'.format(DATABASE_LOGO),
                    height=30,
                    className="ml-2"
                ),
                "پایگاه داده",
            ],
            className='card-header text-right'
        ),
        # CARD BODY +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        html.Ul(
            children=[
                html.Li(
                    children=[
                        IP_SERVER_DATABASE
                    ],
                    className="list-group-item border-bottom border-top border-dark"
                ),
                html.Li(
                    children=[
                        SPREADSHEET_DATABASE
                    ],
                    className="list-group-item"
                )
            ],
            className="list-group list-group-flush"
        )
    ],
    className="card border-dark rounded p-0 m-0 h-100 align-self-center"
)


DATA_CLEANSING_CARD_PART_1 = html.Div(
    children=[
        
        html.Label(
            children=[
                "1- انتخاب جدول از پایگاه داده:"
            ],
            className='row pb-2 m-0 text-center',
            dir="rtl",
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Span(
                            children=[
                                "جدول مشخصات"
                            ],
                        ),
                        dcc.Dropdown(
                            id="SELECT_GEOINFO_TABLE_DATA_CLEANSING-TAB_HOME_BODY",
                            placeholder="انتخاب...",
                            clearable=False,
                            style={
                                "line-height": "40px",
                            }
                        )
                    ],
                    className='col-5 p-0 m-0 text-center',
                ),
                html.Div(
                    children=[
                        html.Span(
                            children=[
                                "جدول داده‏‌ها"
                            ]
                        ),
                        dcc.Dropdown(
                            id="SELECT_DATA_TABLE_DATA_CLEANSING-TAB_HOME_BODY",
                            placeholder="انتخاب...",
                            clearable=False,
                            style={
                                "line-height": "40px",
                            }
                        )
                    ],
                    className='col-5 p-0 m-0 text-center ',
                ),
            ],
            className='row p-0 m-0 align-items-center justify-content-center',
        ),
        
    ],
    className="p-1 m-0"
)


DATA_CLEANSING_CARD_PART_2 = html.Div(
    children=[
        
        html.Label(
            children=[
                "2- انتخاب نوع تاریخ ورودی:"
            ],
            className='row pb-2 m-0 text-center',
            dir="rtl",
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Dropdown(
                            id="SELECT_DATE_TYPE_DATA_CLEANSING-TAB_HOME_BODY",
                            clearable=False,
                            options=[
                                {'label': 'تاریخ شمسی', 'value': 'persian'},
                                {'label': 'تاریخ میلادی', 'value': 'gregorian'},
                            ],
                            value='persian',
                            style={
                                "line-height": "40px",
                            }
                        )
                    ],
                    className='col-5 p-0 m-0 text-center',
                ),
            ],
            className='row p-0 m-0 align-items-center justify-content-center',
        ),
        
    ],
    className="p-1 m-0"
)


DATA_CLEANSING_CARD_PART_3 = html.Div(
    children=[
        
        html.Label(
            children=[
                "3- انتخاب روش درون‌یابی مقادیر گمشده:"
            ],
            className='row pb-2 m-0 text-center',
            dir="rtl",
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Span(
                            children=[
                                "روش"
                            ]
                        ),
                        dcc.Dropdown(
                            id="SELECT_INTERPOLATE_METHOD_DATA_CLEANSING-TAB_HOME_BODY",
                            clearable=False,
                            options=[
                                {'label': 'Back Fill', 'value': 'bfill'},
                                {'label': 'Forward Fill', 'value': 'ffill'},
                                {'label': 'Pad', 'value': 'pad'},
                                {'label': 'Zero', 'value': 'zero'},
                                {'label': 'Linear', 'value': 'linear'},
                                {'label': 'Slinear', 'value': 'slinear'},
                                {'label': 'Akima', 'value': 'akima'},
                                {'label': 'Nearest', 'value': 'nearest'},
                                {'label': 'Spline', 'value': 'spline'},
                                {'label': 'Polynomial', 'value': 'polynomial'},
                                {'label': 'Cubic', 'value': 'cubic'},
                                {'label': 'Quadratic', 'value': 'quadratic'},
                                {'label': 'Barycentric', 'value': 'barycentric'},
                                {'label': 'Krogh', 'value': 'krogh'},
                                {'label': 'Piecewise Polynomial', 'value': 'piecewise_polynomial'},
                                {'label': 'Pchip', 'value': 'pchip'},
                                {'label': 'Cubicspline', 'value': 'cubicspline'},
                            ],
                            value='akima',
                            style={
                                "line-height": "40px",
                            }
                        )
                    ],
                    className='col-8 p-0 m-0 text-center',
                ),
                html.Div(
                    children=[
                        html.Span(
                            children=[
                                "مرتبه"
                            ]
                        ),
                        dcc.Dropdown(
                            id="SELECT_ORDER_INTERPOLATE_METHOD_DATA_CLEANSING-TAB_HOME_BODY",
                            clearable=False,
                            options=[
                                {'label': '0', 'value': 0},
                                {'label': '1', 'value': 1},
                                {'label': '2', 'value': 2},
                                {'label': '3', 'value': 3},
                                {'label': '4', 'value': 4},
                                {'label': '5', 'value': 5},
                            ],
                            value=1,
                            disabled=True,
                            style={
                                "line-height": "40px",
                            },
                        )
                    ],
                    dir="rtl",
                    className='col-2 p-0 m-0 text-center',
                ),
            ],
            className='row p-0 m-0 align-items-center justify-content-center',
        ),
        
    ],
    className="p-1 m-0"
)

DATA_CLEANSING_CARD_PART_4 = html.Div(
    children=[
        
        html.Label(
            children=[
                "4- بیشترین تعداد مقادیر گمشده پی در پی:"
            ],
            className='row pb-2 m-0 text-center',
            dir="rtl",
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Dropdown(
                            id="SELECT_LIMIT_DATA_CLEANSING-TAB_HOME_BODY",
                            clearable=False,
                            options=[
                                {'label': 'بدون محدودیت', 'value': 0},
                                {'label': '1', 'value': 1},
                                {'label': '2', 'value': 2},
                                {'label': '3', 'value': 3},
                                {'label': '4', 'value': 4},
                                {'label': '6', 'value': 6},
                                {'label': '9', 'value': 9},
                                {'label': '12', 'value': 12},
                                {'label': '15', 'value': 15},
                                {'label': '18', 'value': 18},
                                {'label': '21', 'value': 21},
                                {'label': '24', 'value': 24},
                            ],
                            value=0,
                            style={
                                "line-height": "40px",
                            }
                        )
                    ],
                    className='col-5 p-0 m-0 text-center',
                ),
            ],
            className='row p-0 m-0 align-items-center justify-content-center',
        ),
        
    ],
    className="p-1 pb-3 m-0"
)


DATA_CLEANSING_CARD_BUTTON = html.Div(
    children=[
        html.Div(
            children=[
                html.Button(
                    # id='SUBMIT_SPREADSHEET_DATABASE-TAB_HOME_BODY', 
                    className='btn btn-primary rounded p-0 m-0 w-100 h-100',
                    n_clicks=0,
                    children=[
                        html.I(
                            className="fa fa-database ml-2"
                        ),
                        "ایجاد",                                
                    ],
                    style={
                        "height": "40px",
                        "line-height": "40px"
                    }
                )
            ],
            className='col-4 p-0 m-0 ',
        ),
    ],
    className='row p-0 m-0 align-items-center justify-content-center',
)



DATA_CLEANSING_CARD_BODY = html.Div(
    children=[
        DATA_CLEANSING_CARD_PART_1,
        html.P("", className="breakLine p-0 my-2 mx-auto w-75 text-info"),
        DATA_CLEANSING_CARD_PART_2,
        html.P("", className="breakLine p-0 my-2 mx-auto w-75 text-info"),
        DATA_CLEANSING_CARD_PART_3,
        html.P("", className="breakLine p-0 my-2 mx-auto w-75 text-info"),
        DATA_CLEANSING_CARD_PART_4,
        DATA_CLEANSING_CARD_BUTTON,     
    ],
    className="form-group p-0 m-0"
)



DATA_CLEANSING_CARD = html.Div(
    children=[
        # CARD HEADER +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        html.H5(
            children=[
                html.Img(
                    src='data:image/png;base64,{}'.format(DATABASE_LOGO),
                    height=30,
                    className="ml-2"
                ),
                "پاکسازی داده‌ها",
            ],
            className='card-header text-right'
        ),
        # CARD BODY +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        html.Ul(
            children=[
                html.Li(
                    children=[
                        DATA_CLEANSING_CARD_BODY
                    ],
                    className="list-group-item border-top border-dark"
                ),
            ],
            className="list-group list-group-flush"
        )
    ],
    className="card border-dark rounded p-0 m-0 h-100"
)


AQUIFER_HYDROGRAPH_CARD = html.Div(
    children=[
        # CARD HEADER +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        html.H5(
            children=[
                html.Img(
                    src='data:image/png;base64,{}'.format(DATABASE_LOGO),
                    height=30,
                    className="ml-2"
                ),
                "محاسبه هیدروگراف آبخوان",
            ],
            className='card-header text-right'
        ),
        # CARD BODY +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        html.Ul(
            children=[
                html.Li(
                    children=[
                        "222"
                    ],
                    className="list-group-item border-top border-dark h-100"
                ),
            ],
            className="list-group list-group-flush"
        )
    ],
    className="card border-dark rounded p-0 m-0 h-100"
)


USER_SETTINGS_MODEL_BODY_TAB_HOME = html.Div(
    children=[
        html.Div(
            children=[
                DATABASE_CARD,
            ],
            className='col-xl-4 col-lg-6 col-md-12 p-1 m-0',
        ),
        html.Div(
            children=[
                DATA_CLEANSING_CARD
            ],
            className='col-xl-4 col-lg-6 col-md-12 p-1 m-0',
        ),
        html.Div(
            children=[
                AQUIFER_HYDROGRAPH_CARD
            ],
            className='col-xl-4 col-lg-6 col-md-12 p-1 m-0',
        )
    ],
    dir='rtl',
    className='row p-0 m-0 align-self-center justify-content-center h-100',
)


USER_SETTINGS_MODEL = dbc.Modal(
    children=[
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H4("تنظیمات داشبورد مدیریتی"),
                    ],
                    className='col-11 p-0 m-0 text-center',
                ),
                html.Div(
                    children=[
                        dbc.Button(
                            "بستن",
                            id="CLOSE_USER_SETTINGS_MODEL-TAB_HOME_BODY",
                            className="btn btn-danger btn-sm",
                            n_clicks=0,
                        ),
                    ],
                    className='col-1 p-0 m-0 text-left',
                ),                
            ],
            className="row p-0 pt-3 pb-1 mx-3 justify-content-between"
        ),
        
        html.Hr(
            className="p-0 m-0"    
        ),
        
        dbc.ModalBody(
            children=[
                USER_SETTINGS_MODEL_BODY_TAB_HOME,
            ],
            className="p-1 py-2 m-0"   
        ),
        
    ],
    id="USER_SETTINGS_MODEL-TAB_HOME_BODY",
    is_open=True,
    size="xl",
    backdrop="static",
    keyboard=False,
    scrollable=True,
    centered=False,
    autoFocus=True,
    fade=True,
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
                        USER_SETTINGS,
                        USER_SETTINGS_MODEL,
                        # SHOW_COORDINATE
                    ],
                    style={
                        'height': '95vh',
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


