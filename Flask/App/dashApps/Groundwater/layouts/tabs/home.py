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


HOME = html.Div(
    children=[

        # Store State Sidebar ---------
        dcc.Store(
            id="SIDEBAR_STATE-TAB_HOME",
            data="HIDDEN"
        ),

        dcc.Store(
            id="MAP_ITEM-TAB_HOME_BODY",
        ),

        dcc.Interval(
            id='INTERVAL_COMPONENT-TAB_HOME_BODY',
            interval=1 * 1000,
            n_intervals=0,
            max_intervals=5
        ),

        # Sidebar ---------------------
        SIDEBAR_TAB_HOME,

        # Body ------------------------
        BODY_TAB_HOME        

    ],
    className="container-fluid p-0 m-0"
)
