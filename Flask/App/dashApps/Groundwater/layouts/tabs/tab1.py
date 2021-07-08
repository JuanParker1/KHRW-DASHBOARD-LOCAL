import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.layouts.headers.header import *
from App.dashApps.Groundwater.layouts.sidebars.sidebar import *
from App.dashApps.Groundwater.layouts.bodies.body import *
from App.dashApps.Groundwater.layouts.footers.footer import *


# -----------------------------------------------------------------------------
# Tab 1
# -----------------------------------------------------------------------------


TAB_1 = html.Div(
    children=[
        # Header --------------------------------------------------------------
        html.Div(
            children=[
                html.Div(
                    children=[
                        # TAB_1_HEADER
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
                        TAB_1_SIDEBAR_LEFT
                    ],
                    className='left-sidebar'
                ),
                # Body ------------------------------------
                html.Div(
                    children=[
                        html.Div(
                            children=TAB_1_BODY,
                            className="container-fluid"
                        )
                    ],
                    className='my-body pt-2'
                ),
                # Sidebar right ---------------------------
                html.Div(
                    children=[
                        TAB_1_SIDEBAR_RIGHT
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
                        TAB_1_FOOTER
                    ],
                    className="col"
                )
            ],
            className="row"
        ),
        # Hidden Div For Store Data--------------------------------------------
        html.Div(
            children=[
                html.Div(
                    id="TABLE_RAWDATA-TAB1_SIDEBAR",
                )
            ],
            style={
                'display': 'none'
            }
        )
    ],
    className="container-fluid p-0",
    style={"position": "relativ"}
)
