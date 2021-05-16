from App.dashApp.chemograph.callbacks.callback_tab1 import chemograph_callback_tab1
from App.dashApp.chemograph.callbacks.callback_tab2 import chemograph_callback_tab2
from App.dashApp.chemograph.callbacks.callback_tab3 import chemograph_callback_tab3


def chemograph_callback(app):
    chemograph_callback_tab1(app=app)
    chemograph_callback_tab2(app=app)
    chemograph_callback_tab3(app=app)