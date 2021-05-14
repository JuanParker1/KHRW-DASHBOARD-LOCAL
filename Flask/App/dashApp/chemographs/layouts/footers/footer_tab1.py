import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

"""
-------------------------------------------------------------------------------
Tab 1 - Footer
-------------------------------------------------------------------------------
"""

TAB_1_FOOTER = html.Div(
    children=[
        html.Small(
            dcc.Markdown(
                dangerously_allow_html=True,
                children=[
                    '''
                    <footer class="footer">
                        <div class="container">
                            <span class="text-muted">
                                © All Rights Reserved by <b>Khorasan Razavi Regional Water Authority</b>
                            </span>
                        </div>
                    </footer>
                    
                    '''
                ]
            ),
            className='page-header m-1 py-2')
    ],
    className="page-header text-center"
)
