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
            className='card-header text-right bg-light'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "اتصال به پایگاه داده موجود"
                            ],
                            className="text-right",
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
                                "اتصال از طریق نشانی آی‌پی"
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
    className='card border-dark my-2 h-100'
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