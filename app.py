# Import necessary libraries
from dash import Dash, html, dcc, Input, Output, callback
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

# Update the layout of the app
app.layout = html.Div([
    # Add a title
    html.H1('Pink Morsel Sales', style={'textAlign': "center"}),

    dcc.Graph(id='pink-morsel-graph'),
    # Add a radio button with options to select the region
    html.Label('Select Region', style={'fontWeight': 'bold', 'fontSize': 20}),
    dcc.RadioItems(
        id='region-radio',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'},
            {'label': 'North', 'value': 'north'},
            {'label': 'South', 'value': 'south'}
        ],
        value='all',
        labelStyle={'display': 'inline'}
    )
])

# Add a callback to update the graph based on the selected region
@callback(
    Output('pink-morsel-graph', 'figure'),
    Input('region-radio', 'value')
)
def update_graph(region):
    filtered_df = df[df['region'] == region] if region != 'all' else df

    fig = px.line(filtered_df, x="date", y="sales", labels=labels)
    fig.update_layout(annotations=[annotation_dict])
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
