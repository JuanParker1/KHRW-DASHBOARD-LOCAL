import base64
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


DATA_CLEANSING_TAB_CARD_1_IMG = base64.b64encode(
   open('./App/static/images/groundwater/well.png', 'rb').read()
)  # EDITPATH



DATA_CLEANSING_TAB_CARD_1 = html.Div(
    children=[
        # html.H6(
        #     children=[
        #         html.Img(src='data:image/png;base64,{}'.format(DATA_CLEANSING_TAB_CARD_1_IMG.decode()), height=30, className="ml-2"),
        #         "چاه مشاهده‌ای",
        #     ],
        #     className='card-header text-right'
        # ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H6(
                            children=[
                                "انتخاب محدوده:"
                            ],
                            dir="rtl",
                            className="text-right "
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="STUDY_AREA_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1",
                                    placeholder="یک یا چند محدوده انتخاب کنید",
                                    multi=True,
                                )
                            ],
                        ),
                    ],
                    className="col-4 form-group"
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
                                    id="AQUIFER_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1",
                                    placeholder="یک یا چند آبخوان انتخاب کنید",
                                    multi=True,
                                )
                            ],
                        ),
                    ],
                    className="col-4 form-group"
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
                                    id="WELL_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1",
                                    placeholder="یک یا چند چاه مشاهده‌ای انتخاب کنید",
                                    multi=True,
                                )
                            ],
                        ),
                    ],
                    className="col-4 form-group"
                ),
                # html.Div(
                #     children=[
                #         html.H6(
                #             children=[
                #                 "انتخاب بازه زمانی:"
                #             ],
                #             dir="rtl",
                #             className="text-right "
                #         ),
                #         html.Div(
                #             children=[
                #                 dcc.Dropdown(
                #                     id="START_YEAR_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1",
                #                     placeholder="سال شروع",
                #                     options=[
                #                         {'label': '{}'.format(i), 'value': i} for i in range(1370, 1426)
                #                     ],
                #                     style=dict(width='100%'),
                #                     className="Select-value"
                #                 ),
                #                 dcc.Dropdown(
                #                     id="END_YEAR_SELECT-DATA_CLEANSING_TAB-SIDEBAR_CARD_1",
                #                     placeholder="سال پایان",
                #                     style=dict(width='100%'),
                #                     className="Select-value"
                #                 ),
                #             ],
                #             style=dict(display='flex')
                #         ),
                #     ],
                #     className="flex"
                # ),
                html.Div(
                    children=[
                        # MAP_TAB2_SIDEBAR_LEFT_CARD1
                    ],
                    className="form-group mb-0"
                ),
            ],
            className='row card-body text-dark'
        ),
    ],
    className='card border-dark mt-2'
)



"""
---------------------------------------
Sidebar Tab Data Cleansing
---------------------------------------
"""

DATA_CLEANSING_TAB_SIDEBAR = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        DATA_CLEANSING_TAB_CARD_1
                    ],
                    className='col px-0'
                ),
            ],
            className='row'
        ),
    ],
    className="container-fluid"
)