# Importing required libraries
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import dash
import os
import sys

from dash import dcc
from dash import html
from dash.dependencies import Input, Output,State

import warnings
warnings.filterwarnings('ignore')

# Describing path to import the import_data.py file which is required ahead:
path = ('../src/data/')
sys.path.append(path)
# Importing python file from src folder:
import import_data

# Importing lists of the countries and list of country information:
list_cases_country,df_country_info=import_data.import_cases_data()

# Reading all the saved .csv data-files created previously:
df_input_large = pd.read_csv('../data/processed/COVID_final_set.csv',sep=';')
df = pd.read_csv('../data/processed/COVID_CRD.csv',sep=';')
df_input_sir = pd.read_csv('../data/processed/COVID_sir_fitted_table.csv',sep=';')
df_all = df_input_sir.columns
df_all = list(df_all[:109])
df_list=pd.read_csv('../data/processed/Cases_pop_NoNaN.csv',sep=';')
df_vacc_list=pd.read_csv('../data/processed/Vax_per_pop.csv', sep=';')


country_name=df_country_info['location'].unique()
country_iso_code=df_country_info['iso_code'].unique()



'''Dashboard is created by using an external stylesheet named BOOTSTRAP. 
BOOTSTRAP allows us to divide the dashboard into Rows and columns.
COVID-19 dashbord has 5 Rows'''

# Creating Dashboard for all the plots:
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'COVID-19 Dashboard'

