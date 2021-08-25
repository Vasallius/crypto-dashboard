from data import revised, dates
from data import bluesky, retrace, reset, reversal, downtrend, lacking_data
import plotly.express as px
import plotly.graph_objects as go


# === Colors ===


ToT_mapper = {
    "bluesky": "#60A5FA",
    "retrace": "#059669",
    "reset": "#F59E0B",
    "reversal": "#92400E",
    "downtrend": "#DC2626"
}


# === Scatter Plot ===


scatter_fig = px.scatter(revised, x='2D Δ', y='7D Δ',
                         color="RSI", color_continuous_scale="Rainbow")
scatter_fig.update_traces(
    mode="markers+text",
    text=revised['Symbol'],
    textposition="top left",
    textfont_size=10,
)
scatter_fig.update_layout(
    xaxis=dict(
        title="2 Day Change",
        visible=True,
        showgrid=False,
        tick0=0,
        dtick=0.25,
        tickformat=',.0%',
    ),
    yaxis=dict(
        title="7 Day Change",
        visible=True,
        showgrid=False,
        tick0=0,
        dtick=0.25,
        tickformat=',.0%',
    ),
    plot_bgcolor="#FFFFFF",
    margin=dict(
        l=20,
        r=20,
        t=30,
        b=20),
    height=548,
)


# === Trend of Trends (Line)===


line_data = []
for trend, color in ToT_mapper.items():
    scatter_chart = go.Scatter(
        x=dates,
        y=eval(trend),
        marker_color=color,
        name=trend,
        mode="lines+markers"
    )
    line_data.append(scatter_chart)

line_layout = go.Layout(
    margin=dict(
        l=20,
        r=20,
        t=30,
        b=20
    ),
    plot_bgcolor="#FFF",
    xaxis=dict(
        visible=False,
        showgrid=False
    ),
    yaxis=dict(
        tick0=0,
        dtick=0.25,
        tickformat=',.0%',
        showgrid=False,
        linecolor="#BCCCDC"
    ),
    height=280
)


line_fig = go.Figure(
    data=line_data,
    layout=line_layout
)


# === Trend of Trends (Pie) ===


colors = ["#60A5FA", "#059669", "#F59E0B", "#92400E", "#DC2626"]
lacking = 1-bluesky[-1]-retrace[-1]-reset[-1]-reversal[-1]-downtrend[-1]
trends = ["Uptrend - Blueskies", "Uptrend - Retrace", "Sideways - Reset",
          "Sideways - Reversal", "Downtrend", "New / Not Enough Data"]


pie_trends = [bluesky[-1], retrace[-1], reset[-1],
              reversal[-1], downtrend[-1], lacking]
pie_fig = px.pie(names=trends, values=pie_trends)
pie_fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
pie_fig.update_layout(height=280)
pie_fig.update_traces(hoverinfo='label+percent', textfont_size=16,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))

print("Figures.py successfully loaded.")
