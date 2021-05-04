import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from flask_login.utils import login_required

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


def create_dashApp2(app):
    dashApp_2 = dash.Dash(
        name="App2",
        server=app,
        url_base_pathname="/dashApp2/",
        external_stylesheets=external_stylesheets
    )

    dashApp_2.layout = html.Div([
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            id='year-slider',
            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'].min(),
            marks={str(year): str(year) for year in df['year'].unique()},
            step=None
        )
    ])

    @dashApp_2.callback(
        Output('graph-with-slider', 'figure'),
        Input('year-slider', 'value'))
    def update_figure(selected_year):
        filtered_df = df[df.year == selected_year]

        fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                         size="pop", color="continent", hover_name="country",
                         log_x=True, size_max=55)

        fig.update_layout(transition_duration=500)

        return fig

    for view_function in dashApp_2.server.view_functions:
        if view_function.startswith(dashApp_2.config.url_base_pathname):
            dashApp_2.server.view_functions[view_function] = login_required(
                dashApp_2.server.view_functions[view_function])

    return dashApp_2
