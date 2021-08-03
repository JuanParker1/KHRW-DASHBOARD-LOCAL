import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.layouts.sidebars import *
from App.dashApps.Groundwater.layouts.bodies import *


# -----------------------------------------------------------------------------
# Tab 1
# -----------------------------------------------------------------------------


TAB_1 = html.Div(
    children=[
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
