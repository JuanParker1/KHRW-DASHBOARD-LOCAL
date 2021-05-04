import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from flask_login.utils import login_required


df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')


def callbackgen(app):
    @app.callback(
        Output('graph-with-slider', 'figure'),
        Input('year-slider', 'value'))
    def update_figure(selected_year):
        filtered_df = df[df.year == selected_year]

        fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                         size="pop", color="continent", hover_name="country",
                         log_x=True, size_max=55)

        fig.update_layout(transition_duration=500)

        return fig
