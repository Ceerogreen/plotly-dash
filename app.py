import dash
from dash import Dash, html, dcc

stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, use_pages=True, external_stylesheets=stylesheets)
server = app.server

app.layout = html.Div([
    html.H1('March Madness',style={'font-size': '6rem','padding':'10px','padding-bottom':'0px'}),
    html.Div([
        html.Div([
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
    ], className = 'three columns', style={'display':'flex','padding':'10px','font-size': '1.7rem'}) for page in dash.page_registry.values()
    ], className= 'row', style={'display':'flex','padding':'10px'}),
    dash.page_container
], style={'backgroundColor':'#D3D3D3','padding':'5px'})

if __name__ == '__main__':
    app.run(debug=True, jupyter_mode='tab',port=8040)