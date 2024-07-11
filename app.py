# Import necessary libraries
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


# Create a Dash app
app = Dash(__name__)

# Load the data
df = pd.read_csv('data/daily_sales_conv.csv', parse_dates=['date'])
# Sort the data by date
df.sort_values('date', inplace=True)

# Create a line plot
labels = {'sales': 'Sales (USD)', 'date': 'Date', 'region': 'Region'}
annotation_dict = dict(
    x='2021-01-15',
    y=1900,
    xref='x',
    yref='y',
    text='15th of January, 2021',
    showarrow=True,
    arrowhead=5,
    ax=-70,
    ay=-40,
)
fig = px.line(df, x="date", y="sales", line_group='region', labels=labels)
# Add an annotation marking the 15th of January 2021
fig.update_layout(annotations=[annotation_dict])


# Update the layout of the app
app.layout = html.Div([
    # Add a title
    html.H1('Pink Morsel Sales'),

    dcc.Graph(
        id='pink-morsel-graph',
        figure=fig
    )
], style={'textAlign': "center"})


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
