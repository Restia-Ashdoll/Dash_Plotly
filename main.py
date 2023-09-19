import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html
from functions import plotgraph


app = dash.Dash()

df = pd.read_csv("guardbandcore-6.csv")

# Specify the columns you want to plot and their corresponding colors
columns_to_plot = ["CPU0 CORES CORE1 Voltage"]
colors = ["rgb(255, 0, 255)", "rgb(200, 51, 53)"]

graph_list = plotgraph(columns_to_plot, colors, df)

app.layout = html.Div(graph_list)

if __name__ == "__main__":
    app.run_server()


