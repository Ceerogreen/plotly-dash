# %%
import dash
from dash import Dash, html, dcc, Input, Output, callback # Import dependencies
import pandas as pd
import plotly.express as px

# %%
stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] # Get stylesheets

# %%
data = pd.read_csv('data.csv') # import data
data.drop('Unnamed: 0', axis=1, inplace=True)

# %%
FourFactors = ['EFG%', 'EFG%D', 'FTR','FTRD', 'TOV%', 'TOV%D', 'OREB%', 'DREB%'] # Define the four factors
data['Round Made'] = data['ROUND'].astype(str)

# %%
teams = data['TEAM'].unique()
teams = sorted(teams)

# %%
dash.register_page(__name__)

# %%
layout = html.Div([
    html.Div([ # Create Title
        html.Div([
            html.H1('''Team Statistics''')
        ], style={'display':'flex', 'justifyContent':'center','backgroundColor':'#F99C58'}),
    ], className = 'row', style={'display':'flex', 'justifyContent':'center','backgroundColor':'#F99C58'}),
    html.Div([ # Explanatory Paragraph and Dropdown
        html.Div(children = [
                html.H6('''This page is designed to allow for the analysis of historical March Madness data based on team. Start by selecting a team through the search box. The graph on the left provides an historical representation of the team's March Madness performance; A year without a point is a year they missed the tournament. Note that 2020 is excluded due to the Coronavirus leading to the cancellation of the NCAA Tournament. The graph on the right is affected by the two dropdowns, which can select any of the Four Factors that are determined to be the biggest predictors of success in basketball.''')
        ], className= 'nine columns', style={'display':'flex', 'justifyContent':'center'}),
        html.Div([
            html.H5('''Team:'''),
            dcc.Dropdown( # Create team dropdown
                id = 'TeamDrop',
                options = teams,
                value = 'Virginia'
            ),
            html.H5('''Four Factors:'''),
            dcc.Dropdown( # Create First Four Factor Dropdown
                id = 'FourFactors3',
                options = FourFactors,
                value = 'EFG%',
            ),
            dcc.Dropdown( # Create Second Four Factor Dropdown
                id = 'FourFactors4',
                options = FourFactors,
                value = 'EFG%D',
            )
        ], className= 'three columns')
    ], className = 'row', style={'display':'flex', 'justifyContent':'center','backgroundColor':'#7092F4','padding':'10px'}),
    html.Div([ # Contain row with graphs
        html.Div(# Create first graph
            dcc.Graph(
                id = 'Graph2a'
            ), className = 'six columns'),
        html.Div(# Create second graph
            dcc.Graph(
                id = 'Graph2b'
            ), className = 'six columns')
    ], className='row', style={'backgroundColor':'#D3D3D3'})
])

@callback( # Create callback to update first graph
    Output('Graph2a', 'figure'),
    Input('TeamDrop', 'value'),
)
def update_Graph2a(team):
    team_data = data[data['TEAM'] == team] # Take data for specific team
    newdata = pd.DataFrame()
    years = list(range(2007,2024))
    years.remove(2020)
    newdata['YEAR'] = years
    newdata = newdata.merge(team_data, on='YEAR', how='left') # Get data for that team on all years
    newdata = newdata.fillna('Out') # Impute missing data as out of tournament
    newdata[['YEAR','Round Made']]

    new2 = newdata['Round Made'].value_counts() # Create dataframe with value counts for pie chart
    newdf = new2.to_frame()
    years = []
    newdf.reset_index(inplace=True)
    for i in newdf['Round Made']: # Create list of years at specific Round Made
        years.append(newdata.where(newdata['Round Made'] == i)['YEAR'].dropna().values.tolist())
    newdf['years'] = years
    fig = px.pie(newdf, # Create pie chart of team performance
        values = 'count',
        names = 'Round Made',
        hover_data = dict(years = True),
        category_orders={'Round Made': ['Out','68','64','32','16','8','4','2','1']},
        title = team + '\'s Performance Distribution'
    )
    fig.update_layout(title_x=0.5, plot_bgcolor='#D3D3D3', paper_bgcolor='#D3D3D3') # Match format
    return fig



@callback( # Callback to update the second figure
    Output('Graph2b', 'figure'),
    Input('FourFactors3', 'value'),
    Input('FourFactors4', 'value'),
    Input('TeamDrop','value')
)
def update_Graph2b(x_dropdown,y_dropdown,team):
    year_data = data[data['TEAM'] == team] # Filter by team
    fig = px.scatter(year_data, # Scatter requested x and y data
                     x = x_dropdown,
                     y = y_dropdown,
                     color = 'Round Made',
                     category_orders={'Round Made': ['68','64','32','16','8','4','2','1']},
                     hover_data = {x_dropdown: False,
                                y_dropdown: False,
                                'TEAM': True,
                                'SEED': True,
                                'YEAR':True}, 
                     title = x_dropdown + ' vs. ' + y_dropdown
                                )
    fig.update_layout(title_x=0.5, plot_bgcolor='#D3D3D3', paper_bgcolor='#D3D3D3')
    return fig



# %%

