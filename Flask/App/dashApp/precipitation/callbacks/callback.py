from App.dashApp.precipitation.callbacks.callback_tab1 import precipitation_callback_tab1
from App.dashApp.precipitation.callbacks.callback_tab2 import precipitation_callback_tab2
from App.dashApp.precipitation.callbacks.callback_tab3 import precipitation_callback_tab3


def precipitation_callback(app):
    precipitation_callback_tab1(app=app)
    precipitation_callback_tab2(app=app)
    precipitation_callback_tab3(app=app)