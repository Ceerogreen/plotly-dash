# %%
from dash import Dash, html, dcc, Input, Output, callback # Import dependencies
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import plotly.tools as tls 
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# %%
stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] # Get stylesheets

# %%
data = pd.read_csv('data.csv') # import data
data.drop('Unnamed: 0', axis=1, inplace=True)

# %%
teams = data['TEAM'] # Makes image references for all teams
data['path'] = ['logos/' + x + '.png' for x in teams]
unique_teams = data['TEAM'].unique()
team_paths = ['logos/' + i + '.png' for i in unique_teams]
path_dict = dict(zip(unique_teams,team_paths))

# %%
FourFactors = ['EFG%', 'EFG%D', 'FTR','FTRD', 'TOV%', 'TOV%D', 'OREB%', 'DREB%'] # Define the four factors
data['Round Made'] = data['ROUND'].astype(str)

# %%
app = Dash(__name__,external_stylesheets=stylesheets)
server = app.server # Make app accessible as server for Render

# %%
SliderMarks={ # Create slider marks
        2008: {'label': '2008'},
        2009: {'label': '2009', 'style': {'opacity': '0'}},
        2010: {'label': '2010', 'style': {'opacity': '0'}},
        2011: {'label': '2011', 'style': {'opacity': '0'}},
        2012: {'label': '2012', 'style': {'opacity': '0'}},
        2013: {'label': '2013', 'style': {'opacity': '0'}},
        2014: {'label': '2014', 'style': {'opacity': '0'}},
        2015: {'label': '2015', 'style': {'opacity': '0'}},
        2016: {'label': '2016', 'style': {'opacity': '0'}},
        2017: {'label': '2017', 'style': {'opacity': '0'}},
        2018: {'label': '2018', 'style': {'opacity': '0'}},
        2019: {'label': '2019', 'style': {'opacity': '0'}},
        2021: {'label': '2021', 'style': {'opacity': '0'}},
        2022: {'label': '2022', 'style': {'opacity': '0'}},
        2023: {'label': '2023'}}

# %%
app.layout = html.Div([
    html.Div([ # Create Title and Explanatory Paragraph
        html.Div([
            html.H1('''March Madness Overview''')
        ], style={'display':'flex', 'justifyContent':'center','backgroundColor':'#F99C58'}),
        html.Div([
            html.H6('''This app is designed to allow for the analysis of historical March Madness data. The graph on the left provides an efficiency matrix, with Adjusted Offense on the x-axis and Adjusted Defense on the y-axis. A higher ADJ O and lower ADJ D is better. This metric can be either KenPom or BartTorvik, selectable above it. Additionally, the year can be changed by the slider, which affects both graphs. Data exists from 2008 to 2023, with 2020 being excluded due to the Coronavirus leading to the cancellation of the NCAA Tournament. The graph on the right is affected by the two dropdowns, which can select any of the Four Factors that are determined to be the biggest predictors of success in basketball.''')
        ], style={'display':'flex', 'justifyContent':'center','backgroundColor':'#7092F4'})
        # need to add a description later
    ]),
    html.Div(children = [# Contain row with radio and dropdowns
        html.Div(children = [ # Contain radio
            dcc.RadioItems( # Create Radio for Graph 1
                id = 'KPvBT',
                options = ['KenPom','Bart Torvik'],
                value='KenPom',
                inline = True
            )
        ], className = 'three columns', style={'display':'flex', 'justifyContent':'center'}),
        html.Div(children=[ # Create a slider to select the year of the data being displayed
            dcc.Slider(
                data['YEAR'].min(),
                data['YEAR'].max(),
                id = 'YearSlider1',
                step = None,
                value = data['YEAR'].min(),
                marks = SliderMarks,
                tooltip={'placement':'top'}
            )
        ], className = 'three columns'),
        html.Div(children = [
            dcc.Dropdown( # Create First Dropdown
                id = 'FourFactors1',
                options = FourFactors,
                value = 'EFG%',
            )
        ], className = 'three columns'),
        html.Div(children = [
            dcc.Dropdown( # Create First Dropdown
                id = 'FourFactors2',
                options = FourFactors,
                value = 'EFG%D'
            )
        ], className = 'three columns')
    ], className='row', style={'backgroundColor':'#D3D3D3'}),
    html.Div([ # Contain row with graphs
        html.Div(# Create first graph
            dcc.Graph(
                id = 'Graph1a'
            ), className = 'six columns'),
        html.Div(# Create second graph
            dcc.Graph(
                id = 'Graph1b'
            ), className = 'six columns')
    ], className='row', style={'backgroundColor':'#D3D3D3'})
])

