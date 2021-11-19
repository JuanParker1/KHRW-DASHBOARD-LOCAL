import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.layouts.bodies import *
from App.dashApps.Groundwater.layouts.sidebars import *


# -----------------------------------------------------------------------------
# MISSING DATA TAB
# -----------------------------------------------------------------------------

MISSING_DATA_TAB = html.Div(
    className="m-0 p-0",
    children=[
        html.Div(
            className='row m-0 p-0',
            # style={
            #     "height": "95vh"
            # },
            children=[
                html.Div(
                    className='col-3 m-0 p-3 bg-light',
                    # style={
                    #     "height": "95vh"
                    # },
                    children=[
                        SIDEBAR___MISSING_DATA_TAB
                    ]
                ),
                html.Div(
                    className='col-9 m-0 p-0',
                    # style={
                    #     "height": "95vh"
                    # },
                    children=[
                        BODY___MISSING_DATA_TAB
                    ]
                )
            ]
        ),
        dcc.Store(
            id='DATABASE_STATE___MISSING_DATA_TAB',
            storage_type='memory'            
        ),        
        dcc.Store(
            id='DATA_STORE___MISSING_DATA_TAB',
            storage_type='memory'
        ),        
        dcc.Interval(
            id='LOAD_DATABASE___MISSING_DATA_TAB',
            interval=1 * 1000,
            n_intervals=0,
            max_intervals=2
        ) 
    ]
)