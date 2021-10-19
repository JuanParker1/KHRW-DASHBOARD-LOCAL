import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.layouts.sidebars import *
from App.dashApps.Groundwater.layouts.bodies import *


# -----------------------------------------------------------------------------
# Tab 2
# -----------------------------------------------------------------------------


DATA_CLEANSING_TAB = html.Div(
    children=[
        html.Div(
            children=[
                DATA_CLEANSING_TAB_SIDEBAR
            ],
            className='container-fluid'
        ),
        html.Div(
            children=[
                DATA_CLEANSING_TAB_BODY
            ],
            className="container-fluid"
        ),
        dcc.Interval(
            id='INTERVAL_COMPONENT-DATA_CLEANSING_TAB',
            interval=1 * 1000,
            n_intervals=0,
            max_intervals=2
        ),
        html.Div(
            children=[
                html.Div(
                    id="DATABASE_STATE-DATA_CLEANSING_TAB",
                )
            ],
            style={
                'display': 'none'
            }
        )
    ],
    className="container-fluid"
)

