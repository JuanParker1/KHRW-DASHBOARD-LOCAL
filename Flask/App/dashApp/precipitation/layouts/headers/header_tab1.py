import dash_html_components as html
import dash_core_components as dcc


# -----------------------------------------------------------------------------
# Tab 1 - Header
# -----------------------------------------------------------------------------

TAB_1_HEADER = html.Div(
    children=[
        html.H3(
            children=[
                dcc.Markdown(
                    dangerously_allow_html=True,
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
