import dash
from layout import layout

app = dash.Dash(__name__)

server = app.server

app.layout = layout

PORT = os.environ.get('PORT')

if __name__ == '__main__':
    app.run_server(debug=False, port=PORT)
