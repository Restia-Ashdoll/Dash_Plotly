import dcc
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from functions import plotgraph


app = dash.Dash()

df = pd.read_csv("guardbandcore-6.csv")

# Specify the columns you want to plot and their corresponding colors
columns_to_plot = ["CPU0 CORES CORE1 Voltage"]
colors = ["rgb(255, 0, 255)", "rgb(200, 51, 53)"]

#graph_list = plotgraph(columns_to_plot, colors, df)

options = []
for option in df.columns:
    options.append(option)

app.layout = html.Div([
    dcc.Graph(id='graph'), dcc.Dropdown(id='drop', options=options, value=df.columns[1])
])

@app.callback(Output('graph','figure'),
              [Input('drop', 'value')])
def update(selected_column):
    filtered_df = df[selected_column]

    trace = []
    trace.append(go.Scatter(
        x = df['Time Stamp'],
        y = filtered_df,
        mode='lines',
        line = {'color' : 'rgb(255,0,255)'},
        name = 'linegraph'
    ))


    return {'data' : trace,'layout':go.Layout(title='myplot')}

if __name__ == "__main__":
    app.run_server()


