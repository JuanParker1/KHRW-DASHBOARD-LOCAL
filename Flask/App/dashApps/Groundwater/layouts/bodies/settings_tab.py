import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.callbacks.config import *

# -------------------------------------------------------------------------------------------------
# TAB SETTINGS - BODY
# -------------------------------------------------------------------------------------------------


BODY_TAB_SETTINGS = html.Div(
    children=[
        html.Div(
            children=[
                ''
            ],
            className='col-4 p-0 m-0 bg-danger',
        ),
        html.Div(
            children=[
                ''
            ],
            className='col-8 p-0 m-0 bg-dark',
        )
    ],
    dir='rtl',
    className='row p-0 m-0',
    style={
        'height': '95vh',
        'width ': '100vw'
    }
)

