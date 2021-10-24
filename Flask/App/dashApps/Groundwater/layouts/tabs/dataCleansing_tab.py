import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.layouts.bodies import *


# -----------------------------------------------------------------------------
# DATA CLEANSING TAB
# -----------------------------------------------------------------------------

DATA_CLEANSING_TAB = html.Div(
    className='container-fluid',
    children=[
        
        html.Div(
            className='row mx-2 mt-2 mb-0 p-2 border border-dark',
            children=CONTROLS___DATA_CLEANSING_TAB
        ),
        
        html.Div(
            className='row mx-2 mt-0 mb-0',
            style={
                "height": "450px",
            },
            children=GRAPH_MAP___DATA_CLEANSING_TAB
        ),
        
        html.Div(
            className='row mx-2 mt-0 mb-2 pt-5 border border-top-0 border-dark d-flex justify-content-center',
            style={
                "height": "300px",
            },
            children=TABLE___DATA_CLEANSING_TAB
        ),
        
        html.Div(
            className='row m-2 p-2 d-flex justify-content-center',
            children=BUTTONS___DATA_CLEANSING_TAB
        ),
        
        dcc.Store(
            id='DATABASE_STATE___DATA_CLEANSING_TAB',
            storage_type='memory'            
        ),
        
        dcc.Store(
            id='DATA_STORE___DATA_CLEANSING_TAB',
            storage_type='memory'
        ),
        
        dcc.Interval(
            id='LOAD_DATABASE___DATA_CLEANSING_TAB',
            interval=1 * 1000,
            n_intervals=0,
            max_intervals=2
        )
        
    ]
)