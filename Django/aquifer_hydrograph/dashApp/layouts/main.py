# from aquifer_hydrograph.dashApp.app import app

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from aquifer_hydrograph.dashApp.layouts.tabs import tab1, tab2, tab3

main_layout = html.Div(
    children=[
        # html.Div(
        #     children=html.Img(
        #         src=app.get_asset_url("khrw_logo.jpg"),
        #     )
        # ),
        dbc.Tabs(
            className='mainLayoutTabs',
            children=[
                dbc.Tab(
                    id='Tab1',
                    label='ورود داده ها',
                    tabClassName='tabClassName',
                    labelClassName='labelClassName',
                    children=[
                        tab1
                    ]
                ),
                dbc.Tab(
                    id='Tab2',
                    label='چاه های مشاهده ای',
                    tabClassName='tabClassName',
                    labelClassName='labelClassName',
                    children=[
                        tab2
                    ]
                ),
                dbc.Tab(
                    id='Tab3',
                    label='هیدروگراف آبخوان',
                    tabClassName='tabClassName',
                    labelClassName='labelClassName',
                    children=[
                        tab3
                    ]
                )
            ]
        )
    ]
)
