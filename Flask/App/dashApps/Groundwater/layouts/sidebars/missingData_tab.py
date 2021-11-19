# -----------------------------------------------------------------------------
# MISSING DATA TAB - SIDEBAR
# -----------------------------------------------------------------------------



# -------------------------------------
# MODULES
# -------------------------------------

import base64
import numpy as np
from datetime import date
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_table



# -------------------------------------
# CONTROLS
# -------------------------------------

# STUDY AREA:
STUDY_AREA_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            dir='rtl', 
            children='- محدوده مطالعاتی',
            style={
                "font-weight": "bold",
                "font-size": "1rem",
            }
        ),
        dcc.Dropdown(
            id='STUDY_AREA_SELECT___CONTROLS___MISSING_DATA_TAB', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)

# AQUIFER:
AQUIFER_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            className='text-center',
            dir='rtl', 
            children='- آبخوان',
            style={
                "font-weight": "bold",
                "font-size": "1rem",
            }
        ),
        dcc.Dropdown(
            id='AQUIFER_SELECT___CONTROLS___MISSING_DATA_TAB', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)

# WELL:
WELL_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            className='text-center',
            dir='rtl', 
            children='- چاه مشاهده‌ای',
            style={
                "font-weight": "bold",
                "font-size": "1rem",
            }
        ),
        dcc.Dropdown(
            id='WELL_SELECT___CONTROLS___MISSING_DATA_TAB', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)


# INTERPOLATE METHOD:
INTERPOLATE_METHOD_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            className='text-center',
            dir='rtl', 
            children='- انتخاب روش',
            style={
                "font-weight": "bold",
                "font-size": "1rem",
            }
        ),
        dcc.Dropdown(
            id='INTERPOLATE_METHOD_SELECT___CONTROLS___MISSING_DATA_TAB', 
            value='akima',
            options=[
                {'label': 'Back Fill', 'value': 'bfill'},
                {'label': 'Forward Fill', 'value': 'ffill'},
                {'label': 'Pad', 'value': 'pad'},
                {'label': 'Zero', 'value': 'zero'},
                {'label': 'Linear', 'value': 'linear'},
                {'label': 'Slinear', 'value': 'slinear'},
                {'label': 'Akima', 'value': 'akima'},
                {'label': 'Nearest', 'value': 'nearest'},
                {'label': 'Spline', 'value': 'spline'},
                {'label': 'Polynomial', 'value': 'polynomial'},
                {'label': 'Cubic', 'value': 'cubic'},
                {'label': 'Quadratic', 'value': 'quadratic'},
                {'label': 'Barycentric', 'value': 'barycentric'},
                {'label': 'Krogh', 'value': 'krogh'},
                {'label': 'Piecewise Polynomial', 'value': 'piecewise_polynomial'},
                {'label': 'Pchip', 'value': 'pchip'},
                {'label': 'Cubicspline', 'value': 'cubicspline'},
            ],
            clearable=False
        ) 
    ]
)




# ORDER INTERPOLATE METHOD:
ORDER_INTERPOLATE_METHOD_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            className='text-center',
            dir='rtl', 
        children='- مرتبه',
        style={
            "font-weight": "bold",
            "font-size": "1rem",
        }
        ),
        dcc.Dropdown(
            id='ORDER_INTERPOLATE_METHOD_SELECT___CONTROLS___MISSING_DATA_TAB', 
            value=1,
            disabled=True,
            options=[
                {'label': '0', 'value': 0},
                {'label': '1', 'value': 1},
                {'label': '2', 'value': 2},
                {'label': '3', 'value': 3},
                {'label': '4', 'value': 4},
                {'label': '5', 'value': 5},
            ],
            clearable=False
        ) 
    ]
)

