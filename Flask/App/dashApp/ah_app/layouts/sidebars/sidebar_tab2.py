import base64
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from layouts.visualizations.visualization import *



# -----------------------------------------------------------------------------
# Tab 2 - Sidebar - Left
# -----------------------------------------------------------------------------

"""
---------------------------------------
Left - Card 1: 
---------------------------------------
"""

LEFT_CARD_1_IMG = base64.b64encode(
   open('assets/images/well.png', 'rb').read()
)  # EDITPATH



LEFT_CARD_1 = html.Div(
    children=[
        html.H6(
            children=[
                "   انتخاب چاه مشاهده‌ای",
                html.Img(src='data:image/png;base64,{}'.format(LEFT_CARD_1_IMG.decode()), height=30),
            ],
            className='card-header text-right'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "انتخاب آبخوان:"
                            ],
                            dir="rtl",
                            className="text-right "
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1",
                                    placeholder="یک یا چند آبخوان انتخاب کنید",
                                    multi=True,
                                    # persistence=True,
                                    # persistence_type="memory",
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
                                "انتخاب چاه مشاهده‌ای:"
                            ],
                            dir="rtl",
                            className="text-right "
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1",
                                    placeholder="یک یا چند چاه مشاهده‌ای انتخاب کنید",
                                    multi=True,
                                    # persistence=True,
                                    # persistence_type="memory",
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
                                    # persistence=True,
                                    # persistence_type="memory",
                                    options=[
                                        {'label': '{}'.format(i), 'value': i} for i in range(1370, 1426)
                                    ]
                                ),
                                dcc.Dropdown(
                                    id="SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1",
                                    placeholder="سال پایان",
                                    # persistence=True,
                                    # persistence_type="memory",

                                )
                            ],
                        ),
                    ],
                    className="form-group mb-4"
                ),
                html.Div(
                    children=[
                        MAP_TAB2_SIDEBAR_LEFT_CARD1
                    ],
                    className="form-group mb-0"
                ),
            ],
            className='card-body text-dark'
        ),
    ],
    className='card border-dark my-2'
)



# """
# ---------------------------------------
# Left - Card 2: 
# ---------------------------------------
# """

# LEFT_CARD_2_IMG = base64.b64encode(
#     open('assets/images/excel_logo.png', 'rb').read())  # EDITPATH

# LEFT_CARD_2 = html.Div(
#     children=[
#         html.H6(
#             children=[
#                 "صفحه گسترده     ",
#                 html.Img(
#                     src='data:image/png;base64,{}'.format(LEFT_CARD_2_IMG.decode()), height=30),
#             ],
#             className='card-header text-right'
#         ),
#         html.Div(
#             children=[
#                 html.Div(
#                     children=[
#                         html.H6(
#                             children=[
#                                 "ایجاد پایگاه داده از فایل صفحه گسترده"
#                             ],
#                             className="text-right pb-3"
#                         ),
#                         dcc.Upload([
#                             html.B(
#                                 'انتخاب فایل',
#                                 className='font-weight-light'
#                             ),
#                         ],
#                             className="upload-button m-auto",
#                             #id="CHOOSE_SPREADSHEET-TAB1_SIDEBAR_CARD2",
#                             accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#                         ),
#                         html.Small(
#                             dir="rtl",
#                             #id="FILENAME_SPREADSHEET-TAB1_SIDEBAR_CARD2",
#                         )
#                     ],
#                     className='card-text text-center'
#                 ),
#                 html.Div(
#                     children=[
#                         html.Button(
#                             children=[
#                                 "ایجاد"
#                             ],
#                             n_clicks=0,
#                             className="btn btn-success mt-3",
#                             #id="CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2",
#                         ),
#                         dbc.Toast(
#                             is_open=False,
#                             dismissable=True,
#                             duration=5000,
#                             className="popup-notification",
#                             #id="POPUP_CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2"
#                         )
#                     ],
#                     className="d-flex justify-content-start"
#                 )
#             ],
#             className='card-body text-dark'
#         ),
#     ],
#     className='card border-dark my-2'
# )


"""
---------------------------------------
Sidebar Tab 1 - Left
---------------------------------------
"""

TAB_2_SIDEBAR_LEFT = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        LEFT_CARD_1,
                        # LEFT_CARD_2,
                    ],
                    className='col px-0'
                ),
            ],
            className='row'
        ),
    ],
    className="container-fluid"
)






# -----------------------------------------------------------------------------
# Tab 2 - Sidebar - Right
# -----------------------------------------------------------------------------


"""
---------------------------------------
Right - Card 1
---------------------------------------
"""

RIGHT_CARD_1_IMG_1 = base64.b64encode(
   open('assets/images/aquifer.jpg', 'rb').read()
)  # EDITPATH

RIGHT_CARD_1_IMG_2 = base64.b64encode(
   open('assets/images/well.png', 'rb').read()
)  # EDITPATH

RIGHT_CARD_1 = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(src='data:image/png;base64,{}'.format(RIGHT_CARD_1_IMG_1.decode()), height=60)              
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.H4(
                                    #id="INFO_CARD_NUMBER_AQUIFER-TAB1_SIDEBAR_RIGHT_CARD1"
                                ),
                                html.Span(
                                    children="آبخوان‌های موجود"
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
                                html.Img(src='data:image/png;base64,{}'.format(RIGHT_CARD_1_IMG_2.decode()), height=60)              
                            ]
                        ),
                        html.Div(
                            className='text-right',
                            dir="rtl",
                            children=[
                                html.H4(
                                    #id="INFO_CARD_NUMBER_WELL-TAB1_SIDEBAR_RIGHT_CARD1"
                                ),
                                html.Span(
                                    children="چاه‌های مشاهده‌ای موجود"
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



"""
---------------------------------------
Sidebar Tab 2 - Right
---------------------------------------
"""

TAB_2_SIDEBAR_RIGHT = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        RIGHT_CARD_1
                    ],
                    className='col px-0'
                ),
            ],
            className='row'
        ),
    ],
    className="container-fluid"
)
