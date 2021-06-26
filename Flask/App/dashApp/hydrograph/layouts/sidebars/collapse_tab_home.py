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
        html.H6(
            children=[
                "اتصال به پایگاه داده موجود"
            ],
            className="text-right fs-small"
        ),
        html.Div(
            children=[
                html.Button(
                    children=[
                        html.I(className="fa fa-database ml-2"),
                        "اتصال",
                    ],
                    n_clicks=0,
                    className="btn btn-info fs-small",
                    id="CONNECT_TO_EXIST_DATABASE-TAB_HOME_COLLAPSE1"
                )
            ],
            className="d-flex justify-content-end"
        ),
        dbc.Toast(
            is_open=False,
            dismissable=True,
            duration=5000,
            className="popup-notification",
            id="POPUP_CONNECT_TO_EXIST_DATABASE-TAB_HOME_COLLAPSE1"
        )
    ],
    className="form-group m-0"
)

DATABASE_CONNECT_METHOD_2 = html.Div(
    children=[

        html.H6(
            children=[
                "اتصال به پایگاه داده از طریق نشانی آی‌پی"
            ],
            className='text-right fs-small'
        ),

        html.Div(
            children=[

                dcc.Input(
                    placeholder='127.0.0.1:8080',
                    type='text',
                    value='',
                    className="form-control english_number col-8 fs-small",
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
                            className="btn btn-info fs-small",
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
            duration=5000,
            className="popup-notification",
            id="POPUP_CONNECT_TO_SERVER_DATABASE-TAB_HOME_COLLAPSE1"
        )
    ],
    className="form-group m-0"
)


TAB_HOME_COLLAPSE_1 = html.Div(
    children=[

        html.Div(
            children=[
                html.Button(
                    children=[
                        html.I(
                            className="fa fa-database ml-2"
                        ),
                        "مدیریت پایگاه داده"
                    ],
                    n_clicks=0,
                    className="btn btn-link fs-small",
                    id="BUTTON_COLLAPSE-TAB_HOME_COLLAPSE_1"
                )
            ],
            className='card-header bg-light py-1'
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
                                    className="col-xl-2 col-lg-3 col-md-4 col-sm-5 card p-2 mx-2"
                                ),
                                html.Div(
                                    children=[
                                        DATABASE_CONNECT_METHOD_2
                                    ],
                                    className="col-xl-2 col-lg-3 col-md-4 col-sm-5 card p-2 mx-2"
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