import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.layouts.headers.header import *
from App.dashApps.Groundwater.layouts.sidebars.sidebar import *
from App.dashApps.Groundwater.layouts.bodies.body import *
from App.dashApps.Groundwater.layouts.footers.footer import *


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
                    className='left-sidebar'
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
                    className='tab2-right-sidebar-hidden-my-body pt-2'
                ),
                # Sidebar right ---------------------------
                html.Div(
                    id="TAB_2_SIDEBAR_RIGHT",
                    hidden=True,
                    children=[
                        TAB_2_SIDEBAR_RIGHT
                    ],
                    className='tab2-right-sidebar-hidden'
                ),
            ],
            className="row p-0 m-0 w-100"
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