# DURATION:
DURATION_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            className='text-center',
            dir='rtl', 
        children='- بیشترین تعداد مقادیر گمشده پی در پی',
        style={
            "font-weight": "bold",
            "font-size": "1rem",
        }
        ),
        dcc.Dropdown(
            id='DURATION_SELECT___CONTROLS___MISSING_DATA_TAB', 
            value=6,
            options=[
                {'label': 'بدون محدودیت', 'value': 0},
                {'label': '1', 'value': 1},
                {'label': '2', 'value': 2},
                {'label': '3', 'value': 3},
                {'label': '4', 'value': 4},
                {'label': '6', 'value': 6},
                {'label': '9', 'value': 9},
                {'label': '12', 'value': 12},
                {'label': '15', 'value': 15},
                {'label': '18', 'value': 18},
                {'label': '21', 'value': 21},
                {'label': '24', 'value': 24},
            ],
            clearable=False
        ) 
    ]
)






HOW_MODIFY_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
    className='form-group', 
    children=[
        dcc.RadioItems(
            id='HOW_MODIFY_CARD___CONTROLS___MISSING_DATA_TAB', 
            value=3,
            options=[
                {'label': 'بازسازی چاه مشاهده‌ای انتخابی', 'value': 0},
                {'label': 'بازسازی همه چاه‌های مشاهده‌ای آبخوان انتخابی', 'value': 1},
                {'label': 'بازسازی همه چاه‌های مشاهده‌ای محدوده انتخابی', 'value': 2},
                {'label': 'بازسازی همه چاه‌های مشاهده‌ای', 'value': 3},
            ],
            inputClassName="ml-1"
        ) 
    ]
)



# -------------------------------------
# BUTTONS
# -------------------------------------

# BUTTON:
BUTTON___BUTTONS___MISSING_DATA_TAB = dbc.Button(
    id='BUTTON___BUTTONS___MISSING_DATA_TAB',
    className="me-1",
    size="lg",
    children='بروزرسانی پایگاه داده', 
    color='primary',
    n_clicks=0
)

# TOAST:
TOAST___BUTTONS___MISSING_DATA_TAB = dbc.Toast(
    id='TOAST___BUTTONS___MISSING_DATA_TAB',
    is_open=False,
    dismissable=True,
    duration=5000
)




# -------------------------------------
# SIDEBAR
# -------------------------------------

SIDEBAR___MISSING_DATA_TAB = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        html.H5(
            className="text-center pb-2",
            children="انتخاب چاه مشاهده‌ای",
            style={
                "color": "#2c8cff",
                "font-size": "1.3rem",
                "font-weight": "bold",
                "font-weight": 300,
            }
        ),
        STUDY_AREA_CARD___CONTROLS___MISSING_DATA_TAB,
        AQUIFER_CARD___CONTROLS___MISSING_DATA_TAB,
        WELL_CARD___CONTROLS___MISSING_DATA_TAB,
        html.H5(
            className="text-center pb-2 pt-4",
            children="درون‌یابی مقادیر گمشده",
            style={
                "color": "#2c8cff",
                "font-size": "1.3rem",
                "font-weight": "bold",
                "font-weight": 300,
            }
        ),
        INTERPOLATE_METHOD_CARD___CONTROLS___MISSING_DATA_TAB,
        ORDER_INTERPOLATE_METHOD_CARD___CONTROLS___MISSING_DATA_TAB,
        DURATION_CARD___CONTROLS___MISSING_DATA_TAB,
        html.H5(
            className="text-center pb-2 pt-4",
            children="نحوه اعمال تغییرات",
            style={
                "color": "#2c8cff",
                "font-size": "1.3rem",
                "font-weight": "bold",
                "font-weight": 300,
            }
        ),
        HOW_MODIFY_CARD___CONTROLS___MISSING_DATA_TAB,
        html.Div(
            className="text-center pt-4",
            children=[
                BUTTON___BUTTONS___MISSING_DATA_TAB,
                TOAST___BUTTONS___MISSING_DATA_TAB                
            ]
        )       
    ]
)