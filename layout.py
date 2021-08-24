import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq

from figures import scatter_fig, line_fig, pie_fig

from data import sentiment

layout = html.Div([
    # Left
    html.Div(className="inline-block w-1/12 bg-white",),
    # Middle
    html.Div([
        html.Div([
            # Header
            html.Div([
                html.Div("Dashboard", className="lg-text"),
                html.Div("Updated as of xxxx", className="sm-text")
            ], className="flex flex-col  mb-6"),

            # Trends Boxes
            html.Div([
                html.Div(
                    html.Div([
                        html.Div("Uptrend - Blueskies", className="sm-text"),
                        html.Div(
                            "78", className="text-5xl pt-2 pb-2 card-body"),
                        html.Div([
                            html.Div([
                                html.Img(src="./assets/up.svg",
                                         className="w-2 h-3")
                            ], className="bg-green-300 w-4 h-4 rounded-full flex items-center justify-center"),
                            html.Div(
                                "+", className="text-sm", style={'color': '#1BCA8E', 'fontFamily': 'Roboto'}),
                            html.Div("69.12%", className="text-sm",
                                     style={'color': '#1BCA8E', 'fontFamily': 'Roboto'})
                        ], className="flex space-x-1 items-center flex-row"),
                    ], className="flex flex-col items-center"), className="card bg-white"),


                html.Div(
                    html.Div([
                        html.Div("Uptrend - Retrace", className="sm-text"),
                        html.Div(
                            "78", className="text-5xl pt-2 pb-2 card-body"),
                        html.Div([
                            html.Div([
                                html.Img(src="./assets/up.svg",
                                         className="w-2 h-3")
                            ], className="bg-green-300 w-4 h-4 rounded-full flex items-center justify-center"),
                            html.Div(
                                "+", className="text-sm", style={'color': '#1BCA8E', 'fontFamily': 'Roboto'}),
                            html.Div("69.12%", className="text-sm",
                                     style={'color': '#1BCA8E', 'fontFamily': 'Roboto'})
                        ], className="flex space-x-1 items-center flex-row"),
                    ], className="flex flex-col items-center"), className="card bg-white"),

                html.Div(
                    html.Div([
                        html.Div("Sideways - Reset", className="sm-text"),
                        html.Div(
                            "78", className="text-5xl pt-2 pb-2 card-body"),
                        html.Div([
                            html.Div([
                                html.Img(src="./assets/up.svg",
                                         className="w-2 h-3")
                            ], className="bg-green-300 w-4 h-4 rounded-full flex items-center justify-center"),
                            html.Div(
                                "+", className="text-sm", style={'color': '#1BCA8E', 'fontFamily': 'Roboto'}),
                            html.Div("69.12%", className="text-sm",
                                     style={'color': '#1BCA8E', 'fontFamily': 'Roboto'})
                        ], className="flex space-x-1 items-center flex-row"),
                    ], className="flex flex-col items-center"), className="card bg-white"),

                html.Div(
                    html.Div([
                        html.Div("Sideways - Reversal", className="sm-text"),
                        html.Div(
                            "78", className="text-5xl pt-2 pb-2 card-body"),
                        html.Div([
                            html.Div([
                                html.Img(src="./assets/up.svg",
                                         className="w-2 h-3")
                            ], className="bg-green-300 w-4 h-4 rounded-full flex items-center justify-center"),
                            html.Div(
                                "+", className="text-sm", style={'color': '#1BCA8E', 'fontFamily': 'Roboto'}),
                            html.Div("69.12%", className="text-sm",
                                     style={'color': '#1BCA8E', 'fontFamily': 'Roboto'})
                        ], className="flex space-x-1 items-center flex-row"),
                    ], className="flex flex-col items-center"), className="card bg-white"),

                html.Div(
                    html.Div([
                        html.Div("Downtrend", className="sm-text"),
                        html.Div(
                            "78", className="text-5xl pt-2 pb-2 card-body"),
                        html.Div([
                            html.Div([
                                html.Img(src="./assets/up.svg",
                                         className="w-2 h-3")
                            ], className="bg-green-300 w-4 h-4 rounded-full flex items-center justify-center"),
                            html.Div(
                                "+", className="text-sm", style={'color': '#1BCA8E', 'fontFamily': 'Roboto'}),
                            html.Div("69.12%", className="text-sm",
                                     style={'color': '#1BCA8E', 'fontFamily': 'Roboto'})
                        ], className="flex space-x-1 items-center flex-row"),
                    ], className="flex flex-col items-center"), className="card bg-white"),

            ], className="flex flex-row justify-between mb-5"),

            # Scatter Plots
            html.Div([

                html.Div([
                    html.Div("Scatter (2d x 7d)", className="md-text"),
                    html.Div([
                        dcc.Graph(
                            id="scatter-2d-vs-7d",
                            figure=scatter_fig,
                        )], className=" flex-grow rounded-lg shadow-md bg-white"),
                ], className=" flex flex-col w-full h-144"),


            ], className="flex flex-row space-x-4 mb-5 "),

            # Trends of Trends and Sentiment
            html.Div([

                # Trend of Trends
                html.Div([
                    html.Div([
                        html.Div("Pie of Trends", className="md-text"),
                        html.Div([
                             dcc.Graph(
                                 id="pie-trend-of-trends",
                                 figure=pie_fig
                             )], className="flex-grow rounded-lg shadow-md bg-white"),
                    ], className="flex flex-col w-1/2 h-80"),

                    html.Div([
                        html.Div("Sentiment Gauge", className="md-text"),
                        html.Div([

                            daq.Gauge(
                                id="sentiment-gauge",
                                label=" ",
                                color={"gradient": True, "ranges": {
                                    "red": [0, 50], "yellow":[50, 75], "green":[75, 100]}},
                                showCurrentValue=True,
                                value=sentiment['bullish'] / \
                                (sentiment['bullish'] + \
                                 sentiment['bearish'])*100,
                                min=0,
                                max=100,

                            )], id="gaugeeee", className="flex-grow rounded-lg shadow-md bg-white pt-5", style={'height': 280}),

                    ], className="flex flex-col w-1/2 h-80")

                ], className="flex flex-row w-1/2 space-x-4 h-80 "),

                html.Div([
                    html.Div("Trend of Trends", className="md-text"),
                    html.Div([
                        dcc.Graph(
                            id='line-trend-of-trends',
                            figure=line_fig
                        )], className="flex-grow rounded-lg shadow-md bg-white"),
                ], className="flex flex-col w-1/2 h-80")


            ], className="flex flex-row space-x-4 h-80"),
        ], className="mt-8 mb-8")


    ], id="MIDDLE", className="flex flex-col w-11/12 pl-24 pr-24 bg-frame-gray"),

    # Right
    # html.Div(className="inline-block w-1/12 bg-white"),


], className="flex flex-row h-screen",)


print("success")
