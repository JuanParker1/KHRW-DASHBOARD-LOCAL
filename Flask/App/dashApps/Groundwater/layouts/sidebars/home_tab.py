import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.callbacks.config import *

# -------------------------------------------------------------------------------------------------
# SIDEBAR - TAB HOME
# -------------------------------------------------------------------------------------------------

COLLAPSE_BASE_MAP = html.Div(
    children=[
        html.H6(
            children=[
                html.I(
                    className="fas fa-caret-left ml-2",
                    id="ARROW-TAB_HOME_SIDEBAR_COLLAPSE_BASE_MAP"
                ),
                "نقشه‌های اصلی",
          
            ],
            id="OPEN_CLOSE-TAB_HOME_SIDEBAR_COLLAPSE_BASE_MAP",
            n_clicks=0,
            className="inline COLLAPSE-CARD-HEADER"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(STREETS),
                                    className="m-1"
                                ),
                                html.P(
                                    "Streets",
                                    className="card-title text-center m-0 fs-small"
                                )
                            ],
                            id="STREETS_BASE_MAP-TAB_HOME_BODY",
                            className="THUMBNAIL card", 
                            style=BASE_MAP_SELECTED_STYLE
                        ),
                        html.Div(
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(IMAGERY),
                                    className="m-1"
                                ),
                                html.P(
                                    "Imagery",
                                    className="card-title text-center m-0 fs-small"
                                )
                            ],
                            id="IMAGERY_BASE_MAP-TAB_HOME_BODY",
                            className="THUMBNAIL card "
                        ),
                        html.Div(
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(TOPOGRAPHIC),
                                    className="m-1"
                                ),
                                html.P(
                                    "Topographic",
                                    className="card-title text-center m-0 fs-small"
                                )
                            ],
                            id="TOPOGRAPHIC_BASE_MAP-TAB_HOME_BODY",
                            className="THUMBNAIL card"
                        )
                    ],
                    className="card-group mx-1 pt-1"
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(NONEBASEMAP),
                                    className="m-1"
                                ),
                                html.P(
                                    "None",
                                    className="card-title text-center m-0 fs-small"
                                )
                            ],
                            id="NONEBASEMAP_BASE_MAP-TAB_HOME_BODY",
                            className="THUMBNAIL card",
                        ),
                        html.Div(
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(DARK),
                                    className="m-1"
                                ),
                                html.P(
                                    "Dark",
                                    className="card-title text-center m-0 fs-small"
                                )
                            ],
                            id="DARK_BASE_MAP-TAB_HOME_BODY",
                            className="THUMBNAIL card",
                        ),
                        html.Div(
                            children=[
                                html.Img(
                                    src='data:image/png;base64,{}'.format(TERRAIN),
                                    className="m-1"
                                ),
                                html.P(
                                    "Terrain",
                                    className="card-title text-center m-0 fs-small"
                                )
                            ],
                            id="TERRAIN_BASE_MAP-TAB_HOME_BODY",
                            className="THUMBNAIL card"
                        )
                    ],
                    className="card-group mx-1 pb-1"
                ),
                html.Div(
                    children=[
                        html.Div(
                            "شفافیت:",
                            className="fs-small col-2 m-0 p-0"
                        ),
                        html.Div(
                            dcc.Slider(
                                id='OPACITY_BASE_MAP-TAB_HOME_SIDEBAR',
                                updatemode='drag',
                                min=0,
                                max=100,
                                step=5,
                                value=100,
                                marks={
                                    0: {'label': '0%', 'style': {'font-size': 'small'}},
                                    100: {'label': '100%', 'style': {'font-size': 'small'}}
                                },
                                className="p-0 m-0 mx-3"
                            ),
                            className="col-8 m-0 p-0"
                        ),
                        html.Div(
                            dbc.Badge(
                                id="BADGE_OPACITY_BASE_MAP-TAB_HOME_SIDEBAR",
                                children="100%",
                                color="primary",
                                className="w-100"
                            ),
                            className="col-2 m-0 p-0"
                        ),                        
                    ],
                    className="row my-0 mx-1 d-flex justify-content-around px-4 pb-4 pt-3"
                )
            ],
            id="COLLAPSE_BODY-TAB_HOME_SIDEBAR_COLLAPSE_BASE_MAP",
            is_open=False,
            style={"background-color": "#e9e9e9"}
        )
    ],
    className="COLLAPSE-CARD"
)



COLLAPSE_POLITICAL_MAP = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP"
                        ),
                       "مرزهای سیاسی",
                    ]            
                ),
                dbc.Badge(
                    0, 
                    color="primary", 
                    className="m-0 p-2",
                    id="NUMBER_SELECTED_POLITICAL_MAP-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP")         
            ],
            id="OPEN_CLOSE-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP",
            n_clicks=0,
            className="inline COLLAPSE-CARD-HEADER",
            style={
                'display': 'flex',
                'justify-content': 'space-between'
            }
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                dcc.Checklist(
                                    options=[
                                        {'label': 'کشور', 'value': 'COUNTRY'},
                                        {'label': 'استان', 'value': 'PROVINCE'},
                                        {'label': 'شهرستان', 'value': 'COUNTY'},
                                        {'label': 'بخش', 'value': 'DISTRICT'}
                                    ],
                                    id="ADD_POLITICAL_MAP-TAB_HOME_SIDEBAR",
                                    labelClassName  ="list-group-item p-0 m-0 py-2",
                                    inputClassName="mx-2"
                                )
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card"
                )
            ],
            id="COLLAPSE_BODY-TAB_HOME_SIDEBAR_COLLAPSE_POLITICAL_MAP",
            is_open=False,
        )
    ],
    className="COLLAPSE-CARD"
)



COLLAPSE_WATER_MAP = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP"
                        ),
                        "مرزهای آبی",
                    ]            
                ),
                dbc.Badge(
                    0, 
                    color="primary", 
                    className="m-0 p-2",
                    id="NUMBER_SELECTED_WATER_MAP-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP"
                )         
            ],
            id="OPEN_CLOSE-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP",
            n_clicks=0,
            className="inline COLLAPSE-CARD-HEADER",
            style={
                'display': 'flex',
                'justify-content': 'space-between'
            }
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                dcc.Checklist(
                                    options=[
                                        {'label': 'حوضه‌های درجه یک', 'value': 'BASIN1'},
                                        {'label': 'حوضه‌های درجه دو', 'value': 'BASIN2'},
                                        {'label': 'محدوده‌های مطالعاتی', 'value': 'MAHDOUDE'},
                                        {'label': 'آبخوان‌ها', 'value': 'AQUIFER'},
                                    ],
                                    value=["MAHDOUDE"],
                                    id="ADD_WATER_MAP-TAB_HOME_SIDEBAR",
                                    labelClassName  ="list-group-item p-0 m-0 py-2",
                                    inputClassName="mx-2"
                                )
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card"
                )
            ],
            id="COLLAPSE_BODY-TAB_HOME_SIDEBAR_COLLAPSE_WATER_MAP",
            is_open=False,
        )
    ],
    className="COLLAPSE-CARD"
)



# SIDEBAR - TAB HOME
# ------------------------------------------------------------------------

SIDEBAR_TAB_HOME = html.Div(

    children=[
        COLLAPSE_BASE_MAP,
        COLLAPSE_POLITICAL_MAP,
        COLLAPSE_WATER_MAP
    ],
    id="SIDEBAR-TAB_HOME",
    className="SIDEBAR-HIDEN"
)