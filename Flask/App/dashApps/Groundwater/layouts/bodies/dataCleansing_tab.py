# -----------------------------------------------------------------------------
# DATA CLEANSING TAB - BODY
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
# MAP
# -------------------------------------

MAP___DATA_CLEANSING_TAB = dcc.Graph(
    id='MAP___GRAPH_MAP___DATA_CLEANSING_TAB',
    className="w-100 h-100" 
)



# -------------------------------------
# GRAPH
# -------------------------------------

GRAPH___DATA_CLEANSING_TAB = dcc.Graph(
    id='GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB',
    className="w-100 h-100"
)


# -------------------------------------
# TABLE
# -------------------------------------

TABLE___DATA_CLEANSING_TAB = dash_table.DataTable(
    id="TABLE___DATA_CLEANSING_TAB",
    editable=True,
    style_table={
        'overflowX': 'auto',
        'overflowY': 'auto',
        'maxHeight': '34vh'
    },
    style_cell={
        'border': '1px solid grey',
        'font-size': '12px',
        'text_align': 'center',
        # 'minWidth': 200,
        # 'maxWidth': 300,
    },
    style_header={
        # 'backgroundColor': 'rgb(220, 220, 220)',
        'border':'1px solid grey',
        'fontWeight': 'bold',
        'whiteSpace': 'normal',
        'text_align': 'center',
        'height': 'auto',
    }
)




# -------------------------------------
# BODY
# -------------------------------------

BODY___DATA_CLEANSING_TAB = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        html.Div(
            className="row m-0 p-2",
            style={
                "height": "60vh"
            },
            children=[
                GRAPH___DATA_CLEANSING_TAB
            ]
        ),
        html.Div(
            className="row m-0 p-0",
            style={
                "height": "35vh"
            },
            children=[
                html.Div(
                    id="TABLE_HOLDER___BODY___DATA_CLEANSING_TAB",
                    className="col-10 m-0 pl-0 pr-3 pt-0 pb-2",
                    hidden=True,
                    children=[
                        TABLE___DATA_CLEANSING_TAB
                    ]
                ),
                html.Div(
                    id="MAP_HOLDER___BODY___DATA_CLEANSING_TAB",
                    className="col-2 m-0 px-2 pt-0 pb-2",
                    children=[
                        MAP___DATA_CLEANSING_TAB
                    ]
                ),
            ]
        )
    ]
)