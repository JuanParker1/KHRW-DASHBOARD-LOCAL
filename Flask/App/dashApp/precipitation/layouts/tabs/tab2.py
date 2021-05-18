import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_html_components.Div import Div

from layouts.headers.header import *
from layouts.sidebars.sidebar import *
from layouts.bodies.body import *
from layouts.footers.footer import *


# -----------------------------------------------------------------------------
# Tab 2
# -----------------------------------------------------------------------------


TAB_2 = html.Div(
    children=[
        html.Div(
            children=[
                html.Iframe(
                    src="https://www.khrw.shirazipooya.ir",
                    className="iframe"
                ),
            ],
            className="banner"
        )
    ],
    className="container-fluid p-0"
)
