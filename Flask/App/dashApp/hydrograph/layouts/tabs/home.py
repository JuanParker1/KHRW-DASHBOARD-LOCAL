import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApp.hydrograph.layouts.headers.header import *
from App.dashApp.hydrograph.layouts.sidebars.sidebar import *
from App.dashApp.hydrograph.layouts.bodies.body import *
from App.dashApp.hydrograph.layouts.footers.footer import *


# -----------------------------------------------------------------------------
# Tab 1
# -----------------------------------------------------------------------------


HOME = html.Div(
    children=[

        # Collapse ----------------------------
        html.Div(
            children=[
                TAB_HOME_COLLAPSE
            ],
            className='row'
        ),

        # Body ------------------------------------
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB_HOME_BODY
                    ],
                    className="col-12 p-0 my-1"
                )
            ],
            className='row m-0'
        ),

        # Hidden Div For Store Data--------------------------------------------
        html.Div(
            children=[
                html.Div(
                    id="DATA-TAB_HOME",
                )
            ],
            style={
                'display': 'none'
            }
        )
    ],
    className="container-fluid p-0"
)
