import base64
import numpy as np
from datetime import date
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_table

from layouts.visualizations.visualization import *


# -----------------------------------------------------------------------------
# TAB 2 - BODY
# -----------------------------------------------------------------------------


TAB_2_BODY = [
    # html.Div(
    #     children=[
    #         # Graph
    #         TAB2_BODY_CARDINFO
    #     ],
    #     className="row justify-content-center",
    # ),
    html.Div(
        children=[
            # Graph
            TAB2_BODY_CONTENT1
        ],
        className="row justify-content-center",
        style={
            "height": "670px",
            # "margin-bottom": "10px"
        }
    ),
    html.Div(
        children=[
            html.Div(
                children=[
                    # Table
                    TAB2_BODY_CONTENT2
                ],
                className="w-100 h-100 px-4"
            )

        ],
        className="row justify-content-center"
    )
]
