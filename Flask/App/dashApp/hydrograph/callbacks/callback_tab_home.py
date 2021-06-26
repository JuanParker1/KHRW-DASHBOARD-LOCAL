import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash_extensions.javascript import arrow_function

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_table


def hydrograph_callback_tab_home(app):

    @app.callback(
        Output("COLLAPSE-TAB_HOME_COLLAPSE_1", "is_open"),
        Input("BUTTON_COLLAPSE-TAB_HOME_COLLAPSE_1", "n_clicks"),
        State("COLLAPSE-TAB_HOME_COLLAPSE_1", "is_open")
    )
    def toggle_accordion(n1, is_open1):
        ctx = dash.callback_context

        if not ctx.triggered:
            return False
        else:
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if button_id == "BUTTON_COLLAPSE-TAB_HOME_COLLAPSE_1" and n1:
            return not is_open1
        else:
            return False



    @app.callback(
        Output("layer", "children"),
        Output("search_lat_lng", "value"),
        Output("map", "center"),
        Input("map", "dbl_click_lat_lng"),
        Input("search_lat_lng", "value")
    )
    def map_dbl_click(dbl_click_lat_lng, search_lat_lng):
        print(search_lat_lng)
    
        if search_lat_lng is None or search_lat_lng == "" and dbl_click_lat_lng:
            result = dl.Marker(
                children=dl.Tooltip(
                    "({:.3f}, {:.3f})".format(*dbl_click_lat_lng)
                ),
                position=dbl_click_lat_lng
            )

            return [result], "", dbl_click_lat_lng
        
        else:
            
            search_lat_lng = list(
                filter(
                    ("").__ne__,
                    search_lat_lng.split(" ")
                )
            )
            
            if len(search_lat_lng) == 2:
            
                search_lat_lng = [float(x) for x in search_lat_lng]

                result = dl.Marker(
                    children=dl.Tooltip(
                        "({:.2f}, {:.2f})".format(*search_lat_lng)
                    ),
                    position=search_lat_lng
                )

                return [result], "", search_lat_lng
            else:
                raise PreventUpdate
        

    # @app.callback(
    #     Output("out1", "children"), 
    #     Input("ostan", "click_feature")
    # )
    # def ostan_click(feature):
    #     if feature is not None:
    #         return f"شما {feature['properties']['ostn_name']}"
        
    @app.callback(
        Output("info", "children"), 
        Input("ostan", "hover_feature"),
        Input("mahdoude", "hover_feature"),
    )
    def ostan_click(feature_ostan, feature_mahdoude):
        header = [
            html.H4(
                ""
            )
        ]
        
        if feature_ostan:
            return header + [
                html.B(feature_ostan["properties"]["ostn_name"]),
                html.Br(),
                "{:.1f} ha".format(feature_ostan["properties"]["AREA"] / 10000)
            ]
        elif feature_mahdoude:
            return header + [
                html.B(f"نام محدوده مطالعاتی: {feature_mahdoude['properties']['MahName']}"),
                html.Br(),
                html.B(f"کد محدوده مطالعاتی: {feature_mahdoude['properties']['MahCode']}"),
                html.Br(),
                html.B(f"حوزه درجه دو: {feature_mahdoude['properties']['Hoze30Name']}"),
                html.Br(),
                html.B(f"حوزه درجه یک: {feature_mahdoude['properties']['Hoze6Name']}"),
            ]
        else:
            return header + ["موس را روی یک محدوده نگه دارید"]


    @app.callback(
        Output("ostan", "children"),
        Input("ostan", "hover_feature"),
    )
    def oss(feature_ostan):
        if feature_ostan is not None:
            return dl.Tooltip(
                f"{feature_ostan['properties']['ostn_name']}"
            )
        else:
            raise PreventUpdate




    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
    fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                    size="population", color="continent", hover_name="country",
                    log_x=True, size_max=60)

    

    df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    fig2 = go.Figure([go.Scatter(x=df2['Date'], y=df2['AAPL.High'])])     
            

    labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    values = [4500, 2500, 1053, 500]
    fig3 = go.Figure(data=[go.Pie(labels=labels, values=values)])

    df4 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
    fig4 = dash_table.DataTable(
        id='life4',
        columns=[{"name": i, "id": i} for i in df4.columns],
        data=df4.to_dict('records'),
        style_cell={
            'maxWidth': 80
        },
        style_table={'overflowX': 'auto', 'maxWidth': '600px'}
    )

    @app.callback(
        Output("modal", "is_open"),
        Output("modal_header", "children"),
        Output("modal_body", "children"),
        Input("ostan", "click_feature"),
        Input("mahdoude", "click_feature"),
        State("modal", "is_open"),
    )
    def toggle_modal(feature_ostan, feature_mahdoude, is_open):
        if feature_ostan is not None:
            return not is_open, f"{feature_ostan['properties']['ostn_name']}", html.Div([dcc.Graph(id='life', figure=fig)])

        elif feature_mahdoude is not None:
            return not is_open, f"{feature_mahdoude['properties']['MahName']}", html.Div([dcc.Graph(id='life', figure=fig2)])
        else:
            raise PreventUpdate


    @app.callback(
        Output("modal2", "is_open"),
        Output("modal2_header", "children"),
        Output("modal2_body", "children"),
        Input("hozeh30", "click_feature"),
        State("modal2", "is_open"),
    )
    def toggle_modal2(feature_hozeh30, is_open):

        if feature_hozeh30 is not None:
            return not is_open, f"{feature_hozeh30['properties']['Hoze30Name']}", html.Div([dcc.Graph(id='life2', figure=fig3)])
        else:
            raise PreventUpdate
    

    @app.callback(
        Output("modal3", "is_open"),
        Output("modal3_header", "children"),
        Output("modal3_body", "children"),
        Input("hozeh6", "click_feature"),
        State("modal3", "is_open"),
    )
    def toggle_modal3(feature_hozeh6, is_open):

        if feature_hozeh6 is not None:
            return not is_open, f"{feature_hozeh6['properties']['Hoze6Name']}", html.Div(fig4)
        else:
            raise PreventUpdate