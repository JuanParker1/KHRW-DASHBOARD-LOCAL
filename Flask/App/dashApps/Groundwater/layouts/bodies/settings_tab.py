from sqlite3.dbapi2 import Row
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_html_components.B import B
from dash_html_components.Hr import Hr

from App.dashApps.Groundwater.callbacks.config import *

# -----------------------------------------------------------------------------
# TAB SETTINGS - BODY
# -----------------------------------------------------------------------------

# COLUMN 1: DATABASE
# -----------------------------------------------------------------------------

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
                            id='IP_SERVER_DATABASE-TAB_SETTINGS_BODY', 
                            className='form-group ip-box p-0 m-0 text-center w-100 h-100',
                            type='text',
                            placeholder='127.0.0.1:8080',
                        )
                    ],
                    className='col-xl-7 col-lg-7 col-7 p-0 m-0 py-1',
                ),
                html.Div(
                    children=[
                        html.Button(
                            id='SUBMIT_IP_SERVER_DATABASE-TAB_SETTINGS_BODY', 
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
                    className='col-xl-3 col-lg-3 col-3 p-0 m-0 py-1',
                ),
            ],
            className='row p-0 m-0 align-items-center justify-content-center',
        ),
        
        dbc.Toast(
            id="POPUP_IP_SERVER_DATABASE-TAB_SETTINGS_BODY",
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
        html.Label(
            children=[
                "1- انتخاب فایل صفحه گسترده:"
            ],
            className='row pb-2 m-0 text-center',
            dir="rtl",
        ),
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
                            id="CHOOSE_SPREADSHEET-TAB_SETTINGS_BODY",
                            accept=".xlsx, .xls",
                        ),
                    ],
                    className='col-xl-5 col-lg-5 col-5 p-0 m-0',
                    dir="ltr"
                ),
                html.Div(
                    id='CHOOSEED_FILE_NAME-TAB_SETTINGS_BODY',
                    children=[
                        "فایلی انتخاب نشده است!"
                    ],
                    className='col-xl-7 col-lg-7 col-7 p-0 m-0 pr-2 text-right',
                ),
            ],
            className='row p-0 m-0 align-items-center justify-content-center text-center',
        ),
        
        html.Br(),
        
        html.Label(
            children=[
                "2- انتخاب کاربرگ:"
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
                                "کاربرگ مشخصات"
                            ]
                        ),
                        dcc.Dropdown(
                            id="SELECT_GEOINFO_WORKSHEET_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY",
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
                                "کاربرگ داده‏‌ها"
                            ]
                        ),
                        dcc.Dropdown(
                            id="SELECT_DATA_WORKSHEET_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY",
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
        
        html.Br(),
        
        html.Label(
            children=[
                "3- انتخاب نام جدول:"
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
                            ]
                        ),
                        dcc.Input(
                            id="INPUT_GEOINFO_TABLE_NAME-TAB_SETTINGS_BODY",
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
                    className='col-5 p-0 m-0 text-center',
                ),
                html.Div(
                    children=[
                        html.Span(
                            children=[
                                "جدول داده‌ها"
                            ]
                        ),
                        dcc.Input(
                            id="INPUT_DATA_TABLE_NAME-TAB_SETTINGS_BODY",
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
                    className='col-5 p-0 m-0 text-center ',
                ),
            ],
            className='row p-0 m-0 pb-3 align-items-center justify-content-center',
        ),     
        
        dbc.Toast(
            id="POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY",
            is_open=False,
            dismissable=True,
            duration=5000,
            className="popup-notification",
        ),
        
    ],
    className="form-group p-0 m-0"
)


DATABASE_CARD_BUTTON = html.Div(
    children=[
        html.Div(
            children=[
                html.Button(
                    id='SUBMIT_SPREADSHEET_DATABASE-TAB_SETTINGS_BODY', 
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
            className='col-12 p-0 m-0 ',
        ),
    ],
    className='col-4 p-1 m-0 text-left',
)


DATABASE_CARD = html.Div(
    children=[
        # CARD HEADER +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[                       
                                html.H5(
                                    children=[
                                        html.Img(
                                            src='data:image/png;base64,{}'.format(DATABASE_LOGO),
                                            height=30,
                                            className="ml-2"
                                        ),
                                        "پایگاه داده",
                                    ],
                                    className='text-right p-0 m-0'
                                ),
                            ],
                            className='col-8 p-0 m-0',
                        ),
                        DATABASE_CARD_BUTTON 
                    ],
                    className="row m-2 d-flex align-items-center" 
                ),
            ],
            className="card-header justify-content-between p-0"
        ),
        
        
        
        
        
        
        # CARD BODY +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        html.Ul(
            children=[
                html.Li(
                    children=[
                        SPREADSHEET_DATABASE
                        
                    ],
                    className="list-group-item border-bottom border-top border-dark"
                ),
                html.Li(
                    children=[
                        IP_SERVER_DATABASE
                    ],
                    className="list-group-item"
                )
            ],
            className="list-group list-group-flush"
        )
    ],
    className="card border-dark rounded p-0 m-0 h-100 align-self-center"
)


