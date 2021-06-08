import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApp.precipitation.layouts.headers.header import *
from App.dashApp.precipitation.layouts.sidebars.sidebar import *
from App.dashApp.precipitation.layouts.bodies.body import *
from App.dashApp.precipitation.layouts.footers.footer import *


# -----------------------------------------------------------------------------
# Tab 2
# -----------------------------------------------------------------------------


TAB_2 = html.Div(
    children=[
        # Header --------------------------------------------------------------
        html.Div(
            children=[
                html.Div(
                    children=[
                        # TAB_2_HEADER
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
                        TAB_2_SIDEBAR_LEFT
                    ],
                    className="col-lg-3 col-xl-2 px-1 bg-light"
                ),
                # Body ------------------------------------
                html.Div(
                    id="TAB_2_BODY",
                    children=[
                        html.Div(
                            children=TAB_2_BODY,
                            className="container-fluid"
                        )
                    ],
                    className="col-lg-9 col-xl-10 px-2"
                ),
            ],
            className="row justify-content-between p-0 m-0 w-100"
        ),
        # Footer --------------------------------------------------------------
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB_2_FOOTER
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

