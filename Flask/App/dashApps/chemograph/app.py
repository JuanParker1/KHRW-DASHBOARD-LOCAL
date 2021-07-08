import dash
from flask_login.utils import login_required

from App.dashApp.chemograph.callbacks.database_config import *
from App.dashApp.chemograph.layouts.main import MAIN_LAYOUT
from App.dashApp.chemograph.callbacks.callback import chemograph_callback


BOOTSTRAP_CSS = "/static/chemograph/css/bootstrap-4.5.2.min.css"
MAIN_CSS = "/static/chemograph/css/main.css"
JQUERY_JS = "/static/chemograph/js/jquery-3.6.0.min.js"
BOOTSTRAP_JS = "/static/chemograph/js/bootstrap-4.5.2.min.js"
POPPER_JS = "/static/chemograph/js/popper.min.js"
FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)


def create_chemograph_app(server):
    chemograph_app = dash.Dash(
        name="chemograph",
        server=server,
        url_base_pathname="/chemograph/",
        external_stylesheets=[FONT_AWESOME, BOOTSTRAP_CSS, MAIN_CSS],
        external_scripts=[JQUERY_JS, POPPER_JS, BOOTSTRAP_JS],
        title='Chemograph Analysis'
    )
    
    chemograph_app.layout = MAIN_LAYOUT
    
    chemograph_callback(app=chemograph_app)

    for view_function in chemograph_app.server.view_functions:
        if view_function.startswith(chemograph_app.config.url_base_pathname):
            chemograph_app.server.view_functions[view_function] = login_required(
                chemograph_app.server.view_functions[view_function])

    return chemograph_app
