import dash
import pandas as pd
from flask_login.utils import login_required


from App.dashApp.isotope_analysis.layouts.main import MAIN_LAYOUT
from App.dashApp.isotope_analysis.callbacks.callback import isotope_analysis_callback


BOOTSTRAP_CSS = "/static/isotope_analysis/css/bootstrap-4.5.2.min.css"
MAIN_CSS = "/static/isotope_analysis/css/main.css"
JQUERY_JS = "/static/isotope_analysis/js/jquery-3.6.0.min.js"
BOOTSTRAP_JS = "/static/isotope_analysis/js/bootstrap-4.5.2.min.js"
POPPER_JS = "/static/isotope_analysis/js/popper.min.js"


def create_isotope_analysis_app(server):
    isotope_analysis_app = dash.Dash(
        name="isotope_analysis",
        server=server,
        url_base_pathname="/isotope_analysis/",
        external_stylesheets=[MAIN_CSS, BOOTSTRAP_CSS],
        external_scripts=[JQUERY_JS, POPPER_JS, BOOTSTRAP_JS],
        title='Isotope Analysis'
    )
    
    isotope_analysis_app.layout = MAIN_LAYOUT
    
    
    isotope_analysis_callback(app=isotope_analysis_app)

    for view_function in isotope_analysis_app.server.view_functions:
        if view_function.startswith(isotope_analysis_app.config.url_base_pathname):
            isotope_analysis_app.server.view_functions[view_function] = login_required(
                isotope_analysis_app.server.view_functions[view_function])

    return isotope_analysis_app
