import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from urllib.request import urlopen
import json

def usa():
#USA state map
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
    # st.markdown('## Cases in different counties in USA')
    st.title('COVID-19 Cases in different counties of USA')
    opt = st.radio('Type of cases',('Confirmed','Deaths'))
    if opt=='Confirmed':
        color=(0,3000)
    else:
        color=(0,200)
    covid_usa = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv",
                       dtype={"fips": str})
    covid_usa = covid_usa.rename(columns={'cases':'Confirmed','deaths':'Deaths'})
    df = covid_usa.groupby(['county','fips'], as_index=False).max()

    fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color=opt, hover_name='county',
                               #color_continuous_scale="Viridis", 
                               range_color=color,
                               mapbox_style="carto-positron",
                               zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                               opacity=0.5,
                               #labels={'unemp':'unemployment rate'}
                               color_continuous_scale= ['#EFEC2B','#69EF2B','#2BEFE3','#2B40EF','#C82BEF','#EF2B4C'], 
                               template='plotly_dark', labels={'fips':'County Code'},
                               width=930, height=600
                              )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig)
    
# COVID-19 USA
    covid_usa = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv",sep=",")

    opt = st.multiselect('Select States', covid_usa.state.unique().tolist(), default=covid_usa.state.unique()[20:25].tolist())
    opt1 = st.selectbox('Type of Case in USA',('Confirmed','Deaths'))
    opt_lin_log = st.radio('Select the Type of Scale',['Log Scale','Linear Scale'])
    if opt_lin_log == 'Linear Scale':
        scale =False
    else:
        scale=True
    df = covid_usa.groupby(['date','state'], as_index=False).max()
    df = df[df['state'].isin(opt)]
    if opt1=='Confirmed':
        fig = px.line(df, x="date", y='cases',template='plotly_dark', color='state', title='TOTAL CONFIRMED CASES', 
        log_y=scale, width=975, height=600, labels={'cases':'Confirmed Cases','date':'Date'})
        st.plotly_chart(fig)
    else:
        fig = px.line(df, x="date", y='deaths',template='plotly_dark', color='state', title='TOTAL DEATH CASES', 
        log_y=scale, width=975, height=600,labels={'deaths':'Death Cases','date':'Date'})
        st.plotly_chart(fig)

    st.write('©Rakesh Choudhury')