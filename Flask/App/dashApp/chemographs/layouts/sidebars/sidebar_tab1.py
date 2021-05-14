import base64
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


# -----------------------------------------------------------------------------
# Tab 1 - Sidebar - Left
# -----------------------------------------------------------------------------

"""
---------------------------------------
Left - Card 1: 
---------------------------------------
"""

TAB1_SIDEBAR_LEFT_CARD_1_IMG = base64.b64encode(
    open('assets/images/database_logo.png', 'rb').read())  # EDITPATH

TAB1_SIDEBAR_LEFT_CARD_1 = html.Div(
    children=[
        html.H6(
            children=[
                "پایگاه داده     ",
                html.Img(src='data:image/png;base64,{}'.format(TAB1_SIDEBAR_LEFT_CARD_1_IMG.decode()), height=30),
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



"""
---------------------------------------
Left - Card 2: 
---------------------------------------
"""

TAB1_SIDEBAR_LEFT_CARD_2_IMG = base64.b64encode(
    open('assets/images/excel_logo.png', 'rb').read())  # EDITPATH

TAB1_SIDEBAR_LEFT_CARD_2 = html.Div(
    children=[
        html.H6(
            children=[
                "صفحه گسترده     ",
                html.Img(
                    src='data:image/png;base64,{}'.format(TAB1_SIDEBAR_LEFT_CARD_2_IMG.decode()), height=30),
            ],
            className='card-header text-right'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "ایجاد پایگاه داده از فایل صفحه گسترده"
                            ],
                            className="text-right pb-3"
                        ),
                        dcc.Upload([
                            html.B(
                                children=[
                                    'انتخاب فایل',
                                    html.I(className="fa fa-cloud-upload ml-2"),
                                ],
                                className='font-weight-light'
                            ),
                        ],
                            className="upload-button m-auto",
                            id="CHOOSE_SPREADSHEET-TAB1_SIDEBAR_CARD2",
                            accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        ),
                        html.Small(
                            dir="rtl",
                            id="FILENAME_SPREADSHEET-TAB1_SIDEBAR_CARD2",
                        )
                    ],
                    className='card-text text-center'
                ),
                html.Div(
                    children=[
                        html.Button(
                            children=[
                                "ایجاد"
                            ],
                            n_clicks=0,
                            className="btn btn-success mt-3",
                            id="CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2",
                        ),
                        dbc.Toast(
                            is_open=False,
                            dismissable=True,
                            duration=5000,
                            className="popup-notification",
                            id="POPUP_CONNECT_TO_SPREADSHEET-TAB1_SIDEBAR_CARD2"
                        )
                    ],
                    className="d-flex justify-content-start"
                )
            ],
            className='card-body text-dark'
        ),
    ],
    className='card border-dark my-2'
)




"""
---------------------------------------
Left - Card 3: DEBUG
---------------------------------------
"""

TAB1_SIDEBAR_LEFT_CARD_3 = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Input(
                    id="DEBUG_CONTENT-TAB1_SIDEBAR_LEFT_CARD3",
                    type="text",
                    placeholder="Input Variable Name",
                    className="form-control"
                ),
                html.Div(
                    children=[
                        html.Button(
                            children=[
                                "اجرا"
                            ],
                            n_clicks=0,
                            className="btn btn-success mt-3",
                            id="DEBUG_BUTTON-TAB1_SIDEBAR_CARD3",
                        ),
                    ],
                    className="d-flex justify-content-start"
                ),
                html.Div(id="DEBUG_OUTPUT-TAB1_SIDEBAR_CARD3"),
            ],
        className='card-body text-dark'
        ),
    ],
    className='card border-dark my-2'
)






"""
---------------------------------------
Sidebar Tab 1 - Left
---------------------------------------
"""

TAB_1_SIDEBAR_LEFT = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB1_SIDEBAR_LEFT_CARD_1,
                        TAB1_SIDEBAR_LEFT_CARD_2,
                        # TAB1_SIDEBAR_LEFT_CARD_3
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
# Tab 1 - Sidebar - Right
# -----------------------------------------------------------------------------


"""
---------------------------------------
Right - Card 1
---------------------------------------
"""

TAB1_SIDEBAR_RIGHT_CARD_1_IMG_1 = base64.b64encode(
   open('assets/images/aquifer.jpg', 'rb').read()
)  # EDITPATH

TAB1_SIDEBAR_RIGHT_CARD_1_IMG_2 = base64.b64encode(
   open('assets/images/location_marker.png', 'rb').read()
)  # EDITPATH

TAB1_SIDEBAR_RIGHT_CARD_1 = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            className='float-left',
                            children=[
                                html.Img(src='data:image/png;base64,{}'.format(TAB1_SIDEBAR_RIGHT_CARD_1_IMG_1.decode()), height=60)              
                            ]
                        ),
                        html.Div(
                            className='text-right ',
                            dir="rtl",
                            children=[
                                html.H4(
                                    id="INFO_CARD_NUMBER_AQUIFER-TAB1_SIDEBAR_RIGHT_CARD1"
                                ),
                                html.Span(
                                    children="آبخوان‌"
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
                                html.Img(src='data:image/png;base64,{}'.format(TAB1_SIDEBAR_RIGHT_CARD_1_IMG_2.decode()), height=60)              
                            ]
                        ),
                        html.Div(
                            className='text-right',
                            dir="rtl",
                            children=[
                                html.H4(
                                    id="INFO_CARD_NUMBER_WELL-TAB1_SIDEBAR_RIGHT_CARD1"
                                ),
                                html.Span(
                                    children="محل نمونه برداری"
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
Sidebar Tab 1 - Right
---------------------------------------
"""

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
