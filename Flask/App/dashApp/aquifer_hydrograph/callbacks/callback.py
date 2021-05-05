from App.dashApp.aquifer_hydrograph.callbacks.callback_tab1 import aquifer_hydrograph_callback_tab1
from App.dashApp.aquifer_hydrograph.callbacks.callback_tab2 import aquifer_hydrograph_callback_tab2
from App.dashApp.aquifer_hydrograph.callbacks.callback_tab3 import aquifer_hydrograph_callback_tab3

def aquifer_hydrograph_callback(app):
    aquifer_hydrograph_callback_tab1(app=app)
    aquifer_hydrograph_callback_tab2(app=app)
    aquifer_hydrograph_callback_tab3(app=app)
    