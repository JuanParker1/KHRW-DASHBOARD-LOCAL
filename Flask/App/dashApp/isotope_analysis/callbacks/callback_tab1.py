import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px

from App.dashApp.isotope_analysis.callbacks.data_analysis import *

def isotope_analysis_callback_tab1(app):
    # No Matching Data Found Template
    No_Database_Connection = {
        "layout": {
            "xaxis": {"visible": False},
            "yaxis": {"visible": False},
            "annotations": [
                {
                    "text": "No Database Connection ...",
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "font": {"size": 24}
                }
            ]
        }
    }


    # Show Filename Of Selected File
    # Tab 1 - Sidebar - Card 1
    @app.callback(
        Output('show_filename_selected_TAB1_SIDEBAR_CARD1', 'children'),
        Output('show_filename_selected_TAB1_SIDEBAR_CARD1', 'className'),
        Input('upload_button_TAB1_SIDEBAR_CARD1', 'contents'),
        State('upload_button_TAB1_SIDEBAR_CARD1', 'filename')
    )
    def update_filename_selected_tab1_sidebar_card1(contents, filename):
        if contents is None:
            return "No File Choosen!", "text-danger"
        return filename, "text-success"


    # Database (database.csv) Generator From Imported Spreadsheet File
    @app.callback(
        Output('database', 'children'),
        Output("database_generator_toast_TAB1_SIDEBAR_CARD1_CONNECT2", "is_open"),
        Output("database_generator_toast_TAB1_SIDEBAR_CARD1_CONNECT2", "icon"),
        Output("database_generator_toast_TAB1_SIDEBAR_CARD1_CONNECT2", "children"),
        Output("database_generator_toast_TAB1_SIDEBAR_CARD1_CONNECT2", "header"),
        Output("connect_button_TAB1_SIDEBAR_CARD1_CONNECT2", "n_clicks"),
        Input('upload_button_TAB1_SIDEBAR_CARD1', 'contents'),
        Input('connect_button_TAB1_SIDEBAR_CARD1_CONNECT2', 'n_clicks'),
        State('upload_button_TAB1_SIDEBAR_CARD1', 'filename')
    )
    def database_generator(contents, n, filename):
        if contents is None and n > 0:
            return "No Data", True, "danger", "Error Creating Database: No Spreadsheet Selected", "Warning!", 0
        elif n > 0:
            data = read_spreadsheet(contents, filename)
            return data.to_json(date_format='iso', orient='split'), True, "success", "Database Created Successfully", "Success!", 1
        else:
            return "No Data", False, "", "", "", 0


    # Create and Update Map
    # Tab 1 - Body - Card 1
    @app.callback(
        Output('TAB1_BODY_CONTENT1_ID', 'figure'),
        Input('connect_button_TAB1_SIDEBAR_CARD1_CONNECT2', 'n_clicks'),
        Input('database', 'children')
    )
    def update_map_tab1_body_card1(n, database):

        if database is None or database == 'No Data' or n == 0:
            return No_Database_Connection

        token = open("assets/.mapbox_token").read()

        data = pd.read_json(database, orient='split')
        geo_info = geo_info_dataset(data)

        mah_code = list(geo_info['study_area_code'].unique())

        geodf, j_file = read_shapfile(mah_code=mah_code)

        fig = px.choropleth_mapbox(data_frame=geodf,
                                geojson=j_file,
                                locations='Mah_code',
                                opacity=0.3)

        for mc in mah_code:
            df = geo_info[geo_info['study_area_code'] == mc]

            fig.add_trace(
                go.Scattermapbox(
                    lat=df.decimal_degrees_y,
                    lon=df.decimal_degrees_x,
                    mode='markers',
                    marker=go.scattermapbox.Marker(size=10),
                    text=df['st_en_name']
                )
            )

        fig.update_layout(
            mapbox={'style': "stamen-terrain",
                    'center': {'lon': 58.8,
                            'lat': 35.9},
                    'zoom': 6},
            showlegend=False,
            hovermode='closest',
            margin={'l': 0, 'r': 0, 'b': 0, 't': 0},
            mapbox_accesstoken=token
        )

        return fig


    # Tab 1 - Body - Content 2 ----------------------------------------------------
    # Create and Update Table

    @app.callback(
        Output('TAB1_BODY_CONTENT2_ID', 'data'),
        Output('TAB1_BODY_CONTENT2_ID', 'columns'),
        Output('TAB1_BODY_CONTENT2_ID', 'tooltip_header'),
        Output('TAB1_BODY_CONTENT2_ID', 'tooltip_data'),
        Input('connect_button_TAB1_SIDEBAR_CARD1_CONNECT2', 'n_clicks'),
        Input('database', 'children')
    )
    def update_table_tab1_body_card1(n, database):
        if database is None or database == 'No Data' or n == 0:
            return [{}], [], {}, [{}]
        data = pd.read_json(database, orient='split')
        geo_info = geo_info_dataset(data)
        return geo_info.to_dict('records'), [{"name": i, "id": i} for i in geo_info.columns], {j: j for j in geo_info.columns}, [
            {
                column: {'value': str(value), 'type': 'markdown'}
                for column, value in row.items()
            } for row in geo_info.to_dict('records')
        ]
