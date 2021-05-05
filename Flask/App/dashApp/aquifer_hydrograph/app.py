import dash
import dash_bootstrap_components as dbc
from flask_login.utils import login_required

from App.dashApp.aquifer_hydrograph.layouts.main import MAIN_LAYOUT
from App.dashApp.aquifer_hydrograph.callbacks.callback import aquifer_hydrograph_callback


MAIN_CSS = "/static/aquifer_hydrograph/css/main.css"

def create_aquifer_hydrograph_app(server):
    aquifer_hydrograph_app = dash.Dash(
        name="aquifer_hydrograph",
        server=server,
        url_base_pathname="/aquifer_hydrograph/",
        external_stylesheets=[dbc.themes.BOOTSTRAP, MAIN_CSS],
        title='Aquifer Hydrograph Analysis'
    )

    aquifer_hydrograph_app.layout = MAIN_LAYOUT
    
    
    aquifer_hydrograph_callback(app=aquifer_hydrograph_app)

    for view_function in aquifer_hydrograph_app.server.view_functions:
        if view_function.startswith(aquifer_hydrograph_app.config.url_base_pathname):
            aquifer_hydrograph_app.server.view_functions[view_function] = login_required(
                aquifer_hydrograph_app.server.view_functions[view_function])

    return aquifer_hydrograph_app
