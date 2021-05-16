import dash
from flask_login.utils import login_required

from App.dashApp.hydrograph.layouts.main import MAIN_LAYOUT
from App.dashApp.hydrograph.callbacks.callback import hydrograph_callback


BOOTSTRAP_CSS = "/static/hydrograph/css/bootstrap-4.5.2.min.css"
MAIN_CSS = "/static/hydrograph/css/main.css"
JQUERY_JS = "/static/hydrograph/js/jquery-3.6.0.min.js"
BOOTSTRAP_JS = "/static/hydrograph/js/bootstrap-4.5.2.min.js"
POPPER_JS = "/static/hydrograph/js/popper.min.js"
FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)


def create_hydrograph_app(server):
    hydrograph_app = dash.Dash(
        name="hydrograph",
        server=server,
        url_base_pathname="/hydrograph/",
        external_stylesheets=[FONT_AWESOME, BOOTSTRAP_CSS, MAIN_CSS],
        external_scripts=[JQUERY_JS, POPPER_JS, BOOTSTRAP_JS],
        title='Hydrograph Analysis'
    )
    
    hydrograph_app.layout = MAIN_LAYOUT
    
    hydrograph_callback(app=hydrograph_app)

    for view_function in hydrograph_app.server.view_functions:
        if view_function.startswith(hydrograph_app.config.url_base_pathname):
            hydrograph_app.server.view_functions[view_function] = login_required(
                hydrograph_app.server.view_functions[view_function])

    return hydrograph_app
