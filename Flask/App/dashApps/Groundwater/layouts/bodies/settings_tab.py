import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.callbacks.config import *

# -----------------------------------------------------------------------------
# TAB SETTINGS - BODY
# -----------------------------------------------------------------------------

# DATABASE CARD
# .............................................................................

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
                            id='IP_SERVER_DATABASE-TAB_SETTING_BODY', 
                            className='form-group ip-box p-0 m-0 text-center w-100 h-100',
                            type='text',
                            placeholder='127.0.0.1:8080',
                        )
                    ],
                    className='col-xl-8 col-lg-12 col-12 p-0 m-0 py-1',
                ),
                html.Div(
                    children=[
                        html.Button(
                            id='SUBMIT_IP_SERVER_DATABASE-TAB_SETTING_BODY', 
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
                    className='col-xl-4 col-lg-4 col-12 p-0 m-0 py-1',
                ),
            ],
            className='row p-0 m-0 align-items-center justify-content-center',
        ),
        
        dbc.Toast(
            id="POPUP_IP_SERVER_DATABASE-TAB_SETTING_BODY",
            is_open=False,
            dismissable=True,
            duration=5000,
            className="popup-notification",
        )
        
    ],
    className="form-group p-0 py-3 m-0"
)


SPREADSHEET_DATABASE_MODEL = dbc.Modal(
    children=[
        
        dbc.ModalHeader(
            children=[
                "تنظیمات فایل صفحه گسترده ورودی"
            ],
            className="m-auto"            
        ),
        
        dbc.ModalBody(
            children=[
                
            ],    
        ),
        
        dbc.ModalFooter(
            children=[
                dbc.Button(
                    "بستن",
                    id="CLOSE_SPREADSHEET_DATABASE_MODEL-TAB_SETTING_BODY",
                    className="btn btn-danger btn-lg",
                    n_clicks=0,
                    style={
                        "width": "6rem"
                    }
                ),
            ],
            className="row m-auto"
        ),
        
    ],
    id="SPREADSHEET_DATABASE_MODEL-TAB_SETTING_BODY",
    is_open=False,
    size="lg",
    backdrop="static",
    keyboard=False,
    scrollable=False,
    centered=False,
    autoFocus=True,
    fade=True
)


SPREADSHEET_DATABASE = html.Div(
    children=[
        
        html.Div(
            children=[
                "ایجاد پایگاه داده از فایل صفحه گسترده"    
            ],
            className='row p-0 m-0 pb-3 text-center',
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Upload(
                            children=[
                                html.B(
                                    id="CHOOSEED_FILE_NAME-TAB_SETTING_BODY",
                                    children=[
                                        'انتخاب فایل',
                                        html.I(
                                            className="fas fa-cloud-upload-alt ml-2"
                                        ),
                                    ],
                                    className='font-weight-light',
                                ),
                            ],
                            className="upload-button m-auto",
                            id="CHOOSE_SPREADSHEET-TAB_SETTING_BODY",
                            accept=".xlsx, .xls",
                        ),
                    ],
                    className='col-xl-8 col-lg-12 col-12 p-0 m-0 py-1',
                    dir="ltr"
                ),
                html.Div(
                    children=[
                        html.Button(
                            id='SUBMIT_SPREADSHEET_DATABASE-TAB_SETTING_BODY', 
                            className='btn btn-primary rounded-0 p-0 m-0 w-100 h-100',
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
                    className='col-xl-4 col-lg-4 col-12 p-0 m-0 py-1',
                ), 
            ],
            className='row p-0 m-0 align-items-center justify-content-center',
        ),
        
        dbc.Toast(
            id="POPUP_CONNECT_TO_SPREADSHEET_DATABASE-TAB_SETTING_BODY",
            is_open=False,
            dismissable=True,
            duration=5000,
            className="popup-notification",
        ),
        
        SPREADSHEET_DATABASE_MODEL,
        
    ],
    className="form-group p-0 py-3 m-0"
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
                    className="list-group-item"
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
    className="card border-dark rounded p-0 m-0"
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
            className='col-3 p-1 m-0',
        ),
        html.Div(
            children=[
                ''
            ],
            className='col-9 p-1 m-0',
        )
    ],
    dir='rtl',
    className='row p-0 m-0',
    style={
        'height': '95vh',
        'width ': '100vw'
    }
)