import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table


# -----------------------------------------------------------------------------
# Tab 1 - Body
# -----------------------------------------------------------------------------


# Tab 1 - Body - Content 1 --------------------------------
# Map: Study Area & Stations.

TAB1_BODY_CONTENT1 = dcc.Graph(
    id='TAB1_BODY_CONTENT1_ID',
    className="w-100 h-100 mx-4 mb-4",
)


# Tab 1 - Body - Content 2 --------------------------------
# Table: Geographic Information of Stations.

TAB1_BODY_CONTENT2 = dash_table.DataTable(
    id='TAB1_BODY_CONTENT2_ID',
    style_table={
        'overflowX': 'auto',
        'overflowY': 'auto',
        # 'padding': '5px'
    },
    style_cell={
        'border': '1px solid grey',
        'font-size': '14px',
        # 'font_family': 'B Koodak',
        'text_align': 'right',
        'minWidth': 50,
        'maxWidth': 100,
        'width': 75
    },
    style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold',
        'whiteSpace': 'normal',
    },
    css=[{
        'selector': '.dash-table-tooltip',
        'rule': 'background-color: yellow;'
    }],
    tooltip_delay=0,
    tooltip_duration=None,
    page_size=15
)
