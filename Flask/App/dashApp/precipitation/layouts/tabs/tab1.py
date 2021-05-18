import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from layouts.headers.header import *
from layouts.sidebars.sidebar import *
from layouts.bodies.body import *
from layouts.footers.footer import *


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
                        TAB_1_HEADER
                    ],
                    className="col"
                )
            ],
            className="row"
        ),
        # Sidebar & Body ------------------------------------------------------
        html.Div(
            children=[
                # Sidebar ---------------------------------
                html.Div(
                    children=[
                        TAB_1_SIDEBAR
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
                    className='my-body'
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
                    id="database",
                )
            ],
            style={
                'display': 'none'
            }
        )
    ],
    className="container-fluid p-0"
)
