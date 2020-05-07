import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def mil():
    url_pop = 'https://covid.ourworldindata.org/data/ecdc/locations.csv'
    world_pop = pd.read_csv(url_pop,sep=",")
    url = 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'
    covid_new = pd.read_csv(url, sep=",")
    covid_new_plot = covid_new
    covid_new_plot = covid_new_plot.drop(index= covid_new[covid_new_plot['location']=='World'].index,axis=0)
    covid_new = covid_new.groupby('location', as_index=False).max()
    covid_new = covid_new.drop(index= covid_new[covid_new['location']=='World'].index,axis=0)
    covid_new = covid_new.groupby('location', as_index=False).max()
# mapping the two dataset for population 
    covid_pop = (covid_new.merge(world_pop, left_on='location', right_on='location')
              .reindex(columns=['location', 'date', 'new_cases', 'new_deaths', 'total_cases',
           'total_deaths','population','continent']))

    st.title('Cases Per Million Analysis')
    max_val = covid_pop.index.size -1
    opt = st.selectbox('Type of Cases',('Confirmed','Deaths'))
    idx = st.slider('Slide to Limit The Number of Countries',min_value=0, max_value=max_val, value=[0,max_val])

    # Cases per million population
    covid_pop['per_mil_cases'] = (covid_pop['total_cases']/covid_pop['population'])*1000000
    covid_pop['per_mil_deaths'] = (covid_pop['total_deaths']/covid_pop['population'])*1000000
    covid_pop = covid_pop.fillna(0)
    covid_pop = covid_pop.astype({'per_mil_cases':'int64','per_mil_deaths':'int64'})

    if opt == 'Confirmed':
        fig = px.bar(covid_pop.iloc[min(idx):max(idx),:], x="location", y='per_mil_cases',template='plotly_dark', title='COVID-19 Confirmed Cases',
        labels={'per_mil_cases':'Cases Per Million','location':'Country'}, width=975, height=600)
        st.plotly_chart(fig)
    else:
        fig = px.bar(covid_pop.iloc[min(idx):max(idx),:], x="location", y='per_mil_deaths',template='plotly_dark', title='COVID-19 Death Cases',
        labels={'per_mil_deaths':'Deaths Per Million','location':'Country'}, width=975, height=600)
        st.plotly_chart(fig)
    st.write('©Rakesh Choudhury')