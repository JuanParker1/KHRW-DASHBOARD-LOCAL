import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.layouts.sidebars import *
from App.dashApps.Groundwater.layouts.bodies import *


# -----------------------------------------------------------------------------
# Tab 1
# -----------------------------------------------------------------------------


HOME_TAB = html.Div(
    children=[

        # Sidebar ---------------------
        SIDEBAR_TAB_HOME,

        # Body ------------------------
        BODY_TAB_HOME,

        # Store State Sidebar ---------
        dcc.Store(
            id="SIDEBAR_STATE-TAB_HOME",
            data="HIDDEN"
        ),

        dcc.Store(
            id="MAP_ITEM-TAB_HOME_BODY",
        ),

        dcc.Store(
            id="RAW_DATA-TAB_HOME_BODY",
        ),
        
        dcc.Store(
            id="DUMMY_COMPONENT-TAB_HOME_BODY",
            data="OK"
        ),
        
        dcc.Interval(
            id='INTERVAL_COMPONENT_DATA_CLEANSING-TAB_HOME_BODY',
            interval=1 * 1000,
            n_intervals=0,
            max_intervals=2
        ), 

        dcc.Interval(
            id='INTERVAL_COMPONENT-TAB_HOME_BODY',
            interval=1 * 1000,
            n_intervals=0,
            max_intervals=2
        ),     

    ],
    className="container-fluid p-0 m-0"
)
