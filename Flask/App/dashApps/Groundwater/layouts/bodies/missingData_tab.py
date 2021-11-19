# -----------------------------------------------------------------------------
# MISSING DATA TAB - BODY
# -----------------------------------------------------------------------------



# -------------------------------------
# MODULES
# -------------------------------------

import base64
import numpy as np
from datetime import date
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_table



# -------------------------------------
# GRAPH
# -------------------------------------

GRAPH___MISSING_DATA_TAB = dcc.Graph(
    id='GRAPH___MISSING_DATA_TAB',
    className="w-100 h-100"
)



# -------------------------------------
# BODY
# -------------------------------------

BODY___MISSING_DATA_TAB = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        html.Div(
            className="row m-0 p-2",
            style={
                "height": "95vh"
            },
            children=[
                GRAPH___MISSING_DATA_TAB
            ]
        )
    ]
)