import dash
import os
# from layout import layout1
import dash_html_components as html

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([

    # === Navbar ===
    html.Div([

        html.Div([
            html.Img(src="./assets/logo.svg"),
            html.Img(src="./assets/dashboard.svg"),
            html.Img(src="./assets/gear.svg"),
            html.Img(src="./assets/alerts.svg")
        ], className="flex flex-col items-center justify-between",
            style={
            'height': '245px',
            'marginTop': '28px'
        })

    ],
        className="h-screen ",
        style={
            'width': 76,
            'background': 'linear-gradient(180deg, #E30F0F 0%, #150202 0.01%, rgba(0, 0, 0, 0) 100%)',
            'boxShadow': '4px 0px 20px 0px #0000005E',
            'marginRight': '38px'

    }),
    html.Div([

        # === Dashboard Title ===
        html.Div([
            html.Div("Dashboard",
                     className="font-my-font gradient-text gradient-color",
                     style={
                         'paddingTop': '6px',
                         'marginLeft': '-4px',
                     }),

            html.Div("Updated as of August 27, 2020 1:33 PM",
                     style={
                         'fontSize': '16px',
                         'fontFamily': 'Roboto',
                         'color': '#E5E5E5',
                         'lineHeight': '100%',
                         'fontWeight': 300,


                     })
        ], className="flex flex-col",
            style={
            'height': 88,
            'width': 388,
            'marginTop': '27px'
        }),

        # === Content ===

        html.Div([

            # === Left ===

            html.Div([

                # === Trend Counters ===

                html.Div([
                    html.Div("1",
                             style={'borderRadius': '10px', 'background': '#170C1B'}),
                    html.Div("2",
                             style={'borderRadius': '10px', 'background': '#170C1B'}),
                    html.Div("3",
                             style={'borderRadius': '10px', 'background': '#170C1B'}),
                    html.Div("4",
                             style={'borderRadius': '10px', 'background': '#170C1B'}),
                    html.Div("5",
                             style={'borderRadius': '10px', 'background': '#170C1B'}),
                    html.Div("6",
                             style={'borderRadius': '10px', 'background': '#170C1B'}),
                ], className="flex-grow grid grid-cols-2 gap-4",
                    style={
                    'marginBottom': '24px'
                }),

                # === Sentiment Gauge ===

                html.Div("Sentiment Gauge",

                         style={
                             'height': '358px',
                             'borderRadius': '10px',
                             'paddingLeft': '15px',
                             'paddingTop': '10px',
                             'fontFamily': 'my-font',
                             'fontSize': '20px',
                             'color': '#BBB7E0',
                             'background': '#170C1B'

                         })

            ], className="flex flex-col",
                style={
                'width': '273px',
            }
            ),

            # === Middle ===

            html.Div([

                # === Scatter Plot ===

                html.Div("Scatter (2d x 7d)",
                         className="flex-grow",
                         style={
                             'marginBottom': '24px',
                             'borderRadius': '10px',
                             'paddingLeft': '15px',
                             'paddingTop': '10px',
                             'fontFamily': 'my-font',
                             'fontSize': '20px',
                             'color': '#BBB7E0',
                             'background': '#170C1B'
                         }),


                # === Filter ===

                html.Div("Filter",

                         style={
                             'height': '133px',
                             'borderRadius': '10px',
                             'paddingLeft': '15px',
                             'paddingTop': '10px',
                             'fontFamily': 'my-font',
                             'fontSize': '20px',
                             'color': '#BBB7E0',
                             'background': '#170C1B'

                         })
            ], className=" flex flex-col", style={'width': '947px'}),

            # === Right ===

            html.Div([
                html.Div("Trend of Trends",
                         className="flex-grow",
                         style={
                             'marginBottom': '24px',
                             'borderRadius': '10px',
                             'paddingLeft': '15px',
                             'paddingTop': '10px',
                             'fontFamily': 'my-font',
                             'fontSize': '20px',
                             'color': '#BBB7E0',
                             'background': '#170C1B'
                         }),

                html.Div("IRKZ Candidates",

                         style={
                             'height': '547px',
                             'borderRadius': '10px',
                             'paddingLeft': '15px',
                             'paddingTop': '10px',
                             'fontFamily': 'my-font',
                             'fontSize': '20px',
                             'color': '#BBB7E0',
                             'background': '#170C1B'
                         })
            ], className="flex flex-col", style={'width': '516px'})

        ],
            className="flex flex-row h-full space-x-5",
            style={
            'marginTop': '32px',
            'marginBottom': '27px'
        }
        )


    ],
        className=" flex-grow flex flex-col",
        style={'background': '#1D1D3E'})


], className="flex flex-row", style={'background': '#1D1D3E'})

# PORT = os.environ.get('PORT')
PORT = 6969

if __name__ == '__main__':
    app.run_server(debug=True, port=PORT)
