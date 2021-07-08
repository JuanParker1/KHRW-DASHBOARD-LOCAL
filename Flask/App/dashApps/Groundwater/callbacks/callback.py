from App.dashApps.Groundwater.callbacks.callback_home import groundwater_callback_home
from App.dashApps.Groundwater.callbacks.callback_tab1 import groundwater_callback_tab1
from App.dashApps.Groundwater.callbacks.callback_tab2 import groundwater_callback_tab2
from App.dashApps.Groundwater.callbacks.callback_tab3 import groundwater_callback_tab3

def groundwater_callback(app):
    groundwater_callback_home(app=app)
    groundwater_callback_tab1(app=app)
    groundwater_callback_tab2(app=app)
    groundwater_callback_tab3(app=app)