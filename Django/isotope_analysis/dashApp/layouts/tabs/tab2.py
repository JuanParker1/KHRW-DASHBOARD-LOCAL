import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from isotope_analysis.dashApp.layouts.headers.header import *
from isotope_analysis.dashApp.layouts.sidebars.sidebar import *
from isotope_analysis.dashApp.layouts.bodies.body import *
from isotope_analysis.dashApp.layouts.footers.footer import *


# -----------------------------------------------------------------------------
# Tab 2
# -----------------------------------------------------------------------------


TAB_2 = html.Div(
    children=[
        "TAB_2"
    ],
    className="container-fluid p-0"
)
