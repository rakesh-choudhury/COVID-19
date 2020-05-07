import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def analysis():
    st.title('COVID-19 GLOBAL CASES ANALYSIS')
    url_pop = 'https://covid.ourworldindata.org/data/ecdc/locations.csv'
    world_pop = pd.read_csv(url_pop,sep=",")
    url = 'https://covid.ourworldindata.org/data/ecdc/full_data.csv'
    covid_new = pd.read_csv(url, sep=",")
    covid_new_plot = covid_new
    covid_new_plot = covid_new_plot.drop(index= covid_new[covid_new_plot['location']=='World'].index,axis=0)
    covid_new = covid_new.groupby('location', as_index=False).max()
    covid_new = covid_new.drop(index= covid_new[covid_new['location']=='World'].index,axis=0)
    covid_new = covid_new.groupby('location', as_index=False).max()

    opt = st.multiselect('Select Countries', covid_new_plot.location.unique().tolist(), default=covid_new_plot.location.unique()[190:197].tolist())
    opt1 = st.selectbox('Type of Case',('Confirmed','Deaths'))
    opt_lin_log = st.radio('Select the type of scale',['Log Scale','Linear Scale'])
    if opt_lin_log == 'Linear Scale':
        scale =False
    else:
        scale=True

    df = covid_new_plot[covid_new_plot['location'].isin(opt)]

    # Log Linear Graph
    if opt1== 'Confirmed':
        fig = px.line(df, x="date", y='total_cases',template='plotly_dark', color='location', title='COVID-19 TOTAL CONFIRMED CASES',
        log_y=scale, width=975, height=600, labels={'total_cases':'Total Cases','location':'Country','date':'Date'})
        st.plotly_chart(fig)
        # Daily Cases
        #df = covid_new[covid_new['location'].isin(opt)]
        fig = px.line(df, x="date", y='new_cases',template='plotly_dark', title='Daily Confirmed Cases', color='location',
        labels={'new_cases':'Daily New Cases','location':'Country','date':'Date'}, width=975, height=600)
        st.plotly_chart(fig)
    else:
        fig = px.line(df, x="date", y='total_deaths',template='plotly_dark', color='location', title='COVID-19 TOTAL DEATH CASES',
        log_y=scale, width=975, height=600, labels={'total_deaths':'Total Deaths','location':'Country','date':'Date'})
        st.plotly_chart(fig)
        fig = px.line(df, x="date", y='new_deaths',template='plotly_dark', title='Daily Death Cases', color='location',
        labels={'new_deaths':'Daily New Cases','location':'Country','date':'Date'}, width=975, height=600)
        st.plotly_chart(fig)
    st.write('©Rakesh Choudhury')