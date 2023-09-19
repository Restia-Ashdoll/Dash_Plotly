import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html

def plotgraph(columns, colors, df):
    # Create a list to hold dcc.Graph components
    graph_list = []

    for i, column in enumerate(columns):
        x_rows = df["Time Stamp"]
        y_values = df[column]

        trace = go.Scatter(x=x_rows, y=y_values, mode="lines", name=column, line={"color": colors[i]})
        layout = go.Layout(title=f"{column} VOLTAGE")

        graph = dcc.Graph(id=f'lineplot-{i}', figure={'data': [trace], 'layout': layout})
        graph_list.append(graph)

    return graph_list