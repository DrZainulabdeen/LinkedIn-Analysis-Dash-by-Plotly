import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
import calendar
from wordcloud import  wordcloud
from dash import Dash, html, dcc
from dash_extensions import Lottie


url_coonections = "https://assets9.lottiefiles.com/private_files/lf30_5ttqPi.json"
url_companies = "https://assets9.lottiefiles.com/packages/lf20_EzPrWM.json"
url_msg_in = "https://assets9.lottiefiles.com/packages/lf20_8wREpI.json"
url_msg_out = "https://assets2.lottiefiles.com/packages/lf20_Cc8Bpg.json"
url_reactions = "https://assets2.lottiefiles.com/packages/lf20_nKwET0.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([
    # dashboard logo and title
    dbc.Row([
        dbc.Col([dbc.Card([dbc.CardImg(src='/assets/linkedin-logo.png')])], width=2),
        dbc.Col([html.H1('LinkedIn data analysis', className='mt-4')], width=4),
        dbc.Col([dcc.DatePickerSingle(id='date_start', date=date(2020, 1, 1), className='mt-3')], width=2),
        dbc.Col([dcc.DatePickerSingle(id='date_end', date=date(2022,1,1), className='mt-3')], width=2)
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
                html.H3(id='card_messages_received', children='000')
            ], style={'textAlign': 'center'})])], width=2),
        dbc.Col([dbc.Card([
            dbc.CardHeader([Lottie(options=options, height='40%', width='75%', url=url_msg_out)]),
            dbc.CardBody([
                html.H6('Messages sent'),
                html.H3(id='card_messages_sent', children='000')
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


if __name__ == '__main__':
    app.run_server(debug=True)