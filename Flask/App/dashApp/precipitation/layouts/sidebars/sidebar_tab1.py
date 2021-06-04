# --------------------------------------------------------------------------- #
#                                                                             #
#                         IMPORT REQUIREMENT MODULE                           #
#                                                                             #
# --------------------------------------------------------------------------- #

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApp.precipitation.callbacks.initial_settings import *
from App.dashApp.precipitation.layouts.visualizations.visualization import *


# --------------------------------------------------------------------------- #
#                                                                             #
#                           TAB 1 - SIDEBAR - LEFT                            #
#                                                                             #
# --------------------------------------------------------------------------- #


# SIDEBAR - LEFT - CARD 1
# --------------------------------------------------------------------------- #

TAB1_SIDEBAR_LEFT_CARD_1 = html.Div(
    children=[
        html.H6(
            children=[
                "پایگاه داده     ",
                html.Img(src='data:image/png;base64,{}'.format(DATABASE_LOGO), height=30),
            ],
            className='card-header text-right'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "اتصال به پایگاه داده موجود"
                            ],
                            className="text-right"
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    children=[
                                        "اتصال",
                                        html.I(className="fa fa-database ml-2"),
                                    ],
                                    n_clicks=0,
                                    className="btn btn-info mt-3",
                                    id="CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1"
                                )
                            ],
                            className="d-flex justify-content-start"
                        ),
                        dbc.Toast(
                            is_open=False,
                            dismissable=True,
                            duration=5000,
                            className="popup-notification",
                            id="POPUP_CONNECT_TO_EXIST_DATABASE-TAB1_SIDEBAR_CARD1"
                        )
                    ],
                    className="form-group my-0"
                ),
                html.Small(
                    children=[
                        "یا"
                    ],
                    className="breakLine text-secondary my-4"
                ),
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "اتصال به پایگاه داده از طریق نشانی آی‌پی"
                            ],
                            className='text-right'
                        ),
                        dcc.Input(
                            placeholder='127.0.0.1:8080',
                            type='text',
                            value='',
                            className="form-control mt-4 english_number",
                            id="IP_SERVER_DATABASE-TAB1_SIDEBAR_CARD1",
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    children=[
                                        "اتصال",
                                        html.I(className="fa fa-database ml-2"),
                                    ],
                                    n_clicks=0,
                                    className="btn btn-info mt-4",
                                    id="CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1"
                                )
                            ],
                            className="d-flex justify-content-start"
                        ),
                        dbc.Toast(
                            is_open=False,
                            dismissable=True,
                            duration=5000,
                            className="popup-notification",
                            id="POPUP_CONNECT_TO_SERVER_DATABASE-TAB1_SIDEBAR_CARD1"
                        )
                    ],
                    className="form-group my-0"
                ),
            ],
            className='card-body text-dark'
        ),
    ],
    className='card border-dark my-2'
)



# TAB 1 - SIDEBAR - LEFT
# --------------------------------------------------------------------------- #

TAB_1_SIDEBAR_LEFT = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB1_SIDEBAR_LEFT_CARD_1
                    ],
                    className='col px-0'
                ),
            ],
            className='row'
        ),
    ],
    className="container-fluid"
)


# --------------------------------------------------------------------------- #
#                                                                             #
#                           TAB 1 - SIDEBAR - RIGHT                            #
#                                                                             #
# --------------------------------------------------------------------------- #


# SIDEBAR - RIGHT - CARD 1
# --------------------------------------------------------------------------- #

TAB1_SIDEBAR_RIGHT_CARD_1 = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(src='data:image/png;base64,{}'.format(DRAINAGE_BASIN_LOGO), height=50)              
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.H4(
                                    id="INFO_CARD_NUMBER_HOZE30-TAB1_SIDEBAR_RIGHT_CARD1"
                                ),
                                html.Span(
                                    children="حوزه آبریز"
                                )
                            ]
                        )
                    ],
                    className='card-body text-dark'
                ),
            ],
            className='card border-dark my-2 bg-light'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(src='data:image/png;base64,{}'.format(STUDY_AREA_LOGO), height=50)              
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.H4(
                                    id="INFO_CARD_NUMBER_MAHDOUDE-TAB1_SIDEBAR_RIGHT_CARD1"
                                ),
                                html.Span(
                                    children="محدوده مطالعاتی"
                                )                        
                            ]
                        )
                    ],
                    className='card-body text-dark'
                ),
            ],
            className='card border-dark my-2 bg-light'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(src='data:image/png;base64,{}'.format(DROP_WATER_LOGO), height=50)              
                            ]
                        ),
                        html.Div(
                            className='text-right',
                            dir="rtl",
                            children=[
                                html.H4(
                                    id="INFO_CARD_NUMBER_STATION-TAB1_SIDEBAR_RIGHT_CARD1"
                                ),
                                html.Span(
                                    children="ایستگاه"
                                )                        
                            ]
                        )
                    ],
                    className='card-body text-dark'
                ),
            ],
            className='card border-dark my-2 bg-light'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(src='data:image/png;base64,{}'.format(ALTITUDE_LOGO), height=50)              
                            ]
                        ),
                        html.Div(
                            className='text-right',
                            dir="rtl",
                            children=[
                                html.H5(
                                    id="INFO_CARD_HIGH_ELEV_STATION-TAB1_SIDEBAR_RIGHT_CARD1"
                                ),
                                html.Span(
                                    children="مرتفع‌ترین ایستگاه"
                                )                        
                            ]
                        )
                    ],
                    className='card-body text-dark'
                ),
            ],
            className='card border-dark my-2 bg-light'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(src='data:image/png;base64,{}'.format(ALTITUDE_LOGO), height=50)
                            ]
                        ),
                        html.Div(
                            className='text-right',
                            dir="rtl",
                            children=[
                                html.H5(
                                    id="INFO_CARD_LOW_ELEV_STATION-TAB1_SIDEBAR_RIGHT_CARD1"
                                ),
                                html.Span(
                                    children="پست‌ترین ایستگاه"
                                )                        
                            ]
                        )
                    ],
                    className='card-body text-dark'
                ),
            ],
            className='card border-dark my-2 bg-light'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(src='data:image/png;base64,{}'.format(CALENDAR_LOGO), height=50)              
                            ]
                        ),
                        html.Div(
                            className='text-right',
                            dir="rtl",
                            children=[
                                html.H5(
                                    id="INFO_CARD_OLD_STATION-TAB1_SIDEBAR_RIGHT_CARD1"
                                ),
                                html.Span(
                                    children="قدیمی‌ترین ایستگاه"
                                )                        
                            ]
                        )
                    ],
                    className='card-body text-dark'
                ),
            ],
            className='card border-dark my-2 bg-light'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(src='data:image/png;base64,{}'.format(CALENDAR_LOGO), height=50)              
                            ]
                        ),
                        html.Div(
                            className='text-right',
                            dir="rtl",
                            children=[
                                html.H5(
                                    id="INFO_CARD_NEW_STATION-TAB1_SIDEBAR_RIGHT_CARD1"
                                ),
                                html.Span(
                                    children="جدیدترین ایستگاه"
                                )                        
                            ]
                        )
                    ],
                    className='card-body text-dark'
                ),
            ],
            className='card border-dark my-2 bg-light'
        ),
    ]
)


# TAB 1 - SIDEBAR - RIGHT
# --------------------------------------------------------------------------- #

TAB_1_SIDEBAR_RIGHT = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB1_SIDEBAR_RIGHT_CARD_1
                    ],
                    className='col px-0'
                ),
            ],
            className='row'
        ),
    ],
    className="container-fluid"
)
