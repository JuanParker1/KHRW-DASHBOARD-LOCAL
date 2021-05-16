from App.dashApp.hydrograph.callbacks.callback_tab1 import hydrograph_callback_tab1
from App.dashApp.hydrograph.callbacks.callback_tab2 import hydrograph_callback_tab2
from App.dashApp.hydrograph.callbacks.callback_tab3 import hydrograph_callback_tab3

def hydrograph_callback(app):
    hydrograph_callback_tab1(app=app)
    hydrograph_callback_tab2(app=app)
    hydrograph_callback_tab3(app=app)