import dash
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash

from aquifer_hydrograph.dashApp.layouts.main import main_layout

MAIN_CSS = "assets/aquifer_hydrograph/css/main.css"


app = DjangoDash(
    'Aquifer_Hydrograph_App',
    external_stylesheets=[dbc.themes.BOOTSTRAP, MAIN_CSS],
    add_bootstrap_links=True
)

app.layout = main_layout

from aquifer_hydrograph.dashApp.callbacks.main import *
