import dash
from layout import layout

app = dash.Dash(__name__)

app.layout = layout

app.run_server()
