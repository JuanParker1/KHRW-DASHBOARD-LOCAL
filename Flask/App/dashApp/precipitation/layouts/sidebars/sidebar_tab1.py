import base64
import numpy as np
from datetime import date
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_table


# -----------------------------------------------------------------------------
# Tab 1 - Sidebar
# -----------------------------------------------------------------------------

"""
---------------------------------------
Left - Card 1: 
---------------------------------------
"""

LEFT_CARD_1_IMG = base64.b64encode(
    open('assets/images/excel_logo.png', 'rb').read())

LEFT_CARD_1 = html.Div(
    children=[
        html.H6(
            children=[
                html.Img(
                    src='data:image/png;base64,{}'.format(LEFT_CARD_1_IMG.decode()), height=30),
                "       Load Data From File"
            ],
            className='card-header in'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Label(
                            children=[
                                "Connect To An Existing Spreadsheet"
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    children=[
                                        "Connect"
                                    ],
                                    n_clicks=0,
                                    className="btn btn-success mt-3"
                                ),
                            ],
                            className="d-flex justify-content-end"
                        )
                    ],
                    className="form-group my-0"
                ),
                html.Small(
                    children=[
                        "OR"
                    ],
                    className="breakLine text-secondary my-4"
                ),
                html.Div(
                    children=[
                        dcc.Upload([
                            'Drag and Drop or ',
                            html.A(html.B('Select a File')),
                        ],
                            className="upload-button",
                            id="upload_button_TAB1_SIDEBAR_CARD1",
                            accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
                    ],
                    className='card-text text-center'
                ),
                html.Div(
                    children=[
                        html.Button(
                            children=[
                                "Connect"
                            ],
                            n_clicks=0,
                            className="btn btn-success mt-3",
                            id="connect_button_TAB1_SIDEBAR_CARD1_CONNECT2"
                        ),
                        dbc.Toast(
                            id="database_generator_toast_TAB1_SIDEBAR_CARD1_CONNECT2",
                            is_open=False,
                            dismissable=True,
                            duration=5000,
                            style={
                                "position": "fixed",
                                "top": 48,
                                "right": 50,
                                "width": 350
                            },
                        )
                    ],
                    className="d-flex justify-content-end"
                )
            ],
            className='card-body text-dark'
        ),
        html.Div(
            children=[
                html.H6(
                    id="show_filename_selected_TAB1_SIDEBAR_CARD1"
                )
            ],
            className='card-footer'
        ),
    ],
    className='card border-dark mb-2'
)


"""
---------------------------------------
Left - Card 2: 
---------------------------------------
"""

LEFT_CARD_2_IMG = base64.b64encode(
    open('assets/images/database_logo.png', 'rb').read())

LEFT_CARD_2 = html.Div(
    children=[
        html.H6(
            children=[
                html.Img(
                    src='data:image/png;base64,{}'.format(LEFT_CARD_2_IMG.decode()), height=30),
                "       Load Data From Database"
            ],
            className='card-header'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Label(
                            children=[
                                "Connect To An Existing Database"
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    children=[
                                        "Connect"
                                    ],
                                    n_clicks=0,
                                    className="btn btn-info mt-3"
                                )
                            ],
                            className="d-flex justify-content-end"
                        )
                    ],
                    className="form-group my-0"
                ),
                html.Small(
                    children=[
                        "OR"
                    ],
                    className="breakLine text-secondary my-4"
                ),
                html.Div(
                    children=[
                        html.Label(
                            children=[
                                "Connect To Database Server"
                            ]
                        ),
                        dcc.Input(
                            placeholder='127.0.0.1:8080',
                            type='text',
                            value='',
                            className="form-control"
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    children=[
                                        "Connect"
                                    ],
                                    n_clicks=0,
                                    className="btn btn-info mt-3"
                                )
                            ],
                            className="d-flex justify-content-end"
                        )
                    ],
                    className="form-group my-0"
                ),
                html.Small(
                    children=[
                        "OR"
                    ],
                    className="breakLine text-secondary my-4"
                ),
                html.Div(
                    children=[
                        html.Label(
                            children=[
                                "Connect To Local Database"
                            ]
                        ),
                        html.Div(
                            children=[
                                dcc.Upload([
                                    'Drag and Drop or ',
                                    html.A(html.B('Select a File'))
                                ],
                                    className="upload-button")
                            ],
                            className='card-text text-center'
                        ),
                        html.Div(
                            children=[
                                html.Button(
                                    children=[
                                        "Connect"
                                    ],
                                    n_clicks=0,
                                    className="btn btn-info mt-3"
                                )
                            ],
                            className="d-flex justify-content-end"
                        )
                    ],
                    className="form-group my-0"
                ),
            ],
            className='card-body text-dark'
        ),
        html.Div(
            children=[
                "Card Footer"
            ],
            className='card-footer'
        ),
    ],
    className='card border-dark mb-2'
)


"""
---------------------------------------
Sidebar Tab 1
---------------------------------------
"""

TAB_1_SIDEBAR = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        LEFT_CARD_1,
                        LEFT_CARD_2
                    ],
                    className='col px-0'
                ),
            ],
            className='row'
        ),
    ],
    className="container-fluid"
)
