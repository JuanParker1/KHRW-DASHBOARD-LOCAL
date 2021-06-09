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
                                    src='data:image/png;base64,{}'.format(DRAINAGE_BASIN_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="حوزه آبریز درجه 1"
                                ),
                                html.H6(
                                    # id="INFO_CARD_NUMBER_HOZE6-TAB1_SIDEBAR_RIGHT_CARD1",
                                    className="text-primary pt-3"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-md-6 col-lg-3 col-xl-2 card border mb-1 bg-light px-1'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(DRAINAGE_BASIN_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children=" حوزه آبریز درجه 2"
                                ),
                                html.H6(
                                    # id="INFO_CARD_NUMBER_HOZE30-TAB1_SIDEBAR_RIGHT_CARD1",
                                    className="text-primary pt-3"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-md-6 col-lg-3 col-xl-2 card border mb-1 bg-light px-1 box'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(DRAINAGE_BASIN_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="حوزه آبریز درجه 1"
                                ),
                                html.H6(
                                    # id="INFO_CARD_NUMBER_HOZE6-TAB1_SIDEBAR_RIGHT_CARD1",
                                    className="text-primary pt-3"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-md-6 col-lg-3 col-xl-2 card border mb-1 bg-light px-1'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(DRAINAGE_BASIN_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children=" حوزه آبریز درجه 2"
                                ),
                                html.H6(
                                    # id="INFO_CARD_NUMBER_HOZE30-TAB1_SIDEBAR_RIGHT_CARD1",
                                    className="text-primary pt-3"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-md-6 col-lg-3 col-xl-2 card border mb-1 bg-light px-1 box'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(DRAINAGE_BASIN_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="حوزه آبریز درجه 1"
                                ),
                                html.H6(
                                    # id="INFO_CARD_NUMBER_HOZE6-TAB1_SIDEBAR_RIGHT_CARD1",
                                    className="text-primary pt-3"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-md-6 col-lg-3 col-xl-2 card border mb-1 bg-light px-1'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(DRAINAGE_BASIN_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children=" حوزه آبریز درجه 2"
                                ),
                                html.H6(
                                    # id="INFO_CARD_NUMBER_HOZE30-TAB1_SIDEBAR_RIGHT_CARD1",
                                    className="text-primary pt-3"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-md-6 col-lg-3 col-xl-2 card border mb-1 bg-light px-1 box'
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
                                    src='data:image/png;base64,{}'.format(DROP_WATER_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="ایستگاه"
                                ),
                                html.H6(
                                    # id="INFO_CARD_NUMBER_STATION-TAB1_SIDEBAR_RIGHT_CARD1",
                                    className="text-primary pt-3"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-md-6 col-lg-3 col-xl-2 card border mb-1 bg-light px-1'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(STUDY_AREA_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="محدوده مطالعاتی"
                                ),
                                html.H6(
                                    # id="INFO_CARD_NUMBER_MAHDOUDE-TAB1_SIDEBAR_RIGHT_CARD1",
                                    className="text-primary pt-3"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-md-6 col-lg-3 col-xl-2 card border mb-1 bg-light px-1'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(ALTITUDE_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="پست‌ترین ایستگاه"
                                ),
                                html.H6(
                                    # id="INFO_CARD_LOW_ELEV_STATION-TAB1_SIDEBAR_RIGHT_CARD1",
                                    className="text-primary pt-3"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-md-6 col-lg-3 col-xl-2 card border mb-1 bg-light px-1'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(ALTITUDE_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="مرتفع‌ترین ایستگاه"
                                ),
                                html.H6(
                                    # id="INFO_CARD_HIGH_ELEV_STATION-TAB1_SIDEBAR_RIGHT_CARD1",
                                    className="text-primary pt-3"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-md-6 col-lg-3 col-xl-2 card border mb-1 bg-light px-1'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(CALENDAR_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="قدیمی‌ترین ایستگاه"
                                ),
                                html.H6(
                                    # id="INFO_CARD_OLD_STATION-TAB1_SIDEBAR_RIGHT_CARD1",
                                    className="text-primary pt-3"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-md-6 col-lg-3 col-xl-2 card border mb-1 bg-light px-1'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(CALENDAR_LOGO), height=25)
                            ]
                        ),
                        html.Div(
                            className='text-right',
                            dir="rtl",
                            children=[
                                html.Span(
                                    children="جدیدترین ایستگاه"
                                ),
                                html.H6(
                                    # id="INFO_CARD_NEW_STATION-TAB1_SIDEBAR_RIGHT_CARD1",
                                    className="text-primary pt-3"
                                ),
                            ]
                        )
                    ],
                    className='card-body text-dark p-2'
                ),
            ],
            className='col-md-6 col-lg-3 col-xl-2 card border mb-1 bg-light px-1'
        )
    ],
    dir="rtl",
    className="row justify-content-center mt-2"
)


# TAB2 - BODY
# -----------------------------------------------------------------------------

TAB_2_BODY = [

    # CONTENT1 - INFO CARD
    TAB2_BODY_CONTENT1,

    html.Hr(),

    # CONTENT2 - CREATE MAP
    html.Div(
        children=[
            # TAB1_BODY_CONTENT2
        ],
        className="row my-2",
    ),

    # CONTENT3 - CREATE TABLE
    html.Div(
        children=[
            html.Div(
                children=[
                    # TAB1_BODY_CONTENT3
                ],
                className="w-100 h-100"
            )
        ],
        className="row"
    )

]
