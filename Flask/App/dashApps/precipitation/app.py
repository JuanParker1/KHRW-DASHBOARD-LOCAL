import dash
from flask_login.utils import login_required

from App.dashApp.precipitation.layouts.main import SERVER_MAIN_LAYOUT
from App.dashApp.precipitation.callbacks.callback import precipitation_callback


BOOTSTRAP_CSS = "/static/precipitation/css/bootstrap-4.5.2.min.css"
MAIN_CSS = "/static/precipitation/css/main.css"
JQUERY_JS = "/static/precipitation/js/jquery-3.6.0.min.js"
BOOTSTRAP_JS = "/static/precipitation/js/bootstrap-4.5.2.min.js"
POPPER_JS = "/static/precipitation/js/popper.min.js"
FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)


def create_precipitation_app(server):
    precipitation_app = dash.Dash(
        name="surfacewater",
        server=server,
        url_base_pathname="/surfacewater/",
        external_stylesheets=[FONT_AWESOME, BOOTSTRAP_CSS, MAIN_CSS],
        external_scripts=[JQUERY_JS, POPPER_JS, BOOTSTRAP_JS],
        title='آب سطحی'
    )

    precipitation_app.layout = SERVER_MAIN_LAYOUT

    precipitation_callback(app=precipitation_app)

    for view_function in precipitation_app.server.view_functions:
        if view_function.startswith(precipitation_app.config.url_base_pathname):
            precipitation_app.server.view_functions[view_function] = login_required(
                precipitation_app.server.view_functions[view_function])

    return precipitation_app
