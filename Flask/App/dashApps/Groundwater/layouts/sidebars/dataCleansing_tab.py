# -----------------------------------------------------------------------------
# DATA CLEANSING TAB - BODY
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
STUDY_AREA_CARD___CONTROLS___DATA_CLEANSING_TAB = html.Div(
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
            id='STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)

# AQUIFER:
AQUIFER_CARD___CONTROLS___DATA_CLEANSING_TAB = html.Div(
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
            id='AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)

# WELL:
WELL_CARD___CONTROLS___DATA_CLEANSING_TAB = html.Div(
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
            id='WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)


# METHOD 1:
METHOD_1_CARD___CONTROLS___DATA_CLEANSING_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            className='text-center',
            dir='rtl', 
            children='- میانگین اختلاف ماهیانه 6 ماه اخیر بیشتر از',
            style={
                "font-weight": "bold",
                "font-size": "1rem",
            }
        ),
        dcc.Dropdown(
            id='METHOD_1_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
            placeholder='انتخاب ...',
            value=2,
            options=[{"label": f"{x}x", "value": x} for x in [i for i in range(1, 11)]],
            className="w-50 mx-auto",
            clearable=False
        ) 
    ]
)

# METHOD 2:
METHOD_2_CARD___CONTROLS___DATA_CLEANSING_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            className='text-center',
            dir='rtl', 
        children='- میانگین شیب خط ماهانه 6 ماه اخیر بیشتر از',
        style={
            "font-weight": "bold",
            "font-size": "1rem",
        }
        ),
        dcc.Dropdown(
            id='METHOD_2_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
            placeholder='انتخاب ...',
            value=2,
            options=[{"label": f"{x}%", "value": x} for x in [i for i in range(1, 11)]],
            className="w-50 mx-auto",
            clearable=False
        ) 
    ]
)



# -------------------------------------
# BUTTONS
# -------------------------------------

# BUTTON:
BUTTON___BUTTONS___DATA_CLEANSING_TAB = dbc.Button(
    id='BUTTON___BUTTONS___DATA_CLEANSING_TAB',
    className="me-1",
    size="lg",
    children='بروزرسانی پایگاه داده', 
    color='primary',
    n_clicks=0
)

# TOAST:
TOAST___BUTTONS___DATA_CLEANSING_TAB = dbc.Toast(
    id='TOAST___BUTTONS___DATA_CLEANSING_TAB',
    is_open=False,
    dismissable=True,
    duration=5000
)




# -------------------------------------
# SIDEBAR
# -------------------------------------

SIDEBAR___DATA_CLEANSING_TAB = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        html.H5(
            className="text-center pb-3",
            children="انتخاب چاه مشاهده‌ای",
            style={
                "color": "#2c8cff",
                "font-size": "1.3rem",
                "font-weight": "bold",
                "font-weight": 300,
            }
        ),
        STUDY_AREA_CARD___CONTROLS___DATA_CLEANSING_TAB,
        AQUIFER_CARD___CONTROLS___DATA_CLEANSING_TAB,
        WELL_CARD___CONTROLS___DATA_CLEANSING_TAB,
        html.H5(
            className="text-center py-3",
            children="تنظیم هشدار مقادیر بحرانی",
            style={
                "color": "#2c8cff",
                "font-size": "1.3rem",
                "font-weight": "bold",
                "font-weight": 300,
            }
        ),
        METHOD_1_CARD___CONTROLS___DATA_CLEANSING_TAB,
        METHOD_2_CARD___CONTROLS___DATA_CLEANSING_TAB,
        html.Div(
            className="text-center pt-5",
            children=[
                BUTTON___BUTTONS___DATA_CLEANSING_TAB,
                TOAST___BUTTONS___DATA_CLEANSING_TAB                
            ]
        )       
    ]
)