import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
import calendar
from wordcloud import  wordcloud
from dash import Dash, html, dcc
from dash_extensions import Lottie


app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([dbc.Card([dbc.CardImg(src='/assets/linkedin-logo.png')])], width=2),
        dbc.Col([html.H1('Linked In data analysis', className='mt-4')], width=8)
    ], className='mt-2'),
    dbc.Row([
        dbc.Col([dbc.Card([dbc.CardBody([])])], width=2),
        dbc.Col([dbc.Card([dbc.CardBody([])])], width=2),
        dbc.Col([dbc.Card([dbc.CardBody([])])], width=2),
        dbc.Col([dbc.Card([dbc.CardBody([])])], width=2),
        dbc.Col([dbc.Card([dbc.CardBody([])])], width=2),
    ], className='mb-2'),
    dbc.Row([
        dbc.Col([dbc.Card([dbc.CardBody([])])], width=6),
        dbc.Col([dbc.Card([dbc.CardBody([])])], width=4)
    ], className='mb-2'),
    dbc.Row([
        dbc.Col([dbc.Card([dbc.CardBody([])])], width=3),
        dbc.Col([dbc.Card([dbc.CardBody([])])], width=3),
        dbc.Col([dbc.Card([dbc.CardBody([])])], width=4)
    ])
], fluid=True)


if __name__ == '__main__':
    app.run_server(debug=True)