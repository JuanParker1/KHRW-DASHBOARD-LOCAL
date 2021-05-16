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
    id='MAP-TAB1_BODY_CONTENT1',
    className="w-100 h-100 mx-4 mb-4"
)


# Tab 1 - Body - Content 2 --------------------------------
# Table: Geographic Information of Stations.

TAB1_BODY_CONTENT2 = dash_table.DataTable(
    id='TABLE-TAB1_BODY_CONTENT2',
    filter_action="native",
    sort_action="native",
    sort_mode="multi",
    style_table={
        'overflowX': 'auto',
        'overflowY': 'auto',
    },
    style_cell={
        'border': '1px solid grey',
        'font-size': '14px',
        'font_family': 'Tanha-FD',
        'text_align': 'center',
        'minWidth': 40,
        'maxWidth': 120,
        'width': 80
    },
    style_header={
        'backgroundColor': 'rgb(220, 220, 220)',
        'fontWeight': 'bold',
        # 'whiteSpace': 'normal',
        'text_align': 'center',
    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        },
        {
            'if': {'column_id': ['نام چاه', 'نام آبخوان', 'نام محدوده']},
            'textAlign': 'right'
        },
        # {
        #     'if': {'column_id': ['طول جغرافیایی', 'عرض جغرافیایی', 'ارتفاع']},
        #     'textAlign': 'left'
        # }
    ],
    css=[{
        'selector': '.dash-table-tooltip',
        'rule': 'background-color: yellow;'
    }],
    page_size=6
)
