# %%
import dash
from dash import Dash, html, dcc, Input, Output, callback, dash_table # Import dependencies
import pandas as pd

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
dash.register_page(__name__)

# %%
columns = list(data.columns) # Create list of possible columns
columns.remove('TEAM NO') # Remove TEAM NO, not helpful for user

# %%
layout = html.Div([
    html.Div([ # Create Title
        html.Div([
            html.H1('''Table Search''')
        ], style={'display':'flex', 'justifyContent':'center','backgroundColor':'#F99C58'}),
    ], className = 'row', style={'display':'flex', 'justifyContent':'center','backgroundColor':'#F99C58','padding':'10px'}),
    html.Div([ # Explanatory Paragraph and Dropdown
        html.Div(children = [
                html.H6('''This page is for users to search for teams meeting specific criteria to see how they tend to perform. Start by selecting your desired columns from the dropdown below. The chart will display these columns, with all data collected. This data can be filtered using the first box under the column name. For numerical data, use operators such as =, < or >= in front of the numbers you'd like to filter. For non-numerical data, it will text match anywhere within the value (e.g. 'Virginia' will include 'Virginia' as well as 'West Virginia' or 'Virginia Tech'). The table can be sorted by a specific column by pressing the arrow next to the column's name.''')
        ], style={'display':'flex', 'justifyContent':'center'}),
    ], className = 'row', style={'display':'flex', 'justifyContent':'center','backgroundColor':'#7092F4','padding':'10px'}),
    html.Div([ # Contain Dropdown to select table column
        html.Div([
            dcc.Dropdown(
                id = 'column_selector',
                options = columns,
                multi = True,
                value = ['YEAR','TEAM','SEED','ROUND','KADJ O', 'KADJ D', 'KADJ EM', 'EFG%']
            )
        ])
    ], className='row', style={'backgroundColor': '#7092F4','padding':'10px'}),
    html.Div([ # Contain graph
        dash_table.DataTable(
            id = 'Table',
            columns=[
            {"name": i, "id": i} for i in columns
            ],
            data = data.to_dict('records'),
            filter_action = 'native', # Make table filterable
            sort_action = 'native', # Make data sortable
            style_data_conditional=[ # Alternate Striping
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(220, 220, 220)',
                }
            ]
        )
    ], className='row', style={'backgroundColor':'#D3D3D3'})
])

@callback( # Callback to update columns
    Output("Table", "columns"), 
    Input("column_selector", "value")
)
def display_table(cols):
    column=[
            {"name": i, "id": i} for i in cols
            ]
    return column




# %%



