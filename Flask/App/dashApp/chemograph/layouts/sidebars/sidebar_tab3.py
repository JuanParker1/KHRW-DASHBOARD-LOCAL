import base64
import numpy as np
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from App.dashApp.chemograph.layouts.visualizations.visualization import *



# -----------------------------------------------------------------------------
# Tab 3 - Sidebar - Left
# -----------------------------------------------------------------------------

"""
---------------------------------------
Left - Card 1: 
---------------------------------------
"""

TAB3_SIDEBAR_LEFT_CARD_1_IMG = base64.b64encode(
   open('./App/static/chemograph/images/aquifer.jpg', 'rb').read()
)  # EDITPATH

TAB3_SIDEBAR_LEFT_CARD_1 = html.Div(
    children=[
        html.H6(
            children=[
                "    آبخوان",
                html.Img(src='data:image/png;base64,{}'.format(TAB3_SIDEBAR_LEFT_CARD_1_IMG.decode()), height=30, className="ml-2"),
            ],
            className='card-header text-right'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Button(
                            children=[
                                "محاسبه کموگراف آبخوان",
                                html.I(className="fa fa-calculator ml-2"),
                            ],
                            n_clicks=0,
                            className="btn btn-secondary mb-4",
                            id="CALCULATE_AQUIFER_CHEMOGRAPH-TAB3_SIDEBAR_LEFT_CARD1"
                        ),
                        dbc.Toast(
                            is_open=False,
                            dismissable=True,
                            duration=5000,
                            className="popup-notification",
                            id="POPUP_CALCULATE_AQUIFER_CHEMOGRAPH-TAB3_SIDEBAR_CARD1"
                        )
                    ],
                    className="d-flex justify-content-center"
                ),             
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
                                    id="SELECT_AQUIFER-TAB3_SIDEBAR_LEFT_CARD1",
                                    placeholder="یک یا چند آبخوان انتخاب کنید",
                                    multi=True,
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
                                "انتخاب پارامتر:"
                            ],
                            dir="rtl",
                            className="text-right "
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="SELECT_PARAMETER-TAB3_SIDEBAR_LEFT_CARD1",
                                    placeholder="یک پارامتر انتخاب کنید",
                                    multi=False,
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
                                    id="SELECT_START_YEAR-TAB3_SIDEBAR_LEFT_CARD1",
                                    placeholder="سال شروع",
                                    options=[
                                        {'label': '{}'.format(i), 'value': i} for i in range(1370, 1426)
                                    ],
                                    value=1380
                                ),
                                dcc.Dropdown(
                                    id="SELECT_END_YEAR-TAB3_SIDEBAR_LEFT_CARD1",
                                    placeholder="سال پایان",
                                    value=1400
                                )
                            ],
                        ),
                    ],
                    className="form-group mb-4"
                ),
                html.Div(
                    children=[
                        MAP_TAB3_SIDEBAR_LEFT_CARD1
                    ],
                    className="form-group mb-0"
                ),
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "انتخاب محل نمونه برداری:"
                            ],
                            dir="rtl",
                            className="text-right "
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="SELECT_WELL-TAB3_SIDEBAR_LEFT_CARD1",
                                    placeholder="یک یا چند چاه محل نمونه برداری انتخاب کنید",
                                    multi=True,
                                )
                            ],
                        ),
                    ],
                    className="form-group mt-4"
                ),
            ],
            className='card-body text-dark'
        ),
        # Hidden Div For Store Data--------------------------------------------
        html.Div(
            children=[
                html.Div(
                    id="STATE_TABLE_CHEMOGHRAP-TAB3_SIDEBAR",
                )
            ],
            style={
                'display': 'none'
            }
        )
    ],
    className='card border-dark my-2'
)





"""
---------------------------------------
Left - Card 2: 
---------------------------------------
"""

TAB3_SIDEBAR_LEFT_CARD_2 = html.Div(
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
                    id="SELECT_TYPE_YEAR-TAB3_SIDEBAR_LEFT_CARD2",
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
                    id="SELECT_PARAMETER-TAB3_SIDEBAR_LEFT_CARD2",
                    options=[
                        {'label': 'تراز سطح آب', 'value': 'WATER_TABLE_MONTLY'},
                        {'label': 'تغییرات تراز سطح آب (نسبت به ماه قبل)', 'value': 'WATER_TABLE_DIFF_MONTLY'},
                        {'label': 'تغییرات تراز سطح آب (نسبت به ماه سال قبل)', 'value': 'WATER_TABLE_DIFF_MONTLY_YEARLY'},
                        {'label': 'تغییرات ذخیره آبخوان (نسبت به ماه قبل)', 'value': 'STOREG_DIFF_MONTLY'},
                        {'label': 'تغییرات ذخیره آبخوان (نسبت به ماه سال قبل)', 'value': 'STOREG_DIFF_MONTLY_YEARLY'},
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
                    id="STATISTICAL_ANALYSIS-TAB3_SIDEBAR_LEFT_CARD2",
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
                    id="STATE_TABLE_DOWNLOAD_BUTTON-TAB3_SIDEBAR",
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
Sidebar Tab 3 - Left
---------------------------------------
"""

TAB_3_SIDEBAR_LEFT = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB3_SIDEBAR_LEFT_CARD_1,
                        # TAB3_SIDEBAR_LEFT_CARD_2
                    ],
                    className='col px-0'
                ),
            ],
            className='row'
        ),
    ],
    className="container-fluid"
)