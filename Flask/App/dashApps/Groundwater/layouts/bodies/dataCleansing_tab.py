import base64
import numpy as np
from datetime import date
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_table


# -----------------------------------------------------------------------------
# DATA CLEANSING TAB - BODY
# -----------------------------------------------------------------------------



GRAPH = dcc.Graph(
    id='GRAPH-DATA_CLEANSING_TAB-BODY',
    className="w-100 h-100"
)

TABLE = dash_table.DataTable(
    id='TABLE-DATA_CLEANSING_TAB-BODY',
    editable=True,
    filter_action="native",
    style_table={
        'overflowX': 'auto',
        'overflowY': 'auto',
    },
    style_cell={
        'whiteSoace': 'normal',
        'border': '1px solid grey',
        'font-size': '14px',
        'font_family': 'Tanha-FD',
        'text_align': 'center',
        'minWidth': 65,
        'maxWidth': 200,
        'width': 65,
        'height': 'auto'
    },
    style_header={
        'backgroundColor': 'rgb(220, 220, 220)',
        'fontWeight': 'bold',
        'whiteSpace': 'normal',
        'text_align': 'center',
        'height': 'auto',
    },
    css=[{
        'selector': '.dash-table-tooltip',
        'rule': 'background-color: yellow;'
    }],
    page_size=30
)





DATA_CLEANSING_TAB_BODY = html.Div(
    children=[
        html.Div(
            children=[
                GRAPH,
            ],
            className="row justify-content-center",
            style={
                "height": "500px",
            }
        ),
        html.Div(
            children=[
                TABLE,
            ],
            className="row justify-content-center pb-4",
        ),
        html.Button('Update', id='Update', n_clicks=0),
        html.Div(id='Placeholder', children=[]),
        dcc.Interval(id='Interval', interval=5000),
    ]
)




