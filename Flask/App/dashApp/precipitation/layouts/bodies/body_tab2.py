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


# --------------------------------------------------------------------------- #
#                                                                             #
#                                  TAB1 - BODY                                #
#                                                                             #
# --------------------------------------------------------------------------- #

TAB2_BODY_CONTENT1 = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(CALENDAR_2_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="سال جاری"
                                ),
                                html.P(
                                    id="INFO_CARD_CURRENT_YEAR_VALUE-TAB2_BODY_CONTENT1",
                                    className="text-dark pt-3 mt-1 mb-1 mx-auto"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-sm-12 col-md-6 col-lg-4 col-xl-3 card border mb-1 bg-light px-1 box'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(CALENDAR_2_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="سال گذشته"
                                ),
                                html.P(
                                    id="INFO_CARD_PREVIOUS_YEAR_VALUE-TAB2_BODY_CONTENT1",
                                    className="text-dark pt-3 mt-1 mb-1 mx-auto"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-sm-12 col-md-6 col-lg-4 col-xl-3 card border mb-1 bg-light px-1 box'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(MEAN_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="متوسط"
                                ),
                                html.P(
                                    id="INFO_CARD_MEAN_VALUE-TAB2_BODY_CONTENT1",
                                    className="text-dark pt-3 mt-1 mb-1 mx-auto"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-sm-12 col-md-6 col-lg-4 col-xl-3 card border mb-1 bg-light px-1 box'
        ),

        html.Div(
            className="w-100 d-none d-xl-block"
        ),

        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(MAX_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="بیشینه"
                                ),
                                html.P(
                                    id="INFO_CARD_MAX_VALUE-TAB2_BODY_CONTENT1",
                                    className="text-dark pt-3 mt-1 mb-1 mx-auto"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-sm-12 col-md-6 col-lg-4 col-xl-3 card border mb-1 bg-light px-1'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(MIN_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="کمینه"
                                ),
                                html.P(
                                    id="INFO_CARD_MIN_VALUE-TAB2_BODY_CONTENT1",
                                   className="text-dark pt-3 mt-1 mb-1 mx-auto"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-sm-12 col-md-6 col-lg-4 col-xl-3 card border mb-1 bg-light px-1 box'
        ),
    ],
    dir="rtl",
    className="row justify-content-center mt-2"
)


TAB2_BODY_CONTENT2 = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Graph(
                            id='GRAPH1-TAB2_BODY_CONTENT2',
                            className="w-100"
                        )
                    ],
                    className="col-sm-12 col-md-6 col-xl-4"
                ),
                html.Div(
                    children=[
                        dcc.Graph(
                            id='GRAPH2-TAB2_BODY_CONTENT2',
                            className="w-100"
                        )
                    ],
                    className="col-sm-12 col-md-6 col-xl-8"
                ),
            ],
            className="row"
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Graph(
                            id='GRAPH3-TAB2_BODY_CONTENT2',
                            className="w-100"
                        )
                    ],
                    className="col-12"
                ),
            ],
            className="row"
        )
    ],
    dir="rtl",
)


# TAB2 - BODY
# -----------------------------------------------------------------------------

TAB_2_BODY = [

    # CONTENT1 - INFO CARD
    TAB2_BODY_CONTENT1,

    html.Hr(),

    # CONTENT2 - GRAPH
    TAB2_BODY_CONTENT2

]