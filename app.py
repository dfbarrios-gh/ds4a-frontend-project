import requests
import pandas as pd
import json 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
app.title = 'DS4A 2020 Team35'

#global
url = "http://ec2-3-128-198-12.us-east-2.compute.amazonaws.com"

#graphic-one
accidentsPerSubtown = pd.read_json(url + "/accident-number/subtown")
accidentsPerSubtown.rename(columns={'NumberOfAccidents':'Number of Accidents'}, inplace = True)
figAccidentsPerSubtown = px.bar(accidentsPerSubtown, x = "Subtown", y = "Number of Accidents", barmode = "group")

#graphic-two
accidentsPerDayOfWeek = pd.read_json(url + "/accident-number/day-of-week")
accidentsPerDayOfWeek.rename(columns={'NumberOfAccidents':'Number of Accidents','DayOfWeek': 'Day of the week'}, inplace = True)
figAccidentsPerDayOfWeek = px.bar(accidentsPerDayOfWeek, x = "Day of the week", y = "Number of Accidents", barmode = "group")
figAccidentsPerDayOfWeek.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width = 1.5, opacity = 0.6)
#figAccidentsPerDayOfWeek.update_layout(title_text='Number of accidents Vs Day of week')

#graphic-three
accidentsPerHourOfDay = pd.read_json(url + "/accident-number/hour-of-day")
accidentsPerHourOfDay.rename(columns={'NumberOfAccidents':'Number of Accidents', 'Hour': 'Hour of Day'}, inplace = True)
figAccidentsPerHourOfDay = px.bar(accidentsPerHourOfDay, x = "Hour of Day", y = "Number of Accidents", barmode = "group")
figAccidentsPerHourOfDay.update_traces(marker_color='rgb(242,43,0)', marker_line_color='rgb(242,43,0)', marker_line_width = 1.5, opacity = 0.6)

app.layout = html.Div([
    html.Div(
        children = [
            html.H1(children='Graphic: Number of accidents per subtown'),
            html.Div(children='''Summary: This graphic shows the total number of accidents in each individual sub-town.'''),
            dcc.Graph(id='accidents-per-subtown', figure = figAccidentsPerSubtown)
        ], style = {'width': '60%', 'display': 'inline-block', 'vertical-align': 'middle', 'padding-left': '20%', 'padding-top': '2%', 'text-align' : 'center'}),
        html.Div(
        children = [
            html.H1(children='Graphic: Number of accidents per day of the week'),
            html.Div(children='''Summary: This graphic shows the total number of accidents per each day of the week.'''),
            dcc.Graph(id='accidents-per-day-of-week', figure = figAccidentsPerDayOfWeek)
        ], style = {'width': '60%', 'display': 'inline-block', 'vertical-align': 'middle', 'padding-left': '20%', 'padding-top': '5%', 'text-align' : 'center'}),
        html.Div(
        children = [
            html.H1(children='Graphic: Number of accidents per hour of the day'),
            html.Div(children='''Summary: This graphic shows the total number of accidents per each hour of the day.'''),
            dcc.Graph(id='accidents-per-hour-of-day', figure = figAccidentsPerHourOfDay)
        ], style = {'width': '60%', 'display': 'inline-block', 'vertical-align': 'middle', 'padding-left': '20%', 'padding-top': '5%', 'text-align' : 'center'})
])

#configuration
if __name__ == '__main__':
    app.run_server(debug=True)