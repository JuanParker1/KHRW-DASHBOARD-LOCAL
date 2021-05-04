import dash
import dash_bootstrap_components as dbc

from App.dashApp.aquifer_hydrograph.layouts.main import main_layout

from App import app

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

myAppAQ = dash.Dash(
    name="myAppAQ",
    url_base_pathname="/myAppAQ/",
    server=app,
    external_stylesheets=[dbc.themes.BOOTSTRAP, external_stylesheets]
)

myAppAQ.layout = main_layout

from App.dashApp.aquifer_hydrograph.callbacks.main import *


def create_myAppAQ():
    return myAppAQ
