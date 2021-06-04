import dash_html_components as html
import dash_core_components as dcc


# -----------------------------------------------------------------------------
# Tab 3 - Header
# -----------------------------------------------------------------------------

TAB_3_HEADER = html.Div(
    children=[
        html.H2(
            children=[
                dcc.Markdown(
                    dangerously_allow_html=True,
                    # TODO: Find Beter Way!
                    children=[
                        '''

                        '''
                    ]
                )
            ],
            className='page-header text-dark')
    ],
    className="page-header m-1 pt-2"
)
