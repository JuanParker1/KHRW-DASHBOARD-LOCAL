import dash
import dash_core_components as dcc
import dash_html_components as html
from flask_login.utils import login_required
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})


def create_dashApp1(app):
    dashApp_1 = dash.Dash(
        name="App1",
        server=app,
        url_base_pathname="/dashApp1/",
        external_stylesheets=external_stylesheets
    )

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    dashApp_1.layout = html.Div(children=[
        html.H1(children='Hello Dash'),
        html.Div(children='''Dash: A web application framework for Python.'''),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

    for view_function in dashApp_1.server.view_functions:
        if view_function.startswith(dashApp_1.config.url_base_pathname):
            dashApp_1.server.view_functions[view_function] = login_required(
                dashApp_1.server.view_functions[view_function])

    return dashApp_1
