import dash_html_components as html
import dash_dangerously_set_inner_html
from App.dashApps.Groundwater.layouts.tabs import *


# -----------------------------------------------------------------------------
# Tab Pan
# -----------------------------------------------------------------------------

TAB_PAN = html.Div(
    children=[

        # Nav Tabs ------------------------------------------------------------

        dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
            """
                    <ul class="nav nav-tabs mt-1" role="tablist">
                        <li class="nav-item tab-width">
                            <a class="nav-link active" data-toggle="tab" href="#Home">خانه</a>
                        </li>
                        <li class="nav-item tab-width">
                            <a class="nav-link" data-toggle="tab" href="#Tab_1">چاه مشاهده‌ای</a>
                        </li>
                        <li class="nav-item tab-width">
                            <a class="nav-link" data-toggle="tab" href="#Tab_2">انتخابی کمی</a>
                        </li>
                        <li class="nav-item tab-width">
                            <a class="nav-link" data-toggle="tab" href="#Tab_3">انتخابی کیفی</a>
                        </li>
                    </ul>
            """
        ),

        # Tab Panes -----------------------------------------------------------

        html.Div(
            children=[
                html.Div(
                    children=[
                        HOME
                    ],
                    className="tab-pane active",
                    id="Home"
                ),
                html.Div(
                    children=[
                        TAB_1
                    ],
                    className="tab-pane",
                    id="Tab_1"
                ),
                html.Div(
                    children=[
                        TAB_2
                    ],
                    className="tab-pane fade",
                    id="Tab_2"
                ),
                html.Div(
                    children=[
                        TAB_3
                    ],
                    className="tab-pane fade",
                    id="Tab_3"
                ),
            ],
            className="tab-content"
        )
    ],
    className="tabbable"
)


# -----------------------------------------------------------------------------
# Main Layout
# -----------------------------------------------------------------------------

def MAIN_LAYOUT():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        children=[
                            TAB_PAN
                        ],
                        className="col m-0 p-0"
                    )
                ],
                className="row m-0 p-0"
            )
        ],
        className="container-fluid m-0 p-0"
    )
