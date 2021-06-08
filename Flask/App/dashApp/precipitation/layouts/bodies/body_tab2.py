import base64
from dash_html_components.Div import Div
import numpy as np
from datetime import date
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_table

from App.dashApp.precipitation.callbacks.initial_settings import *
from App.dashApp.precipitation.layouts.visualizations.visualization import *


# -----------------------------------------------------------------------------
# TAB 2 - BODY
# -----------------------------------------------------------------------------


TAB_2_BODY = [
    html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                className='float-left',
                                children=[
                                    html.Img(src='data:image/png;base64,{}'.format(CALENDAR_LOGO), height=25)              
                                ]
                            ),
                            html.Div(
                                className='text-right',
                                dir="rtl",
                                children=[
                                    html.Span(
                                        children="جدیدترین ایستگاه",
                                        className="card-info-span"
                                    ),
                                    html.H6(
                                        "558 nرجه",
                                        # id="INFO_CARD_NEW_STATION-TAB1_SIDEBAR_RIGHT_CARD1",
                                        className="mt-2"
                                    ),
                                ]
                            )
                        ],
                        className='card-body text-dark px-0 py-3'
                    ),
                ],
                className='col-lg-2 card border mt-0 mb-2 mx-2 px-3 bg-light rounded'
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                className='float-left',
                                children=[
                                    html.Img(src='data:image/png;base64,{}'.format(CALENDAR_LOGO), height=25)              
                                ]
                            ),
                            html.Div(
                                className='text-right',
                                dir="rtl",
                                children=[
                                    html.Span(
                                        children="جدیدترین ایستگاه",
                                        className="card-info-span"
                                    ),
                                    html.H6(
                                        "558 nرجه",
                                        # id="INFO_CARD_NEW_STATION-TAB1_SIDEBAR_RIGHT_CARD1",
                                        className="mt-2"
                                    ),
                                ]
                            )
                        ],
                        className='card-body text-dark px-0 py-3'
                    ),
                ],
                className='col-lg-2 card border mt-0 mb-2 mx-2 px-3 bg-light rounded'
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                className='float-left',
                                children=[
                                    html.Img(src='data:image/png;base64,{}'.format(CALENDAR_LOGO), height=25)              
                                ]
                            ),
                            html.Div(
                                className='text-right',
                                dir="rtl",
                                children=[
                                    html.Span(
                                        children="جدیدترین ایستگاه",
                                        className="card-info-span"
                                    ),
                                    html.H6(
                                        "558 nرجه",
                                        # id="INFO_CARD_NEW_STATION-TAB1_SIDEBAR_RIGHT_CARD1",
                                        className="mt-2"
                                    ),
                                ]
                            )
                        ],
                        className='card-body text-dark px-0 py-3'
                    ),
                ],
                className='col-lg-2 card border mt-0 mb-2 mx-2 px-3 bg-light rounded'
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                className='float-left',
                                children=[
                                    html.Img(src='data:image/png;base64,{}'.format(CALENDAR_LOGO), height=25)              
                                ]
                            ),
                            html.Div(
                                className='text-right',
                                dir="rtl",
                                children=[
                                    html.Span(
                                        children="جدیدترین ایستگاه",
                                        className="card-info-span"
                                    ),
                                    html.H6(
                                        "558 nرجه",
                                        # id="INFO_CARD_NEW_STATION-TAB1_SIDEBAR_RIGHT_CARD1",
                                        className="mt-2"
                                    ),
                                ]
                            )
                        ],
                        className='card-body text-dark px-0 py-3'
                    ),
                ],
                className='col-lg-2 card border mt-0 mb-2 mx-2 px-3 bg-light rounded'
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                className='float-left',
                                children=[
                                    html.Img(src='data:image/png;base64,{}'.format(CALENDAR_LOGO), height=25)              
                                ]
                            ),
                            html.Div(
                                className='text-right',
                                dir="rtl",
                                children=[
                                    html.Span(
                                        children="جدیدترین ایستگاه",
                                        className="card-info-span"
                                    ),
                                    html.H6(
                                        "558 nرجه",
                                        # id="INFO_CARD_NEW_STATION-TAB1_SIDEBAR_RIGHT_CARD1",
                                        className="mt-2"
                                    ),
                                ]
                            )
                        ],
                        className='card-body text-dark px-0 py-3'
                    ),
                ],
                className='col-lg-2 card border mt-0 mb-2 mx-2 px-3 bg-light rounded'
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                className='float-left',
                                children=[
                                    html.Img(src='data:image/png;base64,{}'.format(CALENDAR_LOGO), height=25)              
                                ]
                            ),
                            html.Div(
                                className='text-right',
                                dir="rtl",
                                children=[
                                    html.Span(
                                        children="جدیدترین ایستگاه",
                                        className="card-info-span"
                                    ),
                                    html.H6(
                                        "558 nرجه",
                                        # id="INFO_CARD_NEW_STATION-TAB1_SIDEBAR_RIGHT_CARD1",
                                        className="mt-2"
                                    ),
                                ]
                            )
                        ],
                        className='card-body text-dark px-0 py-3'
                    ),
                ],
                className='col-lg-2 card border mt-0 mb-2 mx-2 px-3 bg-light rounded'
            ),

        ],
        className="row justify-content-center mt-0 pt-0",
    ),
    html.Div(
        children=[
            html.Div(
                children=[
                    dcc.Graph(
                        # id='GRAPH-TAB2_BODY_CONTENT1',
                        className="px-1 mx-1 border border-primar"
                    )
                ],
                className="col-lg-9 px-1"            
            ),
            html.Div(
                children=[
                    dcc.Graph(
                        # id='GRAPH-TAB2_BODY_CONTENT1',
                        className="px-1 mx-1 border border-primar"
                    )
                ],
                className="col-lg-3 px-1"            
            )
        ],
        className="row justify-content-between mb-2",
    )
]
