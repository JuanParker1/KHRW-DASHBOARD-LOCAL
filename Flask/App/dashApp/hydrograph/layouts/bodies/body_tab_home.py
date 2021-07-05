import dash_leaflet as dl
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_leaflet.express as dlx
from dash_extensions.javascript import arrow_function
import geopandas as gpd


keys = {
    "One": {
        "url": "",
        "name": "None"
    },
    "Two": {
        "url": "https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png",
        "name": "Terrain"
    },
    "Three": {
        "url": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        "name": "Open Street Map"
    },
    "Four": {
        "url": "http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}",
        "name": "Google Satellite Imagery"
    },
}


attribution = '&copy; <a href="http://www.khrw.ir/">Khorasan Regional Water Company</a> '


# -----------------------------------------------------------------------------
# SHAPEFILES LOCATION
# -----------------------------------------------------------------------------
HOZEH6 = "./assets/Hozeh6.geojson"
HOZEH30 = "./assets/Hozeh30.geojson"
MAHDOUDE = "./assets/Mahdoude.geojson"
AQUIFERS = "./assets/Aquifers.geojson"

OSTAN = "./assets/Ostan.geojson"
SHAHRESTAN = "./assets/Shahrestan.geojson"
BAKHSH = "./assets/Bakhsh.geojson"



info = html.Div(
    id="info",
    className="info",
    style={
        "position": "absolute",
        "bottom": "10px",
        "left": "10px",
        "zIndex": "1000",
        "font-family": "Tanha-FD",
        "font-size": "small"
    },
    dir="rtl"
)

search_bar = html.Div(
    children=[
        dcc.RadioItems(
            options=[
                {'label': 'Lat/Lon', 'value': 'LatLon'},
                {'label': 'UTM', 'value': 'UTM'},
            ],
            id="select_coordinate",
            value='LatLon',
            labelStyle={'display': 'inline-block'},
            labelClassName="mx-1",
            className="text-left"
        ),
        dcc.Input(
            id="search_coordinate",
            placeholder="Lat: 36.30 Lon: 59.60",
            type="search",
            debounce=True,
            className="form-control"
        ),
        dbc.Tooltip(
            target="search_coordinate",
            autohide=True,
            placement="right",
            hide_arrow=True,
            delay={ "show": 0, "hide": 10 },
            children=[
                html.Div(
                    children=[
                        html.P(
                            "- سرچ براساس درجه:",
                            className="text-right my-0 py-0"
                        ),
                        html.P(
                            "به ترتیب عرض و طول جغرافیایی وارد شود، مانند:",
                            className="text-nowrap text-right my-0 py-0 mr-4"
                        ),
                        html.P(
                            "> 36.3 59.6",
                            className="text-left my-0 py-0",
                            dir="ltr"
                        ),
                        html.Hr(className="my-1 py-1"),
                        html.P(
                            "- سرچ براساس درجه/دقیقه/ثانیه:",
                            className="text-right my-0 py-0"
                        ),
                        html.P(
                            "به ترتیب عرض و طول جغرافیایی وارد شود، مانند:",
                            className="text-nowrap text-right my-0 py-0 mr-4"
                        ),
                        html.P(
                            "> 36 17 59 59 36 5",
                            className="text-left my-0 py-0",
                            dir="ltr"
                        ),
                        html.Hr(className="my-1 py-1"),
                        html.P(
                            "- سرچ براساس UTM:",
                            className="text-right my-0 py-0"
                        ),
                        html.P(
                            "به ترتیب زون، عرض و طول جغرافیایی وارد شود، مانند:",
                            className="text-nowrap text-right my-0 py-0 mr-4"
                        ),
                        html.P(
                            "> 40S 4020360 733465",
                            className="text-left my-0 py-0",
                            dir="ltr"
                        )
                    ],
                    dir="rtl"
                )
            ],
            style = {
                "maxWidth": "40rem",
                "width": "25rem"
            }
        ),
    ],
    style={
        "position": "absolute",
        "top": "10px",
        "left": "50px",
        "zIndex": "1000"
    },
    dir="ltr"
)

model1 = html.Div(
    children=[
        dbc.Modal(
            size="xl",
            id="modal",
            centered=True,
            is_open=False,
            children=[
                dbc.ModalHeader(
                    id="modal_header"
                ),
                dbc.ModalBody(
                    id="modal_body"
                )
            ]
        )
    ]
)

model2 = html.Div(
    children=[
        dbc.Modal(
            size="xl",
            id="modal2",
            centered=True,
            is_open=False,
            children=[
                dbc.ModalHeader(
                    id="modal2_header"
                ),
                dbc.ModalBody(
                    id="modal2_body"
                )
            ]
        )
    ]
)


model3 = html.Div(
    children=[
        dbc.Modal(
            size="xl",
            id="modal3",
            centered=True,
            is_open=False,
            children=[
                dbc.ModalHeader(
                    id="modal3_header"
                ),
                dbc.ModalBody(
                    id="modal3_body"
                )
            ]
        )
    ]
)


model4 = html.Div(
    children=[
        dbc.Modal(
            size="xl",
            id="modal4",
            centered=True,
            is_open=False,
            children=[
                dbc.ModalHeader(
                    id="modal4_header"
                ),
                dbc.ModalBody(
                    id="modal4_body"
                )
            ]
        )
    ]
)


