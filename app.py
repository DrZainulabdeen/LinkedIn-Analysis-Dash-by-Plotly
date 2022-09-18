import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
from datetime import date
from wordcloud import wordcloud
from dash import Dash, html, dcc
from dash_extensions import Lottie


url_coonections = "https://assets9.lottiefiles.com/private_files/lf30_5ttqPi.json"
url_companies = "https://assets9.lottiefiles.com/packages/lf20_EzPrWM.json"
url_msg_in = "https://assets9.lottiefiles.com/packages/lf20_8wREpI.json"
url_msg_out = "https://assets2.lottiefiles.com/packages/lf20_Cc8Bpg.json"
url_reactions = "https://assets2.lottiefiles.com/packages/lf20_nKwET0.json"

# lottie options
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

df_connections = pd.read_csv('data/Connections.csv', parse_dates=['Connected On'])
df_connections['month'] = df_connections['Connected On'].dt.month_name()

# reading linkedin data
df_invitations = pd.read_csv('data/Invitations.csv', parse_dates=['Sent At'])
df_reactions = pd.read_csv('data/Reactions.csv', parse_dates=['Date'])
df_messages = pd.read_csv('data/messages.csv', parse_dates=['DATE'])

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([
    # dashboard logo and title
    dbc.Row([
        dbc.Col([dbc.Card([dbc.CardImg(src='/assets/linkedin-logo.png')])], width=2),
        dbc.Col([html.H1('LinkedIn data analysis', className='mt-4')], width=4),
        dbc.Col([dcc.DatePickerSingle(id='date_start', date=date(2020, 1, 1), className='mt-3')], width=2),
        dbc.Col([dcc.DatePickerSingle(id='date_end', date=date(2022,8,1), className='mt-3')], width=2)
    ], className='mt-2'),
    # cards with animations
    dbc.Row([
        dbc.Col([dbc.Card([
            dbc.CardHeader([Lottie(options=options, height='70%', width='95%', url=url_coonections)]),
            dbc.CardBody([
                html.H6('Connections'),
                html.H3(id='card_connections', children='000')
            ], style={'textAlign': 'center'})])], width=2),
        dbc.Col([dbc.Card([
            dbc.CardHeader([Lottie(options=options, height='70%', width='45%', url=url_companies)]),
            dbc.CardBody([
                html.H6('Companies'),
                html.H3(id='card_companies', children='000')
            ], style={'textAlign': 'center'})])], width=2),
        dbc.Col([dbc.Card([
            dbc.CardHeader([Lottie(options=options, height='70%', width='35%', url=url_msg_in)]),
            dbc.CardBody([
                html.H6('Messages received'),
                html.H3(id='card_messages_in', children='000')
            ], style={'textAlign': 'center'})])], width=2),
        dbc.Col([dbc.Card([
            dbc.CardHeader([Lottie(options=options, height='40%', width='75%', url=url_msg_out)]),
            dbc.CardBody([
                html.H6('Messages sent'),
                html.H3(id='card_messages_out', children='000')
            ], style={'textAlign': 'center'})])], width=2),
        dbc.Col([dbc.Card([
            dbc.CardHeader([Lottie(options=options, height='35%', width='35%', url=url_reactions)]),
            dbc.CardBody([
                html.H6('Reactions'),
                html.H3(id='card_reactions', children='000')
            ], style={'textAlign': 'center'})])], width=2),
    ], className='mb-2'),
    # line chart and bar chart
    dbc.Row([
        dbc.Col([dbc.Card([dbc.CardBody([
            dcc.Graph(id='line_chart', figure={})
        ])])], width=6),
        dbc.Col([dbc.Card([dbc.CardBody([
            dcc.Graph(id='bar_chart', figure={})
        ])])], width=4)
    ], className='mb-2'),
    # charts TBD, pie chart and word cloud
    dbc.Row([
        dbc.Col([dbc.Card([dbc.CardBody([
            dcc.Graph(id='tbd', figure={})
        ])])], width=3),
        dbc.Col([dbc.Card([dbc.CardBody([
            dcc.Graph(id='pie_chart', figure={})
        ])])], width=3),
        dbc.Col([dbc.Card([dbc.CardBody([
            dcc.Graph(id='word_cloud', figure={})
        ])])], width=4)
    ])
], fluid=True)


@app.callback(
    Output('card_connections', 'children'),
    Output('card_companies', 'children'),
    Output('card_messages_in', 'children'),
    Output('card_messages_out', 'children'),
    Output('card_reactions', 'children'),
    Input('date_start', 'date'),
    Input('date_end', 'date')
)
def update_small_cards(date_start, date_end):
    df_temp_connections = df_connections.copy()
    df_temp_connections = df_temp_connections[(df_temp_connections['Connected On'] >= date_start) & (df_temp_connections['Connected On'] <= date_end)]
    connections = len(df_temp_connections)
    companies = len(df_temp_connections['Company'].unique())
    df_temp_invitations = df_invitations.copy()
    df_temp_invitations = df_temp_invitations[(df_temp_invitations['Sent At'] >= date_start) & (df_temp_invitations['Sent At'] <= date_end)]
    numbers_in = len(df_temp_invitations[df_temp_invitations['Direction'] == 'INCOMING'])
    numbers_out = len(df_temp_invitations[df_temp_invitations['Direction'] == 'OUTGOING'])
    df_temp_reactions = df_reactions.copy()
    df_temp_reactions = df_temp_reactions[(df_temp_reactions['Date'] >= date_start) & (df_temp_reactions['Date'] <= date_end)]
    reactions = len(df_temp_reactions)

    return connections, companies, numbers_in, numbers_out, reactions


if __name__ == '__main__':
    app.run_server(debug=True)
