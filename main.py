import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo
import dash
from dash import dcc
from dash import html


app = dash.Dash()

df = pd.read_csv("guardbandcore-6.csv")

y_columns = df["CPU0 CORES CORE1 Voltage"]
x_rows = df["Time Stamp"]

trace = go.Scatter(x=x_rows,y=y_columns, mode="lines",name="lines")

data = [trace]

layout = go.Layout(title = "Line Chart")

fig = go.Figure(data=data, layout=layout)
fig.write_html("plot.html")

app.layout = html.Div([dcc.Graph(id="lineplot", figure = {"data" : data, "layout" : layout})])

if __name__ == "__main__":
    app.run_server()