# COLUMN 2: DATA CLEANSING
# -----------------------------------------------------------------------------

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
                            id="SELECT_GEOINFO_TABLE_DATA_CLEANSING-TAB_SETTINGS_BODY",
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
                            id="SELECT_DATA_TABLE_DATA_CLEANSING-TAB_SETTINGS_BODY",
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
                            id="SELECT_DATE_TYPE_DATA_CLEANSING-TAB_SETTINGS_BODY",
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
                "3- درون‌یابی مقادیر گمشده:"
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
                                "انتخاب روش"
                            ]
                        ),
                        dcc.Dropdown(
                            id="SELECT_INTERPOLATE_METHOD_DATA_CLEANSING-TAB_SETTINGS_BODY",
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
                            id="SELECT_ORDER_INTERPOLATE_METHOD_DATA_CLEANSING-TAB_SETTINGS_BODY",
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
        html.Br(),
        html.Div(
            children=[
                "بیشترین تعداد مقادیر گمشده پی در پی"
            ],
            className='p-0 m-0 text-center',
            dir="rtl",
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Dropdown(
                            id="SELECT_LIMIT_DATA_CLEANSING-TAB_SETTINGS_BODY",
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
        )
        
    ],
    className="p-1 m-0"
)

DATA_CLEANSING_CARD_PART_4 = html.Div(
    children=[
        
        html.Label(
            children=[
                "4- پلیگون‌های تیسن:"
            ],
            className='row pb-2 m-0 text-center',
            dir="rtl",
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Checklist(
                            id="THIESSEN_CALCULATION_DATA_CLEANSING-TAB_SETTINGS_BODY",
                            options=[
                                {'label': 'محاسبه پلیگون‌های تیسن', 'value': 'CALCULATE'},
                            ],
                            value='CALCULATE',
                            inputClassName="ml-1",
                        )
                    ],
                    className='p-0 m-0',
                ),
            ],
            className='row p-0 m-0 mr-4 align-items-center justify-content-start',
            dir="rtl",
        ),
        
    ],
    className="p-1 pb-3 m-0"
)


DATA_CLEANSING_CARD_BUTTON = html.Div(
    children=[
        html.Div(
            children=[
                html.Button(
                    id='SUBMIT_DATACLEANSING-TAB_SETTINGS_BODY', 
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
            className='col-12 p-0 m-0 ',
        ),
    ],
    className='col-4 p-1 m-0 text-left',
)



DATA_CLEANSING_CARD_BODY = html.Div(
    children=[
        DATA_CLEANSING_CARD_PART_1,
        html.Br(),
        DATA_CLEANSING_CARD_PART_2,
        html.Br(),
        DATA_CLEANSING_CARD_PART_3,
        html.Br(),
        DATA_CLEANSING_CARD_PART_4,   
    ],
    className="form-group p-0 m-0"
)



DATA_CLEANSING_CARD = html.Div(
    children=[
        # CARD HEADER +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[                       
                                html.H5(
                                    children=[
                                        html.Img(
                                            src='data:image/png;base64,{}'.format(DATACLEANSING_LOGO),
                                            height=30,
                                            className="ml-2"
                                        ),
                                        "پاکسازی داده‌ها",
                                    ],
                                    className='text-right p-0 m-0'
                                ),
                            ],
                            className='col-8 p-0 m-0',
                        ),
                        DATA_CLEANSING_CARD_BUTTON,
                        dbc.Toast(
                            id="POPUP_DATA_CLEANSING_DATABASE-TAB_SETTINGS_BODY",
                            is_open=False,
                            dismissable=True,
                            duration=5000,
                            className="popup-notification",
                        ),
                    ],
                    className="row m-2 d-flex align-items-center" 
                ),
               
            ],
            className="card-header justify-content-between p-0"
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


# COLUMN 3: AQUIFER HYDROGRAPH
# -----------------------------------------------------------------------------

AQUIFER_HYDROGRAPH_CARD = html.Div(
    children=[
        # CARD HEADER +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        html.H5(
            children=[
                html.Img(
                    src='data:image/png;base64,{}'.format(CALCULATE_LOGO),
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



# -------------------------------------------------------------------------------------------------
# TAB SETTINGS - BODY
# -------------------------------------------------------------------------------------------------

BODY_TAB_SETTINGS = html.Div(
    children=[
        html.Div(
            children=[
                DATABASE_CARD,
            ],
            className='col-xl-4 col-lg-6 col-md-6 p-1 m-0',
        ),
        html.Div(
            children=[
                DATA_CLEANSING_CARD
            ],
            className='col-xl-4 col-lg-6 col-md-6 p-1 m-0',
        ),
        html.Div(
            children=[
                AQUIFER_HYDROGRAPH_CARD
            ],
            className='col-xl-4 col-lg-6 col-md-6 p-1 m-0',
        ),
    ],
    dir='rtl',
    className='row p-3 m-0 align-self-center justify-content-center h-100',
)