model5 = html.Div(
    children=[
        dbc.Modal(
            size="xl",
            id="modal5",
            centered=True,
            is_open=False,
            children=[
                dbc.ModalHeader(
                    id="modal5_header"
                ),
                dbc.ModalBody(
                    id="modal5_body"
                )
            ]
        )
    ]
)


# -------------------------------------------------------------------------------------------------
# TAB HOME - BODY
# -------------------------------------------------------------------------------------------------


TAB_HOME_BODY = html.Div([
    
    html.Div(
        children=[
            
            dl.Map(
                id="map",
#                 center=[36.30, 59.60],
                zoom=5,
                children=[
                    dl.LayersControl(
                        position="topleft",
                        collapsed=False,
                        children=[
                            # html.Div("انتخاب نقشه پس زمینه:"),
                            dl.BaseLayer(
                                children=[
                                    dl.TileLayer(
                                        url=key["url"],
                                        attribution=attribution
                                    ),
                                ],
                                name=key["name"],
                                checked=key["name"] == "None"  
                            ) for key in keys.values()
                        ]
                    ), 
                    dl.LayersControl(
                        collapsed=False,
                        children=[
                            dl.Overlay(
                                children=[
                                    dl.LayerGroup(
                                        id="layer"
                                    )                                    
                                ],
                                name="click+search",
                                checked=True
                            )                            
                        ] + [
                            dl.Overlay(
                                children=[
                                    dl.GeoJSON(
                                        id="hozeh6",
                                        url=HOZEH6,
#                                         zoomToBounds=True,
#                                         zoomToBoundsOnClick=True,
                                        hoverStyle=arrow_function(
                                            dict(
                                                weight=5,
                                                color='#222',
                                                dashArray=''
                                            )
                                        ),
                                        options={
                                            "style": {
                                                "color": "red"
                                            }
                                        },
                                    )                                    
                                ],
                                name="حوضه درجه یک",
                                checked=False
                            )                            
                        ] + [
                            dl.Overlay(
                                children=[
                                    dl.GeoJSON(
                                        id="hozeh30",
                                        url=HOZEH30,
#                                         zoomToBounds=True,
#                                         zoomToBoundsOnClick=True,
                                        hoverStyle=arrow_function(
                                            dict(
                                                weight=5,
                                                color='#222',
                                                dashArray=''
                                            )
                                        ),
                                        options={
                                            "style": {
                                                "color": "green"
                                            }
                                        }                                       
                                    )                                    
                                ],
                                name="حوضه درجه دو",
                                checked=False
                            )                            
                        ] + [
                            dl.Overlay(
                                children=[
                                    dl.GeoJSON(
                                        id="mahdoude",
                                        url=MAHDOUDE,
                                        zoomToBounds=True,
                                        zoomToBoundsOnClick=True,
                                        hoverStyle=arrow_function(
                                            dict(
                                                weight=5,
                                                color='#222',
                                                dashArray=''
                                            )
                                        ),
                                        options={
                                            "style": {
                                                "color": "tomato"
                                            }
                                        }                                       
                                    )                                    
                                ],
                                name="محدوده مطالعاتی",
                                checked=True
                            )                            
                        ] + [
                            dl.Overlay(
                                children=[
                                    dl.GeoJSON(
                                        id="ostan",
                                        url=OSTAN,
#                                         zoomToBounds=True,
#                                         zoomToBoundsOnClick=True,
                                        hoverStyle=arrow_function(
                                            dict(
                                                weight=5,
                                                color='#222',
                                                dashArray=''
                                            )
                                        ),
                                        options={
                                            "style": {
                                                "color": "blue"
                                            }
                                        }                                       
                                    )                                    
                                ],
                                name="استان",
                                checked=False
                            )                            
                        ] + [
                            dl.Overlay(
                                children=[
                                    dl.GeoJSON(
                                        id="shahrestan",
                                        url=SHAHRESTAN,
#                                         zoomToBounds=True,
                                        zoomToBoundsOnClick=True,
                                        hoverStyle=arrow_function(
                                            dict(
                                                weight=5,
                                                color='#222',
                                                dashArray=''
                                            )
                                        ),
                                        options={
                                            "style": {
                                                "color": "#FD8D3C"
                                            }
                                        }                                       
                                    )                                    
                                ],
                                name="شهرستان",
                                checked=False
                            )                            
                        ]
                    ),
                    dl.LocateControl(
                        options={
                            'locateOptions': {
                                'enableHighAccuracy': True
                            }
                        }
                    ),
                    dl.MeasureControl(
                        position="topleft",
                        primaryLengthUnit="kilometers",
                        primaryAreaUnit="hectares",
                        activeColor="#214097",
                        completedColor="#972158"
                    ),
                    search_bar,
                    info,
                    model1,
                    model2,
                    model3,
                    model4,
                    model5,
                ],
                style={
                    'height': '85vh',
                    "font-family": "Tanha-FD",
                    "font-size": "medium"
                },
            ),
        ],
        dir="rtl"
    ),
    html.Div(
        children=[
            html.Div(
                id="out1",
                className="col-6"
            ),
            html.Div(
                id="out2",
                className="col-6"
            )
        ],
        className="row"
    )
])