app.layout = html.Div([
        # First Row: Information regarding dashboard page
        dbc.Row(dbc.Col(html.Div(dcc.Markdown('''
                            # Enterprise Data Science: COVID-19 Data Analytics SoSe22:
                            Pranav Atul Patwardhan (419148)

                            Goals of the project:
                            - To plot cases/population and vaccination/population.
                            - To trace the confirmed cases for all the countries.
                            - To calculate the doubling rate.
                            - To simulate the spread of COVID-19 using SIR model.
                            - To create a user friendly dashboard, which shows the current count of confirmed cases, world map, doubling rate and SIR model.
                            ''')),
                        style={
                            'fontFamily':'arial',
                            'textAlign':'left',
                            'backgroundColor':'#05445E',
                            'color': '#D4F1F4',
                        },
                        width={'size': 20, 'offset': 0},
                        )
                ),
        # Second Row: Dropdowns for Confirmed Cases and Doubling Rate
        dbc.Row(
            [   #Dropdown for Timeline Confirmed and Doubling rate
                dbc.Col(dcc.Dropdown(
                            id='country_dropdown',
                            options=[ {'label': each,'value':each} for each in df_input_large['COUNTRY'].unique()],
                            value=['Australia', 'United Kingdom','Hong Kong'], # which are pre-selected
                            multi= True),
                        
                        width={'size': 5, "offset": 1, 'order': 'first'}
                        ),

                dbc.Col(
                        dcc.Dropdown(
                            id='doubling_time',
                            options=[
                                {'label': 'Timeline Confirmed ', 'value': 'confirmed'},
                                {'label': 'Timeline Confirmed Filtered', 'value': 'confirmed_filtered'},
                                {'label': 'Timeline Doubling Rate', 'value': 'confirmed_DR'},
                                {'label': 'Timeline Doubling Rate Filtered', 'value': 'confirmed_filtered_DR'}
                            ],
                            value='confirmed',
                            multi=False
                            ),
                        width={'size': 3, "offset": 1, 'order': 'second'}
                        ),

                ], className="g-0",
                #style=dict(display='flex')
        ),

        # Third Row: Graphs for cases/confirmed cases/Doubling rate and graph for cases per population:                        
        dbc.Row(
            [
                dbc.Col(dcc.Graph( 
                            id='main_window_slope'
                            ),
                        width=6, md={'size': 5,  "offset": 1, 'order': 'first'}
                        ),

            ],
                ),

        # Fourth Row: Dropdown for cases per population:                     
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(
                            id='country_drop_down',
                            options=[{'label':country_name[each],'value':country_iso_code[each]} for each in range(len(country_name))],
                            value=['AUS', 'GBR'],
                            multi= True),
                          
                        width={'size': 5, "offset": 1, 'order': 'first'}                         
                        ),

            ],
                ),
    
        # Fifth Row: Graph for cases per population:                        
        dbc.Row(
            [
                dbc.Col(dcc.Graph(
                            id='cases_per_pop'
                            ),
                        width=6, md={'size': 5,  "offset": 1, 'order': 'first'}
                        ),                
            ],
                ),
        # Sixth Row: Dropdown for vaccination per population:
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(
                        id='country_vacc_data',
                        options=[{'label':country_name[each],'value':country_iso_code[each]} for each in range(len(country_name))],
                        value=['AUS', 'GBR'],
                        multi= True),
                                
                    width={'size': 5, "offset": 1, 'order': 'second'}                         
                   ),
            ], className="g-0",
                ),

        # Seventh Row: Graph for vaccination per population:                        
        dbc.Row(
            [
                dbc.Col(dcc.Graph(
                            id='vacc_data'
                            ),
                        width=6, md={'size': 5,  "offset": 1, 'order': 'first'}
                        ),              
            ],
                ),

        # Eighth Row: Dropdown SIR:                        
        dbc.Row(
            [
                #Dropdown for SIR model
                dbc.Col(dcc.Dropdown(
                            id='country_dropdown_sir',
                            options=[ {'label': each,'value':each} for each in df_all[1:]],
                            value='India', # which are pre-selected
                            multi= False
                            ),
                           
                        width={'size': 5, "offset": 1, 'order': 'second'}
                        ),               
            ],
                ),
        # Ninth Row: SIR Graph:
        dbc.Row(
            [
                dbc.Col(dcc.Graph(
                            id='SIR_model'
                            ),
                        width=6, md={'size': 5,  "offset": 1, 'order': 'first'}
                        ),
            ],
                ),
        # Tenth Row: World Map
        dbc.Row(
                dbc.Col(dcc.Graph(id = "World_map",
                              figure = go.Figure(data = [go.Choropleth(
                                        locations = df['CODE'],
                                        z = df['Confirm cases'],
                                        text = df['COUNTRY'],
                                        colorscale = 'Blues',
                                        autocolorscale=False,
                                        reversescale=False,
                                        marker_line_color='darkgray',
                                        marker_line_width=0.5,
                                        colorbar_title = 'Confirmed cases'
                                        )],
                                        layout = go.Layout(
                                        title_text='COVID 19 WORLD MAP',
                                        height=900,
                                        autosize = True,
                                        geo=dict(
                                            showframe=False,
                                            showcoastlines=False,
                                            projection_type='equirectangular'
                                        ))
                                     ),
                              
                              ),
                        width=12, md={'size': 12,  "offset": 0, 'order': 'first'}
                        ),
         )


])


# Cases per population figure plot:
@app.callback(Output('cases_per_pop', 'figure'),
              [Input('country_drop_down', 'value')])
def Cases_fig(list_cases_country):

    traces = []
    for each in list_cases_country:
        traces.append(
            dict(x=df_list.date,
                 y=df_list['Cases_per_pop_' + each],
                 mode='markers+lines',
                 opacity=0.9,
                 line_width=2,
                 marker_size=1,
                 name=each))

    return {
        'data':
        traces,
        'layout':
        dict(width=1280,
             height=900,
             title='Plot for Cases per Population',
             plot_bgcolor='#D9E4EC',
             xaxis={'title':'Date',
                 'tickangle': -45,
                 'nticks': 20,
                 'tickfont': dict(size=14, color='#189AB4'),
             },
             yaxis={'title':'Relative COVID Cases (Absolute Cases/Total Population)',
                 'type': 'log',
                 'range': '[1.1, 5.5]'
             })
    }





