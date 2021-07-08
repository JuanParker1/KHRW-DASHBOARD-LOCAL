import base64
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.layouts.visualizations.visualization import *



# -----------------------------------------------------------------------------
# Tab 2 - Sidebar - Left
# -----------------------------------------------------------------------------

"""
---------------------------------------
Left - Card 1: 
---------------------------------------
"""

TAB2_SIDEBAR_LEFT_CARD_1_IMG = base64.b64encode(
   open('./App/static/images/groundwater/well.png', 'rb').read()
)  # EDITPATH



TAB2_SIDEBAR_LEFT_CARD_1 = html.Div(
    children=[
        html.H6(
            children=[
                "   چاه مشاهده‌ای",
                html.Img(src='data:image/png;base64,{}'.format(TAB2_SIDEBAR_LEFT_CARD_1_IMG.decode()), height=30, className="ml-2"),
            ],
            className='card-header text-right'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "انتخاب آبخوان:"
                            ],
                            dir="rtl",
                            className="text-right "
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="SELECT_AQUIFER-TAB2_SIDEBAR_LEFT_CARD1",
                                    placeholder="یک یا چند آبخوان انتخاب کنید",
                                    multi=True,
                                    # persistence=True,
                                    # persistence_type="memory",
                                )
                            ],
                        ),
                    ],
                    className="form-group mb-4"
                ),
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "انتخاب چاه مشاهده‌ای:"
                            ],
                            dir="rtl",
                            className="text-right "
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="SELECT_WELL-TAB2_SIDEBAR_LEFT_CARD1",
                                    placeholder="یک یا چند چاه مشاهده‌ای انتخاب کنید",
                                    multi=True,
                                    # persistence=True,
                                    # persistence_type="memory",
                                )
                            ],
                        ),
                    ],
                    className="form-group mb-4"
                ),
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "انتخاب بازه زمانی:"
                            ],
                            dir="rtl",
                            className="text-right "
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="SELECT_START_YEAR-TAB2_SIDEBAR_LEFT_CARD1",
                                    placeholder="سال شروع",
                                    # persistence=True,
                                    # persistence_type="memory",
                                    options=[
                                        {'label': '{}'.format(i), 'value': i} for i in range(1370, 1426)
                                    ],
                                    value=1380
                                ),
                                dcc.Dropdown(
                                    id="SELECT_END_YEAR-TAB2_SIDEBAR_LEFT_CARD1",
                                    placeholder="سال پایان",
                                    value=1400
                                    # persistence=True,
                                    # persistence_type="memory",

                                )
                            ],
                        ),
                    ],
                    className="form-group mb-4"
                ),
                html.Div(
                    children=[
                        MAP_TAB2_SIDEBAR_LEFT_CARD1
                    ],
                    className="form-group mb-0"
                ),
            ],
            className='card-body text-dark'
        ),
    ],
    className='card border-dark my-2'
)

"""
---------------------------------------
Left - Card 2: 
---------------------------------------
"""




