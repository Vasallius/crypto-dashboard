import dash
from layout import layout

app = dash.Dash(__name__)

server = app.server

app.layout = layout

app.run_server()
