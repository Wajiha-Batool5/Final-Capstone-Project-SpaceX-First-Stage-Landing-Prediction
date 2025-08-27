# Import required libraries
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("dataset_part_3.csv")
class_df = pd.read_csv("dataset_part_2.csv")[['FlightNumber', 'Class']]
spacex_df = pd.merge(spacex_df, class_df, on='FlightNumber')
max_payload = spacex_df['PayloadMass'].max()
min_payload = spacex_df['PayloadMass'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(
    style={'backgroundColor': '#F5F5F5', 'padding': '20px'},
    children=[
        html.H1(
            'SpaceX Launch Records Dashboard',
            style={
                'textAlign': 'center',
                'color': '#1a237e',
                'fontSize': 40,
                'marginBottom': '30px'
            }
        ),
        html.Div([
            html.Label('Select Launch Site:', style={'fontWeight': 'bold', 'color': '#333'}),
            dcc.Dropdown(
                id='site-dropdown',
                options=[
                    {'label': 'All Sites', 'value': 'ALL'},
                    {'label': 'CCAFS SLC 40', 'value': 'CCAFS SLC 40'},
                    {'label': 'KSC LC 39A', 'value': 'KSC LC 39A'},
                    {'label': 'VAFB SLC 4E', 'value': 'VAFB SLC 4E'}
                ],
                value='ALL',
                placeholder='Select a Launch Site here',
                searchable=True,
                style={'marginBottom': '20px'}
            ),
        ], style={'maxWidth': '500px', 'margin': 'auto'}),
        html.Br(),
        html.Div([
            dcc.Graph(id='success-pie-chart')
        ], style={'backgroundColor': '#fff', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0 2px 8px #aaa', 'maxWidth': '800px', 'margin': 'auto'}),
        html.Br(),
        html.Div([
            html.Label("Payload range (Kg):", style={'fontWeight': 'bold', 'color': '#333'}),
            dcc.RangeSlider(
                id='payload-slider',
                min=0,
                max=10000,
                step=1000,
                value=[min_payload, max_payload],
                marks={i: str(i) for i in range(0, 10001, 2000)},
                tooltip={"placement": "bottom", "always_visible": True}
            ),
        ], style={'maxWidth': '800px', 'margin': 'auto', 'marginBottom': '20px'}),
        html.Div([
            dcc.Graph(id='success-payload-scatter-chart')
        ], style={'backgroundColor': '#fff', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0 2px 8px #aaa', 'maxWidth': '800px', 'margin': 'auto'}),
    ]
)

# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, names='Class', title='Total Success vs Failure Launches')
        return fig
    else:
        site_col = f'LaunchSite_{entered_site}'
        filtered_df = spacex_df[spacex_df[site_col] == True]
        fig = px.pie(filtered_df, names='Class', title=f'Success vs Failure for site {entered_site}')
        return fig


# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart',component_property='figure'),
                [Input(component_id='site-dropdown',component_property='value'),
                Input(component_id='payload-slider',component_property='value')])
def scatter(entered_site, payload):
    filtered_df = spacex_df[(spacex_df['PayloadMass'] >= payload[0]) & (spacex_df['PayloadMass'] <= payload[1])]
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='PayloadMass', y='Class', color='FlightNumber', title='Correlation between Payload and Success for all Sites')
        return fig
    else:
        site_col = f'LaunchSite_{entered_site}'
        filtered_df = filtered_df[filtered_df[site_col] == True]
        fig = px.scatter(filtered_df, x='PayloadMass', y='Class', color='FlightNumber', title=f'Correlation between Payload and Success for site {entered_site}')
        return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)