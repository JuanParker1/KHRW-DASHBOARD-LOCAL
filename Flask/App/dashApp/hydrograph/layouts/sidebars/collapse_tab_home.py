import base64
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_html_components.Button import Button

from App.dashApp.hydrograph.layouts.visualizations.visualization import *

# -------------------------------------------------------------------------------------------------
# TAB HOME - COLLAPSE
# -------------------------------------------------------------------------------------------------


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


# COLLAPSE - TAB HOME
# ------------------------------------------------------------------------

TAB_HOME_COLLAPSE = html.Div(
    children=[
        TAB_HOME_COLLAPSE_1,
    ],
    className="col-12"
)