TAB2_SIDEBAR_LEFT_CARD_2 = html.Div(
    children=[
        html.H6(
            children=[
                "تنظیمات جدول خروجی",
                html.I(className="fa fa-table ml-2"),
            ],
            className='card-header text-right'
        ),
        html.Div(
            children=[
                
                html.H6(
                    children=[
                        "انتخاب دوره آماری:"
                    ],
                    dir="rtl",
                    className="text-right"
                ),
                
                dcc.RadioItems(
                    id="SELECT_TYPE_YEAR-TAB2_SIDEBAR_LEFT_CARD2",
                    options=[
                        {'label': 'سال آبی', 'value': 'WATER_YEAR'},
                        {'label': 'سال شمسی', 'value': 'PERSIAN_YEAR'},
                    ],
                    value='WATER_YEAR',
                    labelClassName ="d-block mr-3 text-right text-secondary font_size"    ,
                    inputClassName="ml-1"           
                )

            ],
            dir="rtl",
            className='card-body text-dark text-right'
        ),
        html.Div(
            children=[
                
                html.H6(
                    children=[
                        "انتخاب پارامتر:"
                    ],
                    dir="rtl",
                    className="text-right"
                ),
                
                dcc.RadioItems(
                    id="SELECT_PARAMETER-TAB2_SIDEBAR_LEFT_CARD2",
                    options=[
                        {'label': 'تراز سطح آب', 'value': 'WATER_TABLE_MONTLY'},
                        {'label': 'تغییرات تراز سطح آب (نسبت به ماه قبل)', 'value': 'WATER_TABLE_DIFF_MONTLY'},
                        {'label': 'تغییرات تراز سطح آب (نسبت به ماه سال قبل)', 'value': 'WATER_TABLE_DIFF_MONTLY_YEARLY'},
                    ],
                    value='WATER_TABLE_MONTLY',
                    labelClassName ="d-block mr-3 text-right text-secondary font_size",
                    inputClassName="ml-1"           
                )

            ],
            dir="rtl",
            className='card-body text-dark text-right'
        ),
            html.Div(
            children=[
                html.H6(
                    children=[
                        "انتخاب تحلیل آماری:"
                    ],
                    dir="rtl",
                    className="text-right"
                ),
                
                dcc.Checklist(
                    id="STATISTICAL_ANALYSIS-TAB2_SIDEBAR_LEFT_CARD2",
                    options=[
                        {'label': 'نمایش تحلیل‌های آماری', 'value': 'STATISTICAL_ANALYSIS'},
                    ],
                    labelClassName ="d-block mr-3 text-right text-secondary font_size",
                    inputClassName="ml-1"           
                )

            ],
            dir="rtl",
            className='card-body text-dark text-right'
        ),
        # Hidden Div For Store Data--------------------------------------------
        html.Div(
            children=[
                html.Div(
                    id="STATE_TABLE_DOWNLOAD_BUTTON-TAB2_SIDEBAR",
                )
            ],
            style={
                'display': 'none'
            }
        )
    ],
    className='card border-dark mt-3'
)




"""
---------------------------------------
Sidebar Tab 1 - Left
---------------------------------------
"""

TAB_2_SIDEBAR_LEFT = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB2_SIDEBAR_LEFT_CARD_1,
                        TAB2_SIDEBAR_LEFT_CARD_2
                    ],
                    className='col px-0'
                ),
            ],
            className='row'
        ),
    ],
    className="container-fluid"
)






# -----------------------------------------------------------------------------
# Tab 2 - Sidebar - Right
# -----------------------------------------------------------------------------


"""
---------------------------------------
Right - Card 1
---------------------------------------
"""

TAB2_SIDEBAR_RIGHT_CARD_1_IMG_1 = base64.b64encode(
   open('./App/static/images/groundwater/aquifer.jpg', 'rb').read()
)  # EDITPATH

TAB2_SIDEBAR_RIGHT_CARD_1_IMG_2 = base64.b64encode(
   open('./App/static/images/groundwater/well.png', 'rb').read()
)  # EDITPATH

TAB2_SIDEBAR_RIGHT_CARD_1 = html.Div(
    className='mt-2 text-right border border-secondary rounded',
    dir="rtl",
    children=[
        html.Div(
            className='card bg-light',
            children=[
                
                html.Img(
                    id="IMG_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                    height=220,
                    width=220,
                    className="mt-3 rounded mx-auto d-block"
                ),
                
                html.Div(
                    className='card-body', 
                    children=[
                        html.H5(
                            id="NAME_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='card-title mb-0',
                        ),
                        # html.P(
                        #     className='card-text',
                        #     children='چاه حسن آباد در آبخوان جوین واقع شده است.'
                        # )                        
                    ]
                ),
                
                html.Ul(
                    className='list-group list-group-flush', 
                    children=[
                        html.Li(
                            id="ID_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item'
                        ),                      
                        html.Li(
                            id="AQUIFER_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item',
                        ),
                        html.Li(
                            id="LONG_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item', 
                        ),
                        html.Li(
                            id="LAT_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item', 
                        ),
                        html.Li(
                            id="ELEV_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item', 
                        ),
                        html.Li(
                            id="START_DATE_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item'
                        ),
                        html.Li(
                            id="END_DATE_OW-TAB2_SIDEBAR_RIGHT_CARD1",
                            className='list-group-item'
                        ),
                    ]
                )
                
            ]
        )
    ]
)



"""
---------------------------------------
Sidebar Tab 2 - Right
---------------------------------------
"""

TAB_2_SIDEBAR_RIGHT = html.Div(
    id="SHOW_HIDE-TAB2_SIDEBAR_RIGHT",
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB2_SIDEBAR_RIGHT_CARD_1
                    ],
                    className='col px-0'
                ),
            ],
            className='row'
        ),
    ],
    className="container-fluid"
)
