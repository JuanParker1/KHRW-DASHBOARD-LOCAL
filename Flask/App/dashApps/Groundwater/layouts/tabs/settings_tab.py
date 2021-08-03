import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.layouts.sidebars import *
from App.dashApps.Groundwater.layouts.bodies import *


# -----------------------------------------------------------------------------
# Tab 1
# -----------------------------------------------------------------------------


SETTINGS_TAB = html.Div(
    children=[

        # Body ------------------------
        BODY_TAB_SETTINGS,   

    ],
    className="container-fluid p-0 m-0"
)
