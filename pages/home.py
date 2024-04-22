# %%
import dash
from dash import Dash, html, dcc

# %%
stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] # Get stylesheets

# %%
dash.register_page(__name__, path='/')

# %%
layout = html.Div([
    html.Div([ # Create Title
        html.Div([
            html.H1('''Home''')
        ], style={'display':'flex', 'justifyContent':'center','backgroundColor':'#F99C58'}),
    ], className = 'row', style={'display':'flex', 'justifyContent':'center','backgroundColor':'#F99C58','padding':'10px'}),
    html.Div([ # Explanatory Paragraph
        html.Div(children = [
                html.H6('''This app is designed to allow for varying levels of March Madness overview. The entire data is available in a searchable table, as well as graphed on a year to year basis, and based on team. Each page can be found linked above, with descriptions on how to use the page. Data for this page comes from Kaggle user Nishaan Amin, sourced from KenPom, BartTorvik and ESPN webpages. ''')
        ], style={'display':'flex', 'justifyContent':'center'}),
    ], className = 'row', style={'display':'flex', 'justifyContent':'center','backgroundColor':'#7092F4','padding':'10px'}),
    html.Div([ # Data Dictionary
        html.Div(children = [
                html.H6('As there are many abbreviations to be found in the data, provided is a guide to what they all mean:')
        ], style={'display':'flex', 'justifyContent':'center'}),
        
    ], className = 'row', style={'display':'flex','backgroundColor':'#7092F4','padding':'10px'}),
    html.Div([
        dcc.Markdown('''
            YEAR: Ending year of the team's season. <br>
            CONF: Conference Name. <br>
            TEAM NO: Unique identifier for the team and the year they played in.<br>
            TEAM: Division I college basketball team name. <br>
            SEED: Preliminary ranking for the March Madness tournament.<br>
            ROUND/Round Made: Farthest round the team made it in the tournament. 68 = First Four, 64 = Round of 64, 32 = Round of 32, 16 = Sweet 16, 8 = Elite Eight, 4 = Final Four, 2 = Finals , 1 = Champion.<br>
            KADJ O: KenPom estimate of how many points a team would score against the average Division I basketball offense over the course of 100 possessions.<br>
            KADJ D: KenPom estimate of how many points a team would allow against the average Division I basketball defense over the course of 100 possessions.<br>
            KADJ EM: KenPom estimate of how many points a team would outscore the average Division I basketball team by over the course of 100 possessions.<br>
            BADJ O: BartTorvik estimate of how many points a team would score against the average Division I basketball offense over the course of 100 possessions.<br>
            BADJ D: BartTorvik estimate of how many points a team would allow against the average Division I basketball defense over the course of 100 possessions.<br>
            BADJ EM: BartTorvik estimate of how many points a team would outscore the average Division I basketball team by over the course of 100 possessions.<br>
            EFG%: Measures field goal percentage adjusting for made three-point shots being 1.5 times more valuable than made two-point shots.<br>
            EFG%D: Measures field goal percentage adjusting for made three-point shots being 1.5 times more valuable than made two-point shots for the opposing team.<br>
            FTR: The ratio of free throw attempts to field goal attempts.<br>
            FTRD: The ratio of free throw attempts to field goal attempts a team allows.<br>
            TOV%: The percent of turnovers committed by a team.<br>
            TOV%D: The percent of turnovers forced by a team.<br>
            OREB%: The percent of rebounds on the offensive end that a team grabs out of all rebounding opportunities possible.<br>
            DREB%: The percent of rebounds on the defensive end that a team grabs out of all rebounding opportunities possible.<br>
            OP OREB%: The ratio of the opposing team's offensive rebounds to a team's defensive rebounds.<br>
            OP DREB%: The ratio of the opposing team's defensive rebounds to a team's offensive rebounds.
            ''', dangerously_allow_html=True)
    ], className = 'row', style={'display':'flex','backgroundColor':'#D3D3D3','padding':'10px'})
])


# %%


# %%