# Vaccination Figure plot:
@app.callback(Output('vacc_data', 'figure'),
              [Input('country_vacc_data', 'value')])
def Vacc_fig(list_cases_country):

    traces = []
    for each in list_cases_country:
        traces.append(
            dict(x=df_vacc_list.date,
                 y=df_vacc_list['Vacc_per_pop_' + each],
                 mode='markers+lines',
                 opacity=0.9,
                 line_width=2,
                 marker_size=1,
                 name=each))

    return {
        'data':
        traces,
        'layout':
        dict(width=1280,
             height=900,
             title='Plot for Vaccination Data',
             plot_bgcolor='#D9E4EC',
             xaxis={'title':'Date',
                 'tickangle': -45,
                 'nticks': 20,
                 'tickfont': dict(size=14, color='#189AB4'),
             },
             yaxis={'title':'Relative Vaccination(Total Vaccination/Total Population)',
                 'type': 'log',
                 'range': '[1.1, 5.5]'
             })
    }



# Confirmed Cases, Doubling Rate Figure plot:
@app.callback(
    Output('main_window_slope', 'figure'),
    [Input('country_dropdown', 'value'),
    Input('doubling_time', 'value')])

def update_figure(country_list,show_doubling):


    if 'DR' in show_doubling:
        my_yaxis={'type':"log",
               'title':'Approximated doubling rate over 3 days (larger numbers are better #stayathome)'
              }
    else:
        my_yaxis={'type':"log",
                  'title':'Confirmed infected people (source johns hopkins csse, log-scale)'
              }


    traces = []
    for each in country_list:

        df_plot=df_input_large[df_input_large['COUNTRY']==each]

        if show_doubling=='doubling_rate_filtered':
            df_plot=df_plot[['state','COUNTRY','confirmed','confirmed_filtered','confirmed_DR','confirmed_filtered_DR','date']].groupby(['COUNTRY','date']).agg(np.mean).reset_index()
        else:
            df_plot=df_plot[['state','COUNTRY','confirmed','confirmed_filtered','confirmed_DR','confirmed_filtered_DR','date']].groupby(['COUNTRY','date']).agg(np.sum).reset_index()
       #print(show_doubling)


        traces.append(dict(x=df_plot.date,
                                y=df_plot[show_doubling],
                                mode='markers+lines',
                                opacity=0.9,
                                name=each
                        )
                )

    return {
            'data': traces,
            'layout': dict (
                width=1280,
                height=900,
                plot_bgcolor='#D9E4EC',
                xaxis={'title':'Timeline',
                        'tickangle':-45,
                        'nticks':20,
                        'tickfont':dict(size=14,color="#189AB4"),
                      },

                yaxis=my_yaxis
        ) 
    }
# SIR Model plot:
@app.callback(
    Output('SIR_model', 'figure'),
    [Input('country_dropdown_sir', 'value')])

def SIR_fig(con_input):
    df= df_input_sir
   
    
    for i in df[1:]:
        data = []
        trace = go.Scatter(x=df.date,
                        y=df[con_input],
                        mode='lines+markers',
                        name = con_input)
        data.append(trace)
        
        trace_fitted = go.Scatter(x=df.date,
                        y=df[con_input +'_fitted'], 
                        mode='lines+markers',
                        name=con_input+'_fitted')
        data.append(trace_fitted)
        
        
            
    return {'data': data,
            'layout' : dict(
                width=1280,
                height=900,
                title= 'SIR model',
                plot_bgcolor='#D9E4EC',
                xaxis={'tickangle':-45,
                        'nticks':20,
                        'tickfont':dict(size=14,color="#189AB4"),
                      },
                yaxis={'type':"log",
                       'range':'[1.1,5.5]'
                      }
                
            )
        }

if __name__ == '__main__':

# Running the application to show Dashboard:
    app.run_server(debug=True, port= 8051, use_reloader=False)