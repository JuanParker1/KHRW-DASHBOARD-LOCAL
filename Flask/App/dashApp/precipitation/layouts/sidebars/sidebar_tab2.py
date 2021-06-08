# --------------------------------------------------------------------------- #
#                                                                             #
#                         IMPORT REQUIREMENT MODULE                           #
#                                                                             #
# --------------------------------------------------------------------------- #

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_html_components.Div import Div

from App.dashApp.precipitation.callbacks.initial_settings import *


# --------------------------------------------------------------------------- #
#                                                                             #
#                           TAB 2 - SIDEBAR - LEFT                            #
#                                                                             #
# --------------------------------------------------------------------------- #

# SIDEBAR - LEFT - CARD 1
# --------------------------------------------------------------------------- #

TAB2_SIDEBAR_LEFT_CARD_1 = html.Div(
    children=[
        html.H6(
            children=[
                "   تحلیل ایستگاهی",
                html.Img(src='data:image/png;base64,{}'.format(DROP_WATER_LOGO), height=30, className="ml-2"),
            ],
            className='card-header text-right'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "انتخاب حوزه آبریز:"
                            ],
                            dir="rtl",
                            className="text-right "
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="SELECT_HOZE30-TAB2_SIDEBAR_LEFT_CARD1",
                                    placeholder="یک یا چند حوزه انتخاب کنید",
                                    multi=True,
                                    className="dash-dropdown-select",
                                    
                                )
                            ],
                        ),
                    ],
                    className="form-group mb-4"
                ),
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "انتخاب محدوده مطالعاتی:"
                            ],
                            dir="rtl",
                            className="text-right "
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="SELECT_MAHDOUDE-TAB2_SIDEBAR_LEFT_CARD1",
                                    placeholder="یک یا چند محدوده مطالعاتی انتخاب کنید",
                                    multi=True,
                                    className="dash-dropdown-select"
                                )
                            ],
                        ),
                    ],
                    className="form-group mb-4"
                ),
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "انتخاب ایستگاه:"
                            ],
                            dir="rtl",
                            className="text-right "
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="SELECT_STATION-TAB2_SIDEBAR_LEFT_CARD1",
                                    placeholder="یک یا چند ایستگاه انتخاب کنید",
                                    multi=True,
                                    className="dash-dropdown-select"
                                )
                            ],
                        ),
                    ],
                    className="form-group mb-4"
                ),
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "انتخاب بازه زمانی:"
                            ],
                            dir="rtl",
                            className="text-right "
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1",
                                    placeholder="سال شروع",
                                    options=[
                                        {'label': '{}'.format(i), 'value': i} for i in range(1369, 1426)
                                    ],
                                    value=1369
                                ),
                                dcc.Dropdown(
                                    id="SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1",
                                    placeholder="سال پایان",
                                    value=1400
                                )
                            ],
                        ),
                    ],
                    className="form-group mb-4"
                ),
                html.Div(
                    children=[
                        dcc.Graph(
                            id='MAP-TAB2_SIDEBAR_LEFT_CARD1',
                            className="sidebar-map"
                        )
                    ],
                    className="form-group mb-0 mx-0"
                ),
            ],
            className='card-body text-dark'
        ),
    ],
    className='card border-dark my-2'
)


# # SIDEBAR - LEFT - CARD 2 - DEBUG
# # --------------------------------------------------------------------------- #

# TAB2_SIDEBAR_LEFT_CARD_2 = html.Div(
#     children=[
#         html.Div(
#             children=[
#                 dcc.Input(
#                     id="DEBUG_CONTENT-TAB2_SIDEBAR_LEFT_CARD2",
#                     type="text",
#                     placeholder="Input Variable Name",
#                     className="form-control"
#                 ),
#                 html.Div(
#                     children=[
#                         html.Button(
#                             children=[
#                                 "اجرا"
#                             ],
#                             n_clicks=0,
#                             className="btn btn-success mt-3",
#                             id="DEBUG_BUTTON-TAB2_SIDEBAR_CARD2",
#                         ),
#                     ],
#                     className="d-flex justify-content-start"
#                 ),
#                 html.Div(id="DEBUG_OUTPUT-TAB2_SIDEBAR_CARD2"),
#             ],
#         className='card-body text-dark'
#         ),
#     ],
#     className='card border-dark my-2'
# )


# TAB 2 - SIDEBAR - LEFT
# --------------------------------------------------------------------------- #

TAB_2_SIDEBAR_LEFT = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB2_SIDEBAR_LEFT_CARD_1,
                        # TAB2_SIDEBAR_LEFT_CARD_2
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
#                           TAB 2 - SIDEBAR - Right                           #
#                                                                             #
# --------------------------------------------------------------------------- #

# SIDEBAR - RIGHT - CARD 1
# --------------------------------------------------------------------------- #

TAB2_SIDEBAR_RIGHT_CARD_1 = html.Div(
    className='mt-2 text-right border border-secondary rounded',
    dir="rtl",
    children=[
        html.Div(
            className='card bg-light',
            children=[
                html.Img(
                    id="IMG_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                    height=220,
                    width=220,
                    className="mt-3 rounded mx-auto d-block"
                ),
                html.Div(
                    className='card-body',
                    children=[
                        html.H5(
                            id="NAME_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='card-title mb-0',
                        ),
                        # html.P(
                        #     className='card-text',
                        #     children='چاه حسن آباد در آبخوان جوین واقع شده است.'
                        # )                        
                    ]
                ),
                html.Ul(
                    className='list-group list-group-flush',
                    children=[
                        html.Li(
                            id="ID_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item'
                        ),                      
                        html.Li(
                            id="AQUIFER_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item',
                        ),
                        html.Li(
                            id="LONG_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item',
                        ),
                        html.Li(
                            id="LAT_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item',
                        ),
                        html.Li(
                            id="ELEV_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item',
                        ),
                        html.Li(
                            id="START_DATE_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item'
                        ),
                        html.Li(
                            id="END_DATE_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item'
                        ),
                    ]
                )
            ]
        )
    ]
)


# TAB 2 - SIDEBAR - Right
# --------------------------------------------------------------------------- #

TAB_2_SIDEBAR_RIGHT = html.Div(
    id="SHOW_HIDE-TAB2_SIDEBAR_RIGHT",
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB2_SIDEBAR_RIGHT_CARD_1
                    ],
                    className='col px-0'
                ),
            ],
            className='row'
        ),
    ],
    className="container-fluid"
)
