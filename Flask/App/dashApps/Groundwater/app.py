import dash
from flask_login.utils import login_required

from App.dashApps.Groundwater.layouts.main import MAIN_LAYOUT
from App.dashApps.Groundwater.callbacks.callback import groundwater_callback


# EXTERNAL STYLESHEETS
external_stylesheets=[
    "/static/vendor/fontawesome/v5.15.3/css/all.css",
    "/static/vendor/bootstrap/v4.6.0/css/bootstrap.min.css",
    "/static/vendor/animate/v4.1.1/animate.min.css",
    "/static/css/style.css",
]


# EXTERNAL SCRIPTS
external_scripts=[
    "/static/vendor/jquery/v3.6.0/jquery.min.js",
    "/static/vendor/popper/v2.9.2/popper.min.js",
    "/static/vendor/bootstrap/v4.6.0/js/bootstrap.min.js",
]


def create_groundwater_app(server):
    groundwater_app = dash.Dash(
        name="groundwater",
        server=server,
        url_base_pathname="/data-analysis/groundwater/",
        external_stylesheets=external_stylesheets,
        external_scripts=external_scripts,
        title='آب زیرزمینی',
        prevent_initial_callbacks=True
    )
    
    groundwater_app.layout = MAIN_LAYOUT
    
    groundwater_callback(app=groundwater_app)

    for view_function in groundwater_app.server.view_functions:
        if view_function.startswith(groundwater_app.config.url_base_pathname):
            groundwater_app.server.view_functions[view_function] = login_required(
                groundwater_app.server.view_functions[view_function]
            )

    return groundwater_app
