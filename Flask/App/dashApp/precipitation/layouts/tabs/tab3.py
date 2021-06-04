import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApp.precipitation.layouts.headers.header import *
from App.dashApp.precipitation.layouts.sidebars.sidebar import *
from App.dashApp.precipitation.layouts.bodies.body import *
from App.dashApp.precipitation.layouts.footers.footer import *


# -----------------------------------------------------------------------------
# Tab 3
# -----------------------------------------------------------------------------


TAB_3 = html.Div(
    children=[
        # Header --------------------------------------------------------------
        html.Div(
            children=[
                html.Div(
                    children=[
                        # TAB_3_HEADER
                    ],
                    className="col text-center"
                )
            ],
            className="row"
        ),
        # Sidebars & Body ------------------------------------------------------
        html.Div(
            children=[
                # Sidebar Left ----------------------------
                html.Div(
                    children=[
                        TAB_3_SIDEBAR_LEFT
                    ],
                    className='left-sidebar'
                ),
                # Body ------------------------------------
                html.Div(
                    children=[
                        html.Div(
                            children=TAB_3_BODY,
                            className="container-fluid"
                        )
                    ],
                    className='my-body-tab3 pt-2'
                ),
                # Sidebar right ---------------------------
                html.Div(
                    children=[
                        # TAB_3_SIDEBAR_RIGHT
                    ],
                    className='right-sidebar'
                ),
            ],
            className="row p-0 m-0 w-100"
        ),
        # Footer --------------------------------------------------------------
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB_3_FOOTER
                    ],
                    className="col"
                )
            ],
            className="row"
        ),
    ],
    className="container-fluid p-0",
    style={"position": "relativ"}
)

