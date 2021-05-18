from callbacks.callback import *
from server import app
from layouts.main import MAIN_LAYOUT

app.layout = MAIN_LAYOUT


if __name__ == '__main__':
    app.run_server(
        host='127.0.0.1',
        port='8010',
        debug=True
    )
