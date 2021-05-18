import dash
import dash_bootstrap_components as dbc


BOOTSTRAP_CSS = "./assets/css/bootstrap.min.css"
MAIN_CSS = "./assets/css/main.css"
BOOTSTRAP_JS = "./assets/js/bootstrap-4.5.2.min.js"
JQUERY_JS = "./assets/js/jquery-3.6.0.min.js"
POPPER_JS = "./assets/js/popper-2.9.1.min.js"


app = dash.Dash(
    name=__name__,
    external_stylesheets=[MAIN_CSS, BOOTSTRAP_CSS],
    external_scripts=[BOOTSTRAP_JS, JQUERY_JS, POPPER_JS]
)
