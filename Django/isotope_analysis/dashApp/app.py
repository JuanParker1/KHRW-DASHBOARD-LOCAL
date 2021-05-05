import dash
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash

from aquifer_hydrograph.dashApp.layouts.main import main_layout
from isotope_analysis.dashApp.layouts.main import MAIN_LAYOUT

BOOTSTRAP_CSS = "assets/isotope_analysis/css/bootstrap-4.5.2.min.css"
MAIN_CSS = "assets/isotope_analysis/css/main.css"
BOOTSTRAP_JS = "assets/isotope_analysis/js/bootstrap-4.5.2.min.js"
JQUERY_JS = "assets/isotope_analysis/js/jquery-3.6.0.min.js"
POPPER_JS = "assets/isotope_analysis/js/popper-2.9.1.min.js"

app = DjangoDash(
    'Isotope_Analysis_App',
    external_stylesheets=[BOOTSTRAP_CSS, MAIN_CSS],
    external_scripts=[JQUERY_JS, POPPER_JS, BOOTSTRAP_JS],
    add_bootstrap_links=True
)

app.layout = MAIN_LAYOUT

from isotope_analysis.dashApp.callbacks.callbacks import *
