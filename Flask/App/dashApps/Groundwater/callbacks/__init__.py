from App.dashApps.Groundwater.callbacks.home_tab import groundwater_callback_home_tab
from App.dashApps.Groundwater.callbacks.settings_tab import groundwater_callback_settings_tab
from App.dashApps.Groundwater.callbacks.callback_tab1 import groundwater_callback_tab1
from App.dashApps.Groundwater.callbacks.callback_tab2 import groundwater_callback_tab2
from App.dashApps.Groundwater.callbacks.callback_tab3 import groundwater_callback_tab3

def groundwater_callback(app):
    groundwater_callback_home_tab(app=app)
    # groundwater_callback_settings_tab(app=app)
    # groundwater_callback_tab1(app=app)
    # groundwater_callback_tab2(app=app)
    # groundwater_callback_tab3(app=app)