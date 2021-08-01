import base64
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_html_components.Button import Button

from App.dashApps.Groundwater.layouts.visualizations.visualization import *
from App.dashApps.Groundwater.callbacks.data_analysis import *

# -------------------------------------------------------------------------------------------------
# SIDEBAR - TAB HOME
# -------------------------------------------------------------------------------------------------

COLLAPSE_BASE_MAP = html.Div(
    children=[
        html.H6(
            children=[
                html.I(
                    className="fas fa-caret-left ml-2",
                    id="ARROW-TAB_HOME_SIDEBAR_COLLAPSE_BASE_MAP"
                ),
                "نقشه‌های اصلی",
          
            ],
            id="OPEN_CLOSE-TAB_HOME_SIDEBAR_COLLAPSE_BASE_MAP",
            n_clicks=0,
            className="inline COLLAPSE-CARD-HEADER"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(STREETS),
                                    className="m-1"
                                ),
                                html.P(
                                    "Streets",
                                    className="card-title text-center m-0 fs-small"
                                )
                            ],
                            id="STREETS_BASE_MAP-TAB_HOME_BODY",
                            className="THUMBNAIL card", 
                            style=BASE_MAP_SELECTED_STYLE
                        ),
                        html.Div(
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(IMAGERY),
                                    className="m-1"
                                ),
                                html.P(
                                    "Imagery",
                                    className="card-title text-center m-0 fs-small"
                                )
                            ],
                            id="IMAGERY_BASE_MAP-TAB_HOME_BODY",
                            className="THUMBNAIL card "
                        ),
                        html.Div(
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(TOPOGRAPHIC),
                                    className="m-1"
                                ),
                                html.P(
                                    "Topographic",
                                    className="card-title text-center m-0 fs-small"
                                )
                            ],
                            id="TOPOGRAPHIC_BASE_MAP-TAB_HOME_BODY",
                            className="THUMBNAIL card"
                        )
                    ],
                    className="card-group mx-1 pt-1"
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(NONEBASEMAP),
                                    className="m-1"
                                ),
                                html.P(
                                    "None",
                                    className="card-title text-center m-0 fs-small"
                                )
                            ],
                            id="NONEBASEMAP_BASE_MAP-TAB_HOME_BODY",
                            className="THUMBNAIL card",
                        ),
                        html.Div(
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(DARK),
                                    className="m-1"
                                ),
                                html.P(
                                    "Dark",
                                    className="card-title text-center m-0 fs-small"
                                )
                            ],
                            id="DARK_BASE_MAP-TAB_HOME_BODY",
                            className="THUMBNAIL card",
                        ),
                        html.Div(
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(TERRAIN),
                                    className="m-1"
                                ),
                                html.P(
                                    "Terrain",
                                    className="card-title text-center m-0 fs-small"
                                )
                            ],
                            id="TERRAIN_BASE_MAP-TAB_HOME_BODY",
                            className="THUMBNAIL card"
                        )
                    ],
                    className="card-group mx-1 pb-1"
                ),
                html.Div(
                    children=[
                        html.Div(
                            "شفافیت:",
                            className="fs-small col-2 m-0 p-0"
                        ),
                        html.Div(
                            dcc.Slider(
                                id='OPACITY_BASE_MAP-TAB_HOME_SIDEBAR',
                                updatemode='drag',
                                min=0,
                                max=100,
                                step=5,
                                value=100,
                                marks={
                                    0: {'label': '0%', 'style': {'font-size': 'small'}},
                                    100: {'label': '100%', 'style': {'font-size': 'small'}}
                                },
                                className="p-0 m-0 mx-3"
                            ),
                            className="col-8 m-0 p-0"
                        ),
                        html.Div(
                            dbc.Badge(
                                id="BADGE_OPACITY_BASE_MAP-TAB_HOME_SIDEBAR",
                                children="100%",
                                color="primary",
                                className="w-100"
                            ),
                            className="col-2 m-0 p-0"
                        ),                        
                    ],
                    className="row my-0 mx-1 d-flex justify-content-around px-4 pb-4 pt-3"
                )
            ],
            id="COLLAPSE_BODY-TAB_HOME_SIDEBAR_COLLAPSE_BASE_MAP",
            is_open=False,
            style={"background-color": "#e9e9e9"}
        )
    ],
    className="COLLAPSE-CARD"
)


COLLAPSE_POLITICAL_MAP = html.Div(
    children=[
        html.H6(
            children=[
                html.I(
                    className="fas fa-caret-left ml-2",
                    id="ARROW-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP"
                ),
                "مرزهای سیاسی",        
            ],
            id="OPEN_CLOSE-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP",
            n_clicks=0,
            className="inline COLLAPSE-CARD-HEADER"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                dcc.Checklist(
                                    options=[
                                        {'label': 'کشور', 'value': 'COUNTRY'},
                                        {'label': 'استان', 'value': 'PROVINCE'},
                                        {'label': 'شهرستان', 'value': 'COUNTY'},
                                        {'label': 'بخش', 'value': 'DISTRICT'}
                                    ],
                                    id="ADD_POLITICAL_MAP-TAB_HOME_SIDEBAR",
                                    labelClassName  ="list-group-item p-0 m-0 py-2",
                                    inputClassName="mx-2"
                                )
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card"
                )
            ],
            id="COLLAPSE_BODY-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP",
            is_open=False,
        )
    ],
    className="COLLAPSE-CARD"
)


COLLAPSE_WATER_MAP = html.Div(
    children=[
        html.H6(
            children=[
                html.I(
                    className="fas fa-caret-left ml-2",
                    id="ARROW-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP"
                ),
                "مرزهای آبی",
          
            ],
            id="OPEN_CLOSE-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP",
            n_clicks=0,
            className="inline COLLAPSE-CARD-HEADER"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                dcc.Checklist(
                                    options=[
                                        {'label': 'حوضه‌های درجه یک', 'value': 'BASIN1'},
                                        {'label': 'حوضه‌های درجه دو', 'value': 'BASIN2'},
                                        {'label': 'محدوده‌های مطالعاتی', 'value': 'MAHDOUDE'},
                                        {'label': 'آبخوان‌ها', 'value': 'AQUIFER'},
                                    ],
                                    value=["MAHDOUDE"],
                                    id="ADD_WATER_MAP-TAB_HOME_SIDEBAR",
                                    labelClassName  ="list-group-item p-0 m-0 py-2",
                                    inputClassName="mx-2"
                                )
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card"
                )
            ],
            id="COLLAPSE_BODY-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP",
            is_open=False,
        )
    ],
    className="COLLAPSE-CARD"
)





# SIDEBAR - TAB HOME
# ------------------------------------------------------------------------

SIDEBAR_TAB_HOME = html.Div(

    children=[
        COLLAPSE_BASE_MAP,
        COLLAPSE_POLITICAL_MAP,
        COLLAPSE_WATER_MAP
    ],
    id="SIDEBAR-TAB_HOME",
    className="SIDEBAR-HIDEN"
)










# COLLAPSE 1
# -----------------------------------------------


DATABASE_CONNECT_METHOD_1 = html.Div(
    children=[
        html.Div(
            children=[
                html.H6(
                    children=[
                        "ایجاد پایگاه داده از فایل صفحه گسترده"
                    ],
                    className="text-center fs-medium"
                ),
            ],
            className="mb-4"
        ),
        html.Div(
            children=[

                dcc.Upload([
                    html.B(
                        children=[
                            html.I(className="fa fa-cloud-upload ml-2"),
                            'انتخاب فایل',
                        ],
                        className='font-weight-light'
                    ),
                ],
                    className="upload-button col-12 fs-medium",
                    id="CHOOSE_SPREADSHEET-TAB_HOME_COLLAPSE1",
                    accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                ),

                html.Div(
                    children=[
                        html.Button(
                            children=[
                                html.I(className="fa fa-database ml-2"),
                                "ایجاد",
                            ],
                            n_clicks=0,
                            className="btn btn-success fs-medium",
                            id="CONNECT_TO_SPREADSHEET-TAB_HOME_COLLAPSE1"
                        )
                    ],
                ),
            ],
            className="d-flex justify-content-between align-items-center m-0"
        ),
        html.Div(
            children=[
                html.Small(
                    dir="rtl",
                    id="FILENAME_SPREADSHEET-TAB_HOME_COLLAPSE1",
                ),
            ],
            className="text-center fs-medium mt-3"
        ),
        dbc.Toast(
            is_open=False,
            dismissable=True,
            duration=5000,
            className="popup-notification animate__animated animate__bounceIn fs-large",
            id="POPUP_CONNECT_TO_SPREADSHEET-TAB_HOME_COLLAPSE1"
        )
    ],
    className="form-group m-0"
)

DATABASE_CONNECT_METHOD_2 = html.Div(
    children=[

        html.Div(
            children=[
                html.H6(
                    children=[
                        "اتصال به پایگاه داده از طریق نشانی آی‌پی"
                    ],
                    className="text-center fs-medium"
                ),
            ],
            className="mb-4"
        ),
        html.Div(
            children=[

                dcc.Input(
                    placeholder='127.0.0.1:8080',
                    type='text',
                    value='',
                    className="form-control english_number col-7 fs-medium",
                    id="IP_SERVER_DATABASE-TAB_HOME_COLLAPSE1" 
                ),

                html.Div(
                    children=[
                        html.Button(
                            children=[
                                html.I(className="fa fa-database ml-2"),
                                "اتصال",
                            ],
                            n_clicks=0,
                            className="btn btn-info fs-medium",
                            id="CONNECT_TO_SERVER_DATABASE-TAB_HOME_COLLAPSE1"
                        )
                    ],
                ),
            ],
            className="d-flex justify-content-between m-0"
        ),

        dbc.Toast(
            is_open=False,
            dismissable=True,
            duration=3000,
            className="popup-notification animate__animated animate__bounceIn fs-large",
            id="POPUP_CONNECT_TO_SERVER_DATABASE-TAB_HOME_COLLAPSE1"
        )
    ],
    className="form-group m-0"
)


TAB_HOME_COLLAPSE_1 = html.Div(
    children=[

        # html.Div(
        #     children=[
        #         html.Button(
        #             children=[
        #                 html.I(
        #                     className="fa fa-database ml-2"
        #                 ),
        #                 "مدیریت پایگاه داده"
        #             ],
        #             n_clicks=0,
        #             className="btn btn-link fs-small",
        #             id="BUTTON_COLLAPSE-TAB_HOME_COLLAPSE_1"
        #         )
        #     ],
        #     className='card-header bg-light py-1'
        # ),

        html.Div(
            id="BUTTON_COLLAPSE-TAB_HOME_COLLAPSE_1",
            children=[
                html.I(
                    className="fa fa-database ml-2"
                ),
                "اتصال به پایگاه داده"
            ],
            n_clicks=0,
            className='card-header bg-light py-2 btn btn-link fs-medium w-100 text-right'
        ),

        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        DATABASE_CONNECT_METHOD_1
                                    ],
                                    className="col-xl-3 col-lg-4 col-md-5 col-sm-5 card p-3 mx-2 card-transition"
                                ),
                                html.Div(
                                    children=[
                                        DATABASE_CONNECT_METHOD_2
                                    ],
                                    className="col-xl-3 col-lg-4 col-md-5 col-sm-5 card p-3 mx-2 card-transition"
                                )
                            ],
                            className="row"
                        )
                    ],
                    className="card-body p-2"
                )
            ],
            id="COLLAPSE-TAB_HOME_COLLAPSE_1",
            is_open=False,
        ),
    ],
    className="fs-small"
)

