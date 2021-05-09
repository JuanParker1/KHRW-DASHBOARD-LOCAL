import dash
import dash_bootstrap_components as dbc



FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)


BOOTSTRAP_CSS = "./assets/css/bootstrap.min.css"
MAIN_CSS = "./assets/css/main.css"
# FONT_AWESOME = "./assets/css/font-awesome.min.css"
BOOTSTRAP_JS = "./assets/js/bootstrap-4.5.2.min.js"
JQUERY_JS = "./assets/js/jquery-3.6.0.min.js"
POPPER_JS = "./assets/js/popper-2.9.1.min.js"


app = dash.Dash(
    name=__name__,
    external_stylesheets=[FONT_AWESOME, MAIN_CSS, BOOTSTRAP_CSS],
    external_scripts=[BOOTSTRAP_JS, JQUERY_JS, POPPER_JS]
)
