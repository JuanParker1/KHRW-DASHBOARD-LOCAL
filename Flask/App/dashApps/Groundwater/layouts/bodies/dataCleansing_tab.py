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
# CONTROLS
# -------------------------------------

# STUDY AREA:
STUDY_AREA_CARD___CONTROLS___DATA_CLEANSING_TAB = [
    html.Div(
        className='form-group text-center', 
        children=[
            html.Label(
                dir='rtl', 
                children='محدوده مطالعاتی'
            ),
            dcc.Dropdown(
                id='STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
                multi=True,
                placeholder='انتخاب ...'
            ) 
        ]
    )
]

# AQUIFER:
AQUIFER_CARD___CONTROLS___DATA_CLEANSING_TAB = [
    html.Div(
        className='form-group text-center', 
        children=[
            html.Label(
                className='text-center',
                dir='rtl', 
                children='آبخوان'
            ),
            dcc.Dropdown(
                id='AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
                multi=True,
                placeholder='انتخاب ...'
            ) 
        ]
    )
]

# WELL:
WELL_CARD___CONTROLS___DATA_CLEANSING_TAB = [
    html.Div(
        className='form-group text-center', 
        children=[
            html.Label(
                className='text-center',
                dir='rtl', 
                children='چاه مشاهده‌ای'
            ),
            dcc.Dropdown(
                id='WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
                multi=True,
                placeholder='انتخاب ...'
            ) 
        ]
    )
]

# METHOD 1:
METHOD_1_CARD___CONTROLS___DATA_CLEANSING_TAB = [
    html.Div(
        className='form-group text-center', 
        children=[
            html.Label(
                className='text-center',
                dir='rtl', 
                children='روش میانگین'
            ),
            dcc.Dropdown(
                id='METHOD_1_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
                placeholder='انتخاب ...',
                value=2,
                options=[{"label": f"{x}x", "value": x} for x in [i for i in range(1, 11)]]
            ) 
        ]
    )
]

# METHOD 2:
METHOD_2_CARD___CONTROLS___DATA_CLEANSING_TAB = [
    html.Div(
        className='form-group text-center', 
        children=[
            html.Label(
                className='text-center',
                dir='rtl', 
                children='روش مشتق'
            ),
            dcc.Dropdown(
                id='METHOD_2_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
                placeholder='انتخاب ...',
                value=2,
                options=[{"label": f"{x}%", "value": x} for x in [i for i in range(1, 11)]]
            ) 
        ]
    ),
]

# CONTROLS ----------------------------
CONTROLS___DATA_CLEANSING_TAB = [
    html.Div(
        className='col-2',
        children=STUDY_AREA_CARD___CONTROLS___DATA_CLEANSING_TAB
    ),
    html.Div(
        className='col-2',
        children=AQUIFER_CARD___CONTROLS___DATA_CLEANSING_TAB
    ),
    html.Div(
        className='col-4',
        children=WELL_CARD___CONTROLS___DATA_CLEANSING_TAB
    ),
    html.Div(
        className='col-2',
        children=METHOD_1_CARD___CONTROLS___DATA_CLEANSING_TAB
    ),
    html.Div(
        className='col-2',
        children=METHOD_2_CARD___CONTROLS___DATA_CLEANSING_TAB
    )
]



# -------------------------------------
# GRAPH & MAP
# -------------------------------------

# MAP
MAP___GRAPH_MAP___DATA_CLEANSING_TAB = [
    dcc.Graph(
        id='MAP___GRAPH_MAP___DATA_CLEANSING_TAB',
        className="w-100 h-100" 
    )    
]

# GRAPH
GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB = [
    dcc.Graph(
        id='GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB',
        className="w-100 h-100"
    )
]


# GRAPH & MAP -------------------------
GRAPH_MAP___DATA_CLEANSING_TAB = [
    html.Div(
        className='col-3 m-0 p-0 border border-top-0 border-dark',
        children=MAP___GRAPH_MAP___DATA_CLEANSING_TAB
    ),
    html.Div(
        className='col-9 m-0 p-0 border border-top-0 border-right-0 border-dark',
        children=GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB
    )
]



# -------------------------------------
# TABLE
# -------------------------------------

TABLE___DATA_CLEANSING_TAB = dash_table.DataTable(
    id="TABLE___DATA_CLEANSING_TAB",
    editable=True,
    style_cell={
        'border': '1px solid grey',
        'font-size': '14px',
        'text_align': 'center'
    },
)



# -------------------------------------
# BUTTONS
# -------------------------------------

# BUTTON:
BUTTON___BUTTONS___DATA_CLEANSING_TAB = dbc.Button(
    id='BUTTON___BUTTONS___DATA_CLEANSING_TAB',
    className="me-1",
    size="lg",
    children='بروزرسانی پایگاه داده', 
    color='primary',
    n_clicks=0
)

# TOAST:
TOAST___BUTTONS___DATA_CLEANSING_TAB = dbc.Toast(
    id='TOAST___BUTTONS___DATA_CLEANSING_TAB',
    is_open=False,
    dismissable=True,
    duration=5000
)


# BUTTONS -----------------------------
BUTTONS___DATA_CLEANSING_TAB = [
    BUTTON___BUTTONS___DATA_CLEANSING_TAB,
    TOAST___BUTTONS___DATA_CLEANSING_TAB,
]