@callback( # Create callback to update first graph
    Output('Graph1a', 'figure'),
    Input('KPvBT', 'value'),
    Input('YearSlider1','value')
)
def update_Graph1a(radio_value,slider_value):
    year_data = data[data['YEAR'] == slider_value]
    if radio_value == 'Bart Torvik':
        fig = px.scatter(year_data, # Scatter year data with BartTorvik stats
            x = 'BADJ O',
            y= 'BADJ D',
            hover_data = {'BADJ O': False,
                          'BADJ D': False,
                          'TEAM': True,
                          'SEED': True,
                          'Round Made': True},
            title='Efficiency Matrix'
        )
        for i, row in year_data.iterrows(): # Put image on respective dot
            logo = Image.open(row['path'])
            fig.add_layout_image(
                dict(
                    source = logo,
                    xref = 'x',
                    yref = 'y',
                    xanchor = 'center',
                    yanchor = 'middle',
                    x = row['BADJ O'],
                    y = row['BADJ D'],
                    sizex=2.4,
                    sizey=2.4,
                    opacity = 0.8,
                    layer = 'above'
                )
            )  
    else:
        fig = px.scatter(year_data, # Scatter year data with KenPom stats
            x = 'KADJ O',
            y= 'KADJ D',
            hover_data = {'KADJ O': False,
                          'KADJ D': False,
                          'TEAM': True,
                          'SEED':True,
                          'Round Made':True},
            title = 'Efficiency Matrix'
        )
        for i, row in year_data.iterrows():
            logo = Image.open(row['path'])
            fig.add_layout_image(
                dict(
                    source = logo,
                    xref = 'x',
                    yref = 'y',
                    xanchor = 'center',
                    yanchor = 'middle',
                    x = row['KADJ O'],
                    y = row['KADJ D'],
                    sizex=2.3,
                    sizey=2.3,
                    opacity = 0.8,
                    layer = 'above'
                )
            )
    fig.update_traces(marker=dict(opacity = 0)) # Make markers invisible
    fig.update_layout(title_x=0.5, plot_bgcolor='#D3D3D3', paper_bgcolor='#D3D3D3')
    return fig



@callback( # Callback to update the second figure
    Output('Graph1b', 'figure'),
    Input('FourFactors1', 'value'),
    Input('FourFactors2', 'value'),
    Input('YearSlider1','value')
)
def update_Graph1b(x_dropdown,y_dropdown,slider_value):
    year_data = data[data['YEAR'] == slider_value] # Filter by year
    scalex = (year_data[x_dropdown].max() - year_data[x_dropdown].min()) / 10 # Create scale for image sizes
    scaley = (year_data[y_dropdown].max() - year_data[y_dropdown].min()) / 10
    fig = px.scatter(year_data, # Scatter requested x and y data
                     x = x_dropdown,
                     y = y_dropdown,
                     hover_data = {x_dropdown: False,
                                y_dropdown: False,
                                'TEAM': True,
                                'SEED': True,
                                'Round Made':True}, 
                     title = x_dropdown + ' vs. ' + y_dropdown
                                )
    
    for i, row in year_data.iterrows(): # Assign image to marker
        logo = Image.open(row['path'])
        fig.add_layout_image(
            dict(
                source = logo,
                xref = 'x',
                yref = 'y',
                xanchor = 'center',
                yanchor = 'middle',
                x = row[x_dropdown],
                y = row[y_dropdown],
                sizex=scalex,
                sizey=scaley,
                opacity = 0.8,
                layer = 'above'
            )
        )
    fig.update_traces(marker=dict(opacity = 0)) # Make markers invisible
    fig.update_layout(title_x=0.5, plot_bgcolor='#D3D3D3', paper_bgcolor='#D3D3D3')
    return fig



# %%
if __name__ == '__main__':
    app.run(debug=True, port=8049)


