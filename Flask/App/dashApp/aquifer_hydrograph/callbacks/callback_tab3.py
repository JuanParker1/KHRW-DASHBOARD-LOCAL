import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px

from App.dashApp.aquifer_hydrograph.callbacks.data import *

def aquifer_hydrograph_callback_tab3(app):

    No_Matching_Data_Found_Fig = {
        "layout": {
            "xaxis": {"visible": False},
            "yaxis": {"visible": False},
            "annotations": [
                {
                    "text": "No matching data found",
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "font": {"size": 24}
                }
            ]
        }
    }

    base_map = go.Figure(
        go.Scattermapbox(
            lat=[36.25],
            lon=[59.55],
            mode='markers',
            marker=go.scattermapbox.Marker(size=9),
            text='Mashhad'
        )
    )

    base_map.update_layout(
        mapbox = {'style': "stamen-terrain",
                'center': {'lon': 59.55,
                            'lat': 36.25},
                'zoom': 5.5},
        showlegend = False,
        hovermode='closest',
        margin = {'l':0, 'r':0, 'b':0, 't':0},
        autosize=False)



    # Update Aquifer Select Dropdown - Sidebar
    @app.callback(Output('aquifer_select_sidebar_tab3', 'options'),
                Input('infoData', 'children'))
    def update_aquifer_select_sidebar_tab3(infoData):
        if infoData is None or infoData == 'No Data':
            return []
        data = pd.read_json(infoData, orient='split')
        return [{"label": col, "value": col} for col in data['نام آبخوان'].unique()]



    # Update Map Sidebar
    @app.callback(Output('mapSidebarTab3', 'figure'),
                Input('aquifer_select_sidebar_tab3', 'value'),
                Input('infoData', 'children'))
    def update_mapSidebarTab3(aquifer, infoData):
        if infoData is None or infoData == 'No Data' or aquifer is None or not aquifer:
            return base_map
        data = pd.read_json(infoData, orient='split')
        data['نام آبخوان'] = data['نام آبخوان'].apply(lambda x: x.rstrip())
        data['نام چاه'] = data['نام چاه'].apply(lambda x: x.rstrip())

        data = data[data['نام آبخوان'].isin(aquifer)]

        mah_code = list(data['کد محدوده مطالعاتی'].unique())
        geodf, j_file = read_shapfile_AreaStudy(mah_code=mah_code)

        fig = px.choropleth_mapbox(data_frame=geodf,
                                geojson=j_file,
                                locations='Mah_code',
                                opacity=0.4)

        if geodf is None or geodf.empty:
            x = 58.8
            y = 35.9
        else:
            x = geodf.geometry.centroid.x.array.mean()
            y = geodf.geometry.centroid.y.array.mean()

        fig.update_layout(
            mapbox = {'style': "stamen-terrain",
                    'center': {'lon': x,
                                'lat': y},
                    'zoom': 5},
            showlegend = False,
            hovermode='closest',
            margin = {'l':0, 'r':0, 'b':0, 't':0}
        )

        return fig



    # Show Value Slider aah number
    @app.callback(
        Output('show_delta_select_sidebar_tab3', 'children'),
        Input('delta_select_sidebar_tab3', 'value')
    )
    def update_show_delta_select_sidebar_tab3(value):
        return '{}'.format(value)





    @app.callback(Output('finalData', 'children'),
                Output('content1Tab3', 'figure'),
                Input('calculate_button_sidebar_tab3', 'n_clicks'),
                State('rawData', 'children'),
                State('aquifer_select_sidebar_tab3', 'value'),
                State('delta_select_sidebar_tab3', 'value'),
                State('select_mean_aquifer_head', 'value'))
    def adjustment_aquifer_head(n_clicks, data, aquifer, threshold, mean_type):
        if data == 'No Data' or aquifer is None or threshold is None or n_clicks == 0:
            df = 'No Data'
            fig = No_Matching_Data_Found_Fig
            return df, fig

        df = pd.read_json(data, orient='split')

        if len(aquifer) == 1:
            df_1 = df[df['نام آبخوان'] == aquifer[0]]
            Final_Table = df_1[['Date_Gregorian', 'Date_Persian', 'Aquifer_Head', 'Aquifer_Head_Arithmetic_Mean', 'Aquifer_Head_Geometric_Mean', 'Aquifer_Head_Harmonic_Mean']].groupby(
                by=['Date_Gregorian', 'Date_Persian']).mean().reset_index()
            Final_Table.replace(0, np.nan, inplace=True)
            Final_Table['Delta'] = Final_Table['Aquifer_Head'].diff().fillna(0)
            Final_Table['Index'] = abs(Final_Table['Delta']).apply(lambda x: 1 if x >= threshold else 0)
            Final_Table['Adjusted_Aquifer_Head'] = Final_Table['Aquifer_Head']

            n = Final_Table.index[Final_Table['Index'] == True].tolist()

            if len(n) > 0:
                while len(n) != 0:
                    delta = Final_Table['Delta'][n[0]]
                    Final_Table['Temp_Aquifer_Head'] = Final_Table['Adjusted_Aquifer_Head']
                    for i in range(n[0]):
                        Final_Table['Temp_Aquifer_Head'][i] = Final_Table['Adjusted_Aquifer_Head'][i] + delta
                        Final_Table['Adjusted_Aquifer_Head'] = Final_Table['Temp_Aquifer_Head']
                        Final_Table['Delta'] = Final_Table['Adjusted_Aquifer_Head'].diff().fillna(0)
                        Final_Table['Index'] = abs(Final_Table['Delta']).apply(lambda x: 1 if x >= threshold else 0)
                        n = Final_Table.index[Final_Table['Index'] == True].tolist()

            if 'Temp_Aquifer_Head' in Final_Table.columns:
                Final_Table = Final_Table.drop(['Temp_Aquifer_Head'], axis=1)

            if 'Delta' in Final_Table.columns:
                Final_Table = Final_Table.drop(['Delta'], axis=1)

            if 'Index' in Final_Table.columns:
                Final_Table = Final_Table.drop(['Index'], axis=1)

            df_1 = pd.merge(left=df_1,
                        right=Final_Table[['Date_Gregorian', 'Date_Persian', 'Adjusted_Aquifer_Head']],
                        how='outer',
                        on=['Date_Gregorian', 'Date_Persian']).sort_values(['ID', 'Date_Gregorian'])

            # df_1.to_excel("output.xlsx", sheet_name='Sheet_name_1')
            # Final_Table.to_excel("Final_Table.xlsx", sheet_name='Sheet_name_1')
            
            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=Final_Table['Date_Persian'],
                    y=Final_Table['Aquifer_Head'],
                    mode='lines+markers',
                    name='تعدیل نشده'
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=Final_Table['Date_Persian'],
                    y=Final_Table['Adjusted_Aquifer_Head'],
                    mode='lines+markers',
                    name='تعدیل شده'
                )
            )

            if 'Arithmetic' in mean_type:
                fig.add_trace(
                    go.Scatter(
                        x=Final_Table['Date_Persian'],
                        y=Final_Table['Aquifer_Head_Arithmetic_Mean'],
                        mode='lines+markers',
                        name='میانگین حسابی'
                    )
                )

            if 'Geometric' in mean_type:
                fig.add_trace(
                    go.Scatter(
                        x=Final_Table['Date_Persian'],
                        y=Final_Table['Aquifer_Head_Geometric_Mean'],
                        mode='lines+markers',
                        name='میانگین هندسی'
                    )
                )

            if 'Harmonic' in mean_type:
                fig.add_trace(
                    go.Scatter(
                        x=Final_Table['Date_Persian'],
                        y=Final_Table['Aquifer_Head_Harmonic_Mean'],
                        mode='lines+markers',
                        name='میانگین هارمونیک'
                    )
                )


            title_name = 'متوسط تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی در آبخوان ' + aquifer[0]

            fig.update_layout(
                title=title_name,
                xaxis_title="تاریخ",
                yaxis_title="ارتفاع سطح آب ایستابی - متر",
                autosize=False,
                font=dict(
                    family="B Koodak",
                    size=16,
                    color="RebeccaPurple"
                ),
                xaxis=dict(
                    tickformat="%Y-%m"
                ),
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1,
                    xanchor="left",
                    x=0
                )
            )
            
            return df_1.to_json(date_format='iso', orient='split'), fig


        if len(aquifer) > 1:
            df_many = df[df['نام آبخوان'].isin(aquifer)]

            fig = go.Figure()

            for aq in aquifer:
                df_aquifer = df_many[df_many['نام آبخوان'] == aq]

                Final_Table = df_aquifer[['Date_Gregorian', 'Date_Persian', 'Aquifer_Head', 'Aquifer_Head_Arithmetic_Mean', 'Aquifer_Head_Geometric_Mean', 'Aquifer_Head_Harmonic_Mean']].groupby(
                    by=['Date_Gregorian', 'Date_Persian']).mean().reset_index()
                Final_Table.replace(0, np.nan, inplace=True)
                Final_Table['Delta'] = Final_Table['Aquifer_Head'].diff().fillna(0)
                Final_Table['Index'] = abs(Final_Table['Delta']).apply(lambda x: 1 if x >= threshold else 0)
                Final_Table['Adjusted_Aquifer_Head'] = Final_Table['Aquifer_Head']

                n = Final_Table.index[Final_Table['Index'] == True].tolist()

                if len(n) > 0:
                    while len(n) != 0:
                        delta = Final_Table['Delta'][n[0]]
                        Final_Table['Temp_Aquifer_Head'] = Final_Table['Adjusted_Aquifer_Head']
                        for i in range(n[0]):
                            Final_Table['Temp_Aquifer_Head'][i] = Final_Table['Adjusted_Aquifer_Head'][i] + delta
                            Final_Table['Adjusted_Aquifer_Head'] = Final_Table['Temp_Aquifer_Head']
                            Final_Table['Delta'] = Final_Table['Adjusted_Aquifer_Head'].diff().fillna(0)
                            Final_Table['Index'] = abs(Final_Table['Delta']).apply(lambda x: 1 if x >= threshold else 0)
                            n = Final_Table.index[Final_Table['Index'] == True].tolist()

                if 'Temp_Aquifer_Head' in Final_Table.columns:
                    Final_Table = Final_Table.drop(['Temp_Aquifer_Head'], axis=1)

                if 'Delta' in Final_Table.columns:
                    Final_Table = Final_Table.drop(['Delta'], axis=1)

                if 'Index' in Final_Table.columns:
                    Final_Table = Final_Table.drop(['Index'], axis=1)

                df_aquifer = pd.merge(left=df_aquifer,
                                        right=Final_Table[['Date_Gregorian', 'Date_Persian', 'Adjusted_Aquifer_Head']],
                                        how='outer',
                                        on=['Date_Gregorian', 'Date_Persian']).sort_values(['ID', 'Date_Gregorian'])

                fig.add_trace(
                    go.Scatter(
                        x=Final_Table['Date_Persian'],
                        y=Final_Table['Adjusted_Aquifer_Head'],
                        mode='lines+markers',
                        name=aq
                    )
                )


            title_name = 'متوسط تراز ماهانه (روز پانزدهم) تعدیل شده سطح آب زیرزمینی در آبخوان'

            fig.update_layout(
                title=title_name,
                xaxis_title="تاریخ",
                yaxis_title="ارتفاع سطح آب ایستابی - متر",
                autosize=False,
                font=dict(
                    family="B Koodak",
                    size=16,
                    color="RebeccaPurple"
                ),
                xaxis=dict(
                    tickformat="%Y-%m"
                ),
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1,
                    xanchor="left",
                    x=0
                )
            )


            return Final_Table.to_json(date_format='iso', orient='split'